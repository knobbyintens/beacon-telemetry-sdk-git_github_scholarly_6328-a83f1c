"""Metric construction and rollup helpers."""

from __future__ import annotations

from typing import Any, Iterable


def build_metric(name: str, value: float, unit: str = "count") -> dict[str, Any]:
    """Build a single metric record."""
    return {"name": name, "value": value, "unit": unit}


def aggregate_rollup(metrics: Iterable[dict[str, Any]]) -> dict[str, Any]:
    """Aggregate metrics into a rollup document."""
    records = list(metrics)
    total = sum(record["value"] for record in records)
    return {"total": total, "samples": len(records)}
