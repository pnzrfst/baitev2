from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from uuid import uuid4

## This class is our factory of clips. Whenever you need to create a new clip or read a clip, you can call it with their methods to help you to find what you're looking for.


@dataclass
class Clip:
    text: str
    created_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    id: str = field(default_factory=lambda: str(uuid4()))

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def to_raw(cls, raw) -> "Clip":
        if isinstance(raw, str):
            return cls(text=raw)
        return cls(**raw)
