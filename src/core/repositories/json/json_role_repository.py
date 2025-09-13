import json
import os
from typing import List, Optional

from core.entities.role import Role
from core.entities.user import User
from core.repositories.role_repository import RoleRepository

DB_DIR = "src/core/shared/databases/roles.json"

class JSONRoleRepository(RoleRepository):
    """
    Role repository that uses a JSON file for storage.
    """
    def __init__(self):
        db_dir = os.path.dirname(DB_DIR)
        os.makedirs(db_dir, exist_ok=True)

        file_path = os.path.join(db_dir, "roles.json")

        self.file_path = file_path
        # Ensure the file exists
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump([], f)

    """
    Load data from the JSON file.
    """
    def _load_data(self) -> List[dict]:
        with open(self.file_path, "r", encoding="utf-8") as f:
            return json.load(f)
        
    """
    Save data to the JSON file.
    """
    def _save_data(self, data: List[dict]) -> None:
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    """
    Add a new role.
    """
    def add(self, role: Role) -> Role:
        data = self._load_data()
        data.append(role.__dict__)
        self._save_data(data)
        return role

    """
    Return a role by user_id.
    """
    def get_by_user_id(self, user_id: str) -> Optional[Role]:
        data = self._load_data()
        for item in data:
            if item["user_id"] == user_id:
                return Role(**item)
        return None

    """
    List all active users.
    """
    def list_all(self) -> List[User]:
        data = self._load_data()
        return [User(**item) for item in data if item.get("active", True)]
