import json
import os
from typing import Dict, List, Optional

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
                json.dump({}, f)

    """
    Load data from the JSON file.
    """
    def _load_data(self) -> Dict[str, List[dict]]:
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}
        
    """
    Save data to the JSON file.
    """
    def _save_data(self, data: Dict[str, List[dict]]) -> None:
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4, default=str)

    """
    Add a new clinical data entry.
    """
    def add(self, data_type: str, value: str, unit: str, description: str, user_id: str, patient_id: str) -> ClinicalData:
        new_clinical_data = ClinicalData(
            data_type,
            value,
            unit,
            description,
            user_id,
            patient_id
        )

        data = self._load_data()

        if patient_id not in data:
            data[patient_id] = []

        data[patient_id].append(new_clinical_data.__dict__)
        self._save_data(data)

        return new_clinical_data

    """
    Update a clinical data entry by creating a new version (does not overwrite previous version).
    """
    def update(self, id: str, user_id: str, data_type: str, value: str, unit: str, description: str) -> ClinicalData:
        data = self._load_data()
        
        for item in data:
            if item["id"] == id:
                item["active"] = False

                clinical_data = ClinicalData(
                    data_type, 
                    value, 
                    unit, 
                    description, 
                    user_id, 
                    item["patient_id"], 
                    item.get("version", 1) + 1
                )

                data.append(clinical_data.__dict__)
                break

        self._save_data(data)
        
        return clinical_data

    """
    Return a clinical data entry by ID.
    """
    def get_by_id(self, clinical_data_id: str) -> Optional[ClinicalData]:
        data = self._load_data()

        for records in data.values():
            for record in records:
                if record["id"] == clinical_data_id:
                    return ClinicalData(**record)
                    
        return None
    
    """
    Return a list of clinical data entries by patient ID.
    """
    def list_by_patient_id(self, patient_id: str) -> List[ClinicalData]:
        data = self._load_data()
        
        result = data.get(patient_id, [])

        return [item for item in result if item.get("active", True)]

    """
    List all active clinical data entries.
    """
    def list_all(self) -> List[ClinicalData]:
        data = self._load_data()
        
        result = []

        for entries in data.values():
            for entry in entries:
                if entry.get("active", True):
                    result.append(entry)
        return result

    """
    List by period.
    """
    def list_by_period(self, start_date: str, end_date: str) -> List[ClinicalData]:
        data = self._load_data()

        result = []

        for entries in data.values():
            for item in entries:
                timestamp = item.get("timestamp", "")
                if item.get("active", True) and start_date <= timestamp <= end_date:
                    result.append(item)
        return result

    """
    Inactivate a clinical data entry (soft delete).
    """
    def inactivate(self, clinical_data_id: str) -> bool:
        data = self._load_data()

        for records in data.values():
            for record in records:
                if record["id"] == clinical_data_id:
                    record["active"] = False

                    self._save_data(data)

                    return True
        return False

    def inactivate_by_patient_id(self, patient_id) -> bool:
        data = self._load_data()

        for patient_id_record, records in data.items():
            if patient_id_record == patient_id:
                for record in records:
                    if record.get("active", True):
                        record["active"] = False

        self._save_data(data)

        return True