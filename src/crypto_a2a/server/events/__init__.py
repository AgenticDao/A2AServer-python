"""Event handling components for the Crypto A2A server."""

from crypto_a2a.server.events.event_consumer import EventConsumer
from crypto_a2a.server.events.event_queue import Event, EventQueue
from crypto_a2a.server.events.in_memory_queue_manager import InMemoryQueueManager
from crypto_a2a.server.events.queue_manager import (
    NoTaskQueue,
    QueueManager,
    TaskQueueExists,
)


__all__ = [
    'Event',
    'EventConsumer',
    'EventQueue',
    'InMemoryQueueManager',
    'NoTaskQueue',
    'QueueManager',
    'TaskQueueExists',
]
