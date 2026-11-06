"""Beacon telemetry SDK public surface (1.4 line)."""

from .client import flush_buffer, send_batch
from .legacy import send_event
from .metrics import aggregate_rollup, build_metric
from .pipeline import register_stage, run_pipeline

__all__ = [
    "send_batch",
    "flush_buffer",
    "send_event",
    "build_metric",
    "aggregate_rollup",
    "run_pipeline",
    "register_stage",
]
