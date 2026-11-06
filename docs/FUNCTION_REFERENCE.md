# Beacon Telemetry SDK - Function Reference

The public surface is defined by the `__all__` list in `src/beacon/__init__.py`.
Line numbers point at the `def` statement of each function in the listed module.

## Active

| Function | Module | Line | Status |
| --- | --- | --- | --- |
| `configure_transport` | `src/beacon/client.py` | 36 | active |
| `flush` | `src/beacon/client.py` | 63 | active |
| `register_stage` | `src/beacon/pipeline.py` | 10 | active |
| `run_pipeline` | `src/beacon/pipeline.py` | 15 | active |
| `send_batch` | `src/beacon/client.py` | 48 | active |
| `summarize_window` | `src/beacon/metrics.py` | 33 | active |

## Deprecated

| Function | Module | Line | Status |
| --- | --- | --- | --- |
| `build_metric` | `src/beacon/metrics.py` | 16 | deprecated |

## Removed

| Function | Module | Line | Status |
| --- | --- | --- | --- |
| `aggregate_rollup` | `src/beacon/metrics.py` | - | removed |
| `flush_buffer` | `src/beacon/client.py` | - | removed |
| `send_event` | `src/beacon/legacy.py` | - | removed |
