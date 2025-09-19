import json
import os
from typing import List

from core.entities.audit_log import AuditLog
from core.repositories.audit_log_repository import AuditLogRepository

DB_DIR = "src/core/shared/databases/audit_log.json"

class JSONAuditLogRepository(AuditLogRepository):
    """
    Audit log repository that uses a JSON file for storage.
    """
    def __init__(self):
        db_dir = os.path.dirname(DB_DIR)
        os.makedirs(db_dir, exist_ok=True)

        file_path = os.path.join(db_dir, "audit_log.json")

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
    Add a new audit log entry.
    """
    def add(self, audit_log: AuditLog) -> AuditLog:
        data = self._load_data()
        data.append(audit_log.__dict__)
        self._save_data(data)
        return audit_log

    """
    List all active audit log entries.
    """
    def list_all(self) -> List[AuditLog]:
        data = self._load_data()
        return [AuditLog(**item) for item in data if item.get("active", True)]
