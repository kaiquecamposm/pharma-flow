import json
import os
from typing import List

from core.entities.education_progress import EducationProgress
from core.repositories.education_progress_repository import EducationProgressRepository

DB_DIR = "src/core/shared/databases/education_progress.json"

class JSONEducationProgressRepository(EducationProgressRepository):
    """
    Education progress repository that uses a JSON file for storage.
    """
    def __init__(self):
        db_dir = os.path.dirname(DB_DIR)
        os.makedirs(db_dir, exist_ok=True)

        file_path = os.path.join(db_dir, "education_progress.json")

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
    Create a new education progress entry.
    """
    def add(self, user_id: str, module_id: str) -> EducationProgress:
        data = self._load_data()

        new_progress = EducationProgress(
            user_id,
            module_id,
        )

        data.append(new_progress.__dict__)
        self._save_data(data)

        return new_progress

    """
    Return a education progress entry by ID.
    """
    def get_by_id(self, education_progress_id: str) -> EducationProgress:
        data = self._load_data()
        for item in data:
            if item["id"] == education_progress_id:
                return EducationProgress(**item)
        return None

    """
    Get a education progress entry by user ID and module ID.
    """
    def get_by_user_and_module(self, user_id: str, module_id: str) -> EducationProgress:
        data = self._load_data()
        for item in data:
            if item["user_id"] == user_id and item["module_id"] == module_id:
                return EducationProgress(**item)
        return None

    def list_by_user_id(self, user_id) -> list[EducationProgress]:
        data = self._load_data()
        return [EducationProgress(**item) for item in data if item["user_id"] == user_id]

    """
    Update a education progress entry by creating a new version (does not overwrite previous version).
    """
    def update(self, education_progress_id: str, completed: bool, completed_at: str, score: int) -> EducationProgress:
        data = self._load_data()
        for item in data:
            if item["id"] == education_progress_id:
                item["completed"] = completed
                item["completed_at"] = completed_at
                item["score"] = score
                self._save_data(data)
                return EducationProgress(**item)
        return None
    
