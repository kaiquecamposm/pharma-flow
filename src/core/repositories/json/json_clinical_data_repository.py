import json
import os
from datetime import datetime, timezone
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
    def add(self, data_type: str, value: str, unit: str, description: str, user_id: str, patient_id: str) -> ClinicalData:
        new_clinical_data = ClinicalData(
            data_type=data_type,
            value=value,
            unit=unit,
            description=description,
            user_id=user_id,
            patient_id=patient_id,
        )
        data = self._load_data()
        data.append(new_clinical_data.__dict__)
        self._save_data(data)

        return new_clinical_data

    """
    Update a clinical data entry by creating a new version (does not overwrite previous version).
    """
    def update(self, id: str, user_id: str, data_type: str, value: str, unit: str, description: str) -> ClinicalData:
        data = self._load_data()
        
        for item in data:
            if item["id"] == id:
                # Inactivate old version
                item["active"] = False

                # Create new version
                clinical_data = ClinicalData(
                    data_type=data_type,
                    value=value,
                    unit=unit,
                    description=description,
                    user_id=user_id,
                    patient_id=item["patient_id"],
                    timestamp=datetime.now(timezone.utc).isoformat(),
                    version=item.get("version", 1) + 1,
                    active=True
                )
                data.append(clinical_data.__dict__)
                break

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
    def list_by_patient_id(self, patient_id: str) -> list[ClinicalData]:
        data = self._load_data()
        return [ClinicalData(**item) for item in data if item.get("patient_id") == patient_id]

    """
    List all active clinical data entries.
    """
    def list_all(self) -> List[ClinicalData]:
        data = self._load_data()
        return [ClinicalData(**item) for item in data if item.get("active", True)]

    """
    List by period.
    """
    def list_by_period(self, start_date: str, end_date: str) -> List[ClinicalData]:
        data = self._load_data()
        return [
            ClinicalData(**item) for item in data 
            if start_date <= item.get("timestamp", "") <= end_date and item.get("active", True)
        ]

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

    def inactivate_by_patient_id(self, patient_id):
        data = self._load_data()
        updated = False
        for item in data:
            if item.get("patient_id") == patient_id and item.get("active", True):
                item["active"] = False
                updated = True
        if updated:
            self._save_data(data)
        return updated