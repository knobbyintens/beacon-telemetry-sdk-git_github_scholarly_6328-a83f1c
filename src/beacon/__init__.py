"""Beacon telemetry SDK public surface (2.0 line)."""

from .client import configure_transport, flush, send_batch
from .metrics import build_metric, summarize_window
from .pipeline import register_stage, run_pipeline

__all__ = [
    "configure_transport",
    "send_batch",
    "flush",
    "build_metric",
    "summarize_window",
    "run_pipeline",
    "register_stage",
]
