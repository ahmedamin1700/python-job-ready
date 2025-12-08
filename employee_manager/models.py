from dataclasses import asdict, dataclass
from typing import Any, Dict


@dataclass
class Employee:
    id: int
    name: str
    email: str
    age: int
    role: str

    def to_dict(self) -> Dict[str, Any]:
        """Converts this object into a dictionary."""
        return asdict(self)

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Employee":
        """
        Factory method: Creates an Employee object from a dictionary.
        Example: Employee.from_dict({'name': 'Alice', ...})
        """
        return Employee(
            id=data.get("id", 0),
            name=data["name"],
            email=data["email"],
            age=data["age"],
            role=data["role"],
        )
