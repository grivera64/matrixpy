from dataclasses import dataclass

from .message import Message
from .room import Room


@dataclass
class BroadcastResult:
    """Represents the outcome of sending a message to a single room during a
    space broadcast.

    Use `ok` to check whether the message was delivered, and `error` to
    inspect the failure when it was not.
    """

    room: Room
    message: Message | None
    error: BaseException | None

    @property
    def ok(self) -> bool:
        """Whether the message was sent successfully to the room."""
        return self.error is None
