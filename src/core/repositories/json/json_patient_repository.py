import json
import os
from typing import List, Optional

from core.entities.patient import Patient
from core.entities.user import User
from core.repositories.user_repository import UserRepository

DB_DIR = "src/core/shared/databases/patients.json"

class JSONPatientRepository(UserRepository):
    """
    Patient repository that uses a JSON file for storage.
    """
    def __init__(self):
        db_dir = os.path.dirname(DB_DIR)
        os.makedirs(db_dir, exist_ok=True)

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
    def add(self, full_name, email, dob, gender, active) -> Patient:
        data = self._load_data()

        new_patient = Patient(
            full_name,
            email,
            dob,
            gender,
            active
        )

        data.append(new_patient.__dict__)
        self._save_data(data)

        return new_patient

    """
    Return a patient by ID.
    """
    def get_by_id(self, patient_id: str) -> Optional[Patient]:
        data = self._load_data()
        for item in data:
            if item["id"] == patient_id and item.get("active", True):
                return Patient(**item)
        return None
    
    """
    Return a patient by email.
    """
    def get_by_email(self, email: str) -> Optional[Patient]:
        data = self._load_data()
        for item in data:
            if item["email"] == email and item.get("active", True):
                return User(**item)
        return None

    """
    List all active patients.
    """
    def list_all(self) -> List[Patient]:
        data = self._load_data()
        return [Patient(**item) for item in data if item.get("active", True)]

    """
    Update a patient by creating a new version (does not overwrite previous version).
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
                item["active"] = False
                self._save_data(data)
                return True
        return False
