import json
import os
from typing import List, Optional

from core.entities.education_module import EducationModule
from core.repositories.education_module_repository import EducationModuleRepository

DB_DIR = "src/core/shared/databases/education_module.json"

class JSONEducationModuleRepository(EducationModuleRepository):
    """
    Education module repository that uses a JSON file for storage.
    """
    def __init__(self):
        db_dir = os.path.dirname(DB_DIR)
        os.makedirs(db_dir, exist_ok=True)

        file_path = os.path.join(db_dir, "education_module.json")

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
    Return a education module entry by ID.
    """
    def get_by_id(self, module_id: str) -> Optional[EducationModule]:
        data = self._load_data()
        for item in data:
            if item["id"] == module_id:
                return EducationModule(**item)
        return None

    """
    List all active education module entries.
    """
    def list_all(self) -> List[EducationModule]:
        data = self._load_data()
        return [EducationModule(**item) for item in data if item.get("active", True)]

    """
    Update a education module entry by creating a new version (does not overwrite previous version).
    """
    def update(self, module: EducationModule) -> EducationModule:
        data = self._load_data()
        for item in data:
            if item["id"] == module.id:
                module.version = item.get("version", 1) + 1
                item.update(module.__dict__)
                break
        self._save_data(data)
        return module

