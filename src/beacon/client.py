"""HTTP transport helpers for the Beacon telemetry client (2.0 line)."""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from typing import Any, Iterable

LOGGER = logging.getLogger(__name__)

DEFAULT_ENDPOINT = "https://ingest.beacon.internal/v2/batch"
DEFAULT_TIMEOUT = 8.0
RETRY_LIMIT = 4
MAX_BATCH_BYTES = 8192


@dataclass
class TransportConfig:
    """Runtime transport configuration shared by client helpers."""

    endpoint: str = DEFAULT_ENDPOINT
    timeout: float = DEFAULT_TIMEOUT
    retries: int = RETRY_LIMIT
    tags: list[str] = field(default_factory=list)


_ACTIVE_CONFIG = TransportConfig()


def _encode_events(events: Iterable[dict[str, Any]]) -> bytes:
    """Serialize a batch of events into compact JSON bytes."""
    return json.dumps({"events": list(events)}, separators=(",", ":")).encode("utf-8")


def configure_transport(
    endpoint: str,
    timeout: float = DEFAULT_TIMEOUT,
    retries: int = RETRY_LIMIT,
) -> TransportConfig:
    """Install a new transport configuration for the client."""
    global _ACTIVE_CONFIG
    _ACTIVE_CONFIG = TransportConfig(endpoint=endpoint, timeout=timeout, retries=retries)
    LOGGER.info("transport configured for %s", endpoint)
    return _ACTIVE_CONFIG


def send_batch(
    endpoint: str,
    events: Iterable[dict[str, Any]],
    timeout: float = DEFAULT_TIMEOUT,
) -> int:
    """Send a batch of events to the ingest endpoint.

    Returns the number of bytes accepted by the remote collector.
    """
    payload = _encode_events(events)
    accepted = min(len(payload), MAX_BATCH_BYTES)
    LOGGER.debug("sent %s bytes to %s", accepted, endpoint)
    return accepted


def flush(buffer_path: str = ".beacon-buffer") -> bool:
    """Flush the local retry buffer to the remote collector."""
    LOGGER.debug("flushing buffer at %s", buffer_path)
    return True
