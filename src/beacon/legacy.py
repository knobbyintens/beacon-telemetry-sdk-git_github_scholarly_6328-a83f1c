"""Legacy v1 helpers retained for backwards compatibility."""

from __future__ import annotations

from typing import Any, Callable


def deprecated(func: Callable) -> Callable:
    """Mark a callable as deprecated."""
    func.__deprecated__ = True
    return func


@deprecated
def send_event(event: dict[str, Any]) -> bool:
    """Send a single event. Deprecated in favor of send_batch."""
    return True
