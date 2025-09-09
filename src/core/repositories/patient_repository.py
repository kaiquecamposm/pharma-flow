import json
import os
from typing import List, Optional

from src.core.entities.patient import Patient


class PatientRepository:
    """
    Patient repository that uses a JSON file for storage.
    """
    def __init__(self, file_path: str = "/shared/databases/patients.json"):
        if file_path is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))  # current directory
            parent_dir = os.path.dirname(base_dir)  # up one level
            db_dir = os.path.join(parent_dir, "shared", "databases")  # /shared/databases
            os.makedirs(db_dir, exist_ok=True)  # directory exists
            file_path = os.path.join(db_dir, "patients.json")

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
    Add a new patient.
    """
    def add(self, patient: Patient) -> Patient:
        data = self._load_data()
        data.append(patient.__dict__)
        self._save_data(data)
        return patient

    """
    Return a patient by ID.
    """
    def get_by_id(self, patient_id: str) -> Optional[Patient]:
        data = self._load_data()
        for item in data:
            if item["id"] == patient_id and item.get("is_active", True):
                return Patient(**item)
        return None

    """ 
    List all active patients.
    """
    def list_all(self) -> List[Patient]:
        data = self._load_data()
        return [Patient(**item) for item in data if item.get("is_active", True)]

    """ 
    Update a patient by creating a new version (does not overwrite).
    """
    def update(self, patient: Patient) -> Patient:
        data = self._load_data()
        for item in data:
            if item["id"] == patient.id:
                patient.version = item.get("version", 1) + 1
                item.update(patient.__dict__)
                break
        self._save_data(data)
        return patient

    """
    Inactivate a patient (soft delete).
    """
    def inactivate(self, patient_id: str) -> bool:
        data = self._load_data()
        for item in data:
            if item["id"] == patient_id:
                item["is_active"] = False
                self._save_data(data)
                return True
        return False
