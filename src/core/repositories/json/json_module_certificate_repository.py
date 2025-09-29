import json
import os
from typing import List

from core.entities.module_certificate import ModuleCertificate
from core.repositories.module_certificate_repository import ModuleCertificateRepository

DB_DIR = "src/core/shared/databases/module_certificate.json"

class JSONModuleCertificateRepository(ModuleCertificateRepository):
    """
    Module certificate repository that uses a JSON file for storage.
    """
    def __init__(self):
        db_dir = os.path.dirname(DB_DIR)
        os.makedirs(db_dir, exist_ok=True)

        file_path = os.path.join(db_dir, "module_certificate.json")

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
    Get an education module by its ID.
    """
    def add(self, user_id: str, module_id: str) -> ModuleCertificate:
        data = self._load_data()

        new_certificate = ModuleCertificate(
            user_id,
            module_id,
        )

        data.append(new_certificate.__dict__)
        self._save_data(data)

        return new_certificate

    """
    Get a certificate by user ID and module ID.
    """
    def get_by_user_and_module(self, user_id: str, module_id: str) -> ModuleCertificate:
        data = self._load_data()

        for item in data:
            if item["user_id"] == user_id and item["module_id"] == module_id:
                return ModuleCertificate(**item)
        return None

    """
    List all certificates for a given user.
    """
    def list_by_user(self, user_id: str) -> list[ModuleCertificate]:
        data = self._load_data()

        return [ModuleCertificate(**item) for item in data if item["user_id"] == user_id]