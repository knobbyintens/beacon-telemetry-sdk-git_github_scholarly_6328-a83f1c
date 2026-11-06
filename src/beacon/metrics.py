"""Metric construction and window summarization (2.0 line)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Iterable


def deprecated(func: Callable) -> Callable:
    """Mark a callable as deprecated."""
    func.__deprecated__ = True
    return func


@deprecated
def build_metric(name: str, value: float, unit: str = "count") -> dict[str, Any]:
    """Build a single metric record.

    Deprecated: new code should use summarize_window instead.
    """
    return {"name": name, "value": value, "unit": unit}


@dataclass
class WindowSummary:
    """Summary of metrics observed during one reporting window."""

    total: float
    samples: int
    unit: str


def summarize_window(metrics: Iterable[dict[str, Any]], unit: str = "count") -> WindowSummary:
    """Summarize metrics over the current reporting window."""
    records = list(metrics)
    total = sum(record["value"] for record in records)
    return WindowSummary(total=total, samples=len(records), unit=unit)
