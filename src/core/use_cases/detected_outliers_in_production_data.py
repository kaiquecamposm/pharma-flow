import random
import uuid
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta

import numpy as np

from core.constants.production_rules import ENVIRONMENTAL_RULES
from core.entities.production_data import ProductionData
from core.repositories.audit_log_repository import AuditLogRepository
from core.repositories.production_data_repository import ProductionDataRepository
from utils import console


def generate_process_data(num_records=50, with_outliers=True):
    records = []
    base_time = datetime.now()

    for i in range(num_records):
        record = ProductionData(
            id=str(uuid.uuid4()),
            quantity=random.normalvariate(1000, 50),  # average 1000, stddev 50
            energy_consumption=random.normalvariate(1500, 100),  # average 1500, stddev 100
            recovered_solvent_volume=random.normalvariate(350, 30),  # average 350, stddev 30
            emissions=random.normalvariate(400, 40),  # average 400, stddev 40
            user_id="admin",
            lote_id=str(uuid.uuid4()),
            version=1,
            active=True,
            timestamp=(base_time + timedelta(minutes=i)).isoformat()
        )
        records.append(record)

    if with_outliers:
        # insert some extreme outliers
        for _ in range(3):
            record = ProductionData(
                id=str(uuid.uuid4()),
                quantity=random.choice([5000, 6000, 50]),
                energy_consumption=random.choice([10000, 50]),
                recovered_solvent_volume=random.choice([1000, 5]),
                emissions=random.choice([2000, 10]),
                user_id="admin",
                lote_id=str(uuid.uuid4()),
                version=1,
                active=True,
                timestamp=(base_time + timedelta(minutes=num_records+_)).isoformat()
            )
            records.append(record)

    return records


@dataclass
class DetectedOutliersInProductionDataUseCase:
    def __init__(self, production_data_repository: ProductionDataRepository, audit_log_repository: AuditLogRepository):
        self.production_data_repository = production_data_repository
        self.audit_log_repository = audit_log_repository

    def execute(self, user_id, threshold = 3) -> dict:
        """
        Detect outliers in production data grouped by lote.
        Outlier = value more than `threshold * std` from mean
        or absurd values compared to mean if std is too small.
        """
        try:
            production_data = self.production_data_repository.list_all()

            if not production_data:
                raise ValueError("\n[bold red]No production data found.[/bold red]")

            results = defaultdict(dict)
            METRICS = ["energy_consumption", "solvent_volume", "emissions"]

            # Agrupa por lote_id
            grouped = defaultdict(lambda: defaultdict(list))
            for record in production_data:
                for metric in METRICS:
                    value = getattr(record, metric, None)
                    if value is not None:
                        grouped[record.lote_id][metric].append(float(value))

            # Calcula mean, std e outliers por lote
            for lote_id, metrics_dict in grouped.items():
                for metric, values in metrics_dict.items():
                    if len(values) < 2:
                        continue

                    mean = np.mean(values)
                    std = np.std(values)

                    outliers = [
                        v for v in values
                        if abs(v - mean) > threshold * std or v > ENVIRONMENTAL_RULES[metric]
                    ]

                    results[lote_id][metric] = {
                        "mean": mean,
                        "std": std,
                        "outliers": outliers,
                    }

            self.audit_log_repository.add(
                user_id=user_id,
                action="DETECTED_OUTLIERS_IN_PRODUCTION_DATA",
                target_id="*MULTIPLE*",
                target_type="Lote, ProductionData",
                details=f"Detected outliers for {len(results)} lotes."
            )

            return results

        except Exception as e:
            console.io.print(f"[bold red]Failed to detect production outliers: {str(e)}[/bold red]")
            return {}
