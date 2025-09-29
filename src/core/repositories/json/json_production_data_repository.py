import json
import os
from typing import List

from core.entities.production_data import ProductionData
from core.repositories.production_data_repository import ProductionDataRepository

DB_DIR = "src/core/shared/databases/production_data.json"

class JSONProductionDataRepository(ProductionDataRepository):
    """
    Production data repository that uses a JSON file for storage.
    """
    def __init__(self):
        db_dir = os.path.dirname(DB_DIR)
        os.makedirs(db_dir, exist_ok=True)

        file_path = os.path.join(db_dir, "production_data.json")

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
    Add a new production data entry.
    """
    def add(self, quantity: int, energy_consumption: int, recovered_solvent_volume: int, emissions: int, user_id: str, lote_id: str) -> ProductionData:
        data = self._load_data()

        new_production_data = ProductionData(
            quantity,
            energy_consumption,
            recovered_solvent_volume,
            emissions,
            user_id,
            lote_id
        )

        data.append(new_production_data.__dict__)
        self._save_data(data)

        return new_production_data
    
    """
    Return a production data entry by lote_id
    """
    def get_by_lote_id(self, lote_id):
        data = self._load_data()
        for item in data:
            if item["lote_id"] == lote_id:
                return ProductionData(**item)
        return None

    """
    List all active production data entries.
    """
    def list_all(self) -> List[ProductionData]:
        data = self._load_data()
        return [ProductionData(**item) for item in data if item.get("active", True)]

    """
    List by period.
    """
    def list_by_period(self, start_date, end_date) -> List[ProductionData]:
        data = self._load_data()
        return [
            ProductionData(**item) for item in data 
            if start_date <= item.get("timestamp", "") <= end_date and item.get("active", True)
        ]

    """
    Inactivate production data entries by lote_id (soft delete).
    """
    def inactivate_by_lote_id(self, lote_id: str) -> bool:
        data = self._load_data()
        found = False
        for item in data:
            if item["lote_id"] == lote_id and item.get("active", True):
                item["active"] = False
                found = True
        if found:
            self._save_data(data)
        return found