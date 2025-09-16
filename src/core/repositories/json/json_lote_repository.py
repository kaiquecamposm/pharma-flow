import json
import os
from typing import List, Optional

from core.entities.lote import Lote
from core.repositories.lote_repository import LoteRepository

DB_DIR = "src/core/shared/databases/lote.json"

class JSONLoteRepository(LoteRepository):
    """
    Lote repository that uses a JSON file for storage.
    """
    def __init__(self):
        db_dir = os.path.dirname(DB_DIR)
        os.makedirs(db_dir, exist_ok=True)

        file_path = os.path.join(db_dir, "lote.json")

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
    Add a new lote entry.
    """
    def add(self, lote: Lote) -> Lote:
        data = self._load_data()
        data.append(lote.__dict__)
        self._save_data(data)
        return lote

    """
    Return a lote entry by ID.
    """
    def get_by_id(self, lote_id: str) -> Optional[Lote]:
        data = self._load_data()
        for item in data:
            if item["id"] == lote_id:
                return Lote(**item)
        return None

    """
    List all active lote entries.
    """
    def list_all(self) -> List[Lote]:
        data = self._load_data()
        return [Lote(**item) for item in data if item.get("active", True)]

    """
    Update a lote entry by creating a new version (does not overwrite previous version).
    """
    def update(self, lote: Lote) -> Lote:
        data = self._load_data()
        for item in data:
            if item["id"] == lote.id:
                lote.version = item.get("version", 1) + 1
                item.update(lote.__dict__)
                break
        self._save_data(data)
        return lote

    """
    Inactivate a lote entry (soft delete).
    """
    def inactivate(self, lote_id: str) -> bool:
        data = self._load_data()
        for item in data:
            if item["id"] == lote_id:
                item["active"] = False
                self._save_data(data)
                return True
        return False
