import json
import os
from typing import List, Optional

from core.entities.professional import Professional
from core.repositories.professional_repository import ProfessionalRepository

DB_DIR = "src/core/shared/databases/professionals.json"

class JSONProfessionalRepository(ProfessionalRepository):
    """
    Professional repository that uses a JSON file for storage.
    """
    def __init__(self):
        db_dir = os.path.dirname(DB_DIR)
        os.makedirs(db_dir, exist_ok=True)

        file_path = os.path.join(db_dir, "professionals.json")

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
    Add a new professional.
    """
    def add(self, professional: Professional) -> Professional:
        data = self._load_data()
        data.append(professional.__dict__)
        self._save_data(data)
        return professional

    """
    Return a professional by ID.
    """
    def get_by_id(self, professional_id: str) -> Optional[Professional]:
        data = self._load_data()
        for item in data:
            if item["id"] == professional_id and item.get("active", True):
                return Professional(**item)
        return None
    
    """
    Return a professional by email.
    """
    def get_by_email(self, email: str) -> Optional[Professional]:
        data = self._load_data()
        for item in data:
            if item["email"] == email and item.get("active", True):
                return Professional(**item)
        return None

    """
    List all active professionals.
    """
    def list_all(self) -> List[Professional]:
        data = self._load_data()
        return [Professional(**item) for item in data if item.get("active", True)]

    """
    Update a professional by creating a new version (does not overwrite previous version).
    """
    def update(self, professional: Professional) -> Professional:
        data = self._load_data()
        for item in data:
            if item["id"] == professional.id:
                professional.version = item.get("version", 1) + 1
                item.update(professional.__dict__)
                break
        self._save_data(data)
        return professional

    """
    Inactivate a professional (soft delete).
    """
    def inactivate(self, professional_id: str) -> bool:
        data = self._load_data()
        for item in data:
            if item["id"] == professional_id:
                item["active"] = False
                self._save_data(data)
                return True
        return False
