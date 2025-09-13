import json
import os
from typing import List, Optional

from core.repositories.user_repository import UserRepository

from core.entities.user import User

DB_DIR = "src/core/shared/databases/users.json"

class JSONUserRepository(UserRepository):
    """
    User repository that uses a JSON file for storage.
    """
    def __init__(self):
        db_dir = os.path.dirname(DB_DIR)
        os.makedirs(db_dir, exist_ok=True)

        file_path = os.path.join(db_dir, "users.json")

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
    Add a new user.
    """
    def add(self, user: User) -> User:
        data = self._load_data()
        data.append(user.__dict__)
        self._save_data(data)
        return user

    """
    Return a user by ID.
    """
    def get_by_id(self, user_id: str) -> Optional[User]:
        data = self._load_data()
        for item in data:
            if item["id"] == user_id and item.get("active", True):
                return User(**item)
        return None
    
    """
    Return a user by email.
    """
    def get_by_email(self, email: str) -> Optional[User]:
        data = self._load_data()
        for item in data:
            if item["email"] == email and item.get("active", True):
                return User(**item)
        return None

    """
    List all active users.
    """
    def list_all(self) -> List[User]:
        data = self._load_data()
        return [User(**item) for item in data if item.get("active", True)]

    """
    Update a user by creating a new version (does not overwrite previous version).
    """
    def update(self, user: User) -> User:
        data = self._load_data()
        for item in data:
            if item["id"] == user.id:
                user.version = item.get("version", 1) + 1
                item.update(user.__dict__)
                break
        self._save_data(data)
        return user

    """
    Inactivate a user (soft delete).
    """
    def inactivate(self, user_id: str) -> bool:
        data = self._load_data()
        for item in data:
            if item["id"] == user_id:
                item["active"] = False
                self._save_data(data)
                return True
        return False
