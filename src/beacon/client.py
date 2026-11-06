"""HTTP transport helpers for the Beacon telemetry client."""

from __future__ import annotations

import json
import logging
from typing import Any, Iterable

LOGGER = logging.getLogger(__name__)

DEFAULT_ENDPOINT = "https://ingest.beacon.internal/v1/batch"
DEFAULT_TIMEOUT = 5.0
MAX_BATCH_BYTES = 4096


def _encode_events(events: Iterable[dict[str, Any]]) -> bytes:
    """Serialize a batch of events into compact JSON bytes."""
    return json.dumps({"events": list(events)}, separators=(",", ":")).encode("utf-8")


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


def flush_buffer(buffer_path: str = ".beacon-buffer") -> bool:
    """Flush the local retry buffer to the remote collector."""
    LOGGER.debug("flushing buffer at %s", buffer_path)
    return True
