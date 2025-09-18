import json
import os
from typing import List, Optional

from core.entities.clinical_data import ClinicalData
from core.repositories.clinical_data_repository import ClinicalDataRepository

DB_DIR = "src/core/shared/databases/clinical_data.json"

class JSONClinicalDataRepository(ClinicalDataRepository):
    """
    Clinical data repository that uses a JSON file for storage.
    """
    def __init__(self):
        db_dir = os.path.dirname(DB_DIR)
        os.makedirs(db_dir, exist_ok=True)

        file_path = os.path.join(db_dir, "clinical_data.json")

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
    Add a new clinical data entry.
    """
    def add(self, clinical_data: ClinicalData) -> ClinicalData:
        data = self._load_data()
        data.append(clinical_data.__dict__)
        self._save_data(data)
        return clinical_data

    """
    Return a clinical data entry by ID.
    """
    def get_by_id(self, clinical_data_id: str) -> Optional[ClinicalData]:
        data = self._load_data()
        for item in data:
            if item["id"] == clinical_data_id:
                return ClinicalData(**item)
        return None
    
    """
    Return a list of clinical data entries by patient ID.
    """
    def get_by_patient_id(self, patient_id: str) -> list[ClinicalData]:
        data = self._load_data()
        return [ClinicalData(**item) for item in data if item.get("patient_id") == patient_id]

    """
    List all active clinical data entries.
    """
    def list_all(self) -> List[ClinicalData]:
        data = self._load_data()
        return [ClinicalData(**item) for item in data if item.get("active", True)]

    """
    Update a clinical data entry by creating a new version (does not overwrite previous version).
    """
    def update(self, clinical_data: ClinicalData) -> ClinicalData:
        data = self._load_data()
        for item in data:
            if item["id"] == clinical_data.id:
                clinical_data.version = item.get("version", 1) + 1
                item.update(clinical_data.__dict__)
                break
        self._save_data(data)
        return clinical_data

    """
    Inactivate a clinical data entry (soft delete).
    """
    def inactivate(self, clinical_data_id: str) -> bool:
        data = self._load_data()
        for item in data:
            if item["id"] == clinical_data_id:
                item["active"] = False
                self._save_data(data)
                return True
        return False
