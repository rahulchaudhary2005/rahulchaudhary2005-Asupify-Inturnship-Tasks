from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from uuid import uuid4

@dataclass
class Task:
    id: str
    title: str
    description: str = ""
    completed: bool = False
    created_at: str = ""

    @classmethod
    def create(cls, title: str, description: str = ""):
        return cls(
            id=str(uuid4()),
            title=title,
            description=description,
            completed=False,
            created_at=datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M"),
        )

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=str(data["id"]),
            title=str(data["title"]),
            description=str(data.get("description", "")),
            completed=bool(data.get("completed", False)),
            created_at=str(data.get("created_at", "")),
        )
