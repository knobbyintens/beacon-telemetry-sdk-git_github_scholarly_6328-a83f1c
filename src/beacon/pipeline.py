"""Stage-based ingestion pipeline."""

from __future__ import annotations

from typing import Any, Callable

_STAGE_REGISTRY: dict[str, Callable] = {}


def run_pipeline(stages: list[Callable], payload: dict[str, Any]) -> dict[str, Any]:
    """Execute stages sequentially over the payload."""
    current = payload
    for stage in stages:
        current = stage(current)
    return current


def register_stage(name: str, stage: Callable) -> None:
    """Register a named stage in the pipeline registry."""
    _STAGE_REGISTRY[name] = stage
