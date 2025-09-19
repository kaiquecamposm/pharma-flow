import random
import uuid
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta

import numpy as np

from core.constants.production_data_limits import ABSOLUTE_LIMITS
from core.entities.production_data import ProductionData
from core.repositories.production_data_repository import ProductionDataRepository
from utils import console


def generate_process_data(num_records=50, with_outliers=True):
    records = []
    base_time = datetime.now()

    for i in range(num_records):
        record = ProductionData(
            id=str(uuid.uuid4()),
            quantity=random.normalvariate(1000, 50),  # média 1000, desvio 50
            energy_consumption=random.normalvariate(1500, 100),  # média 1500, desvio 100
            recovered_solvent_volume=random.normalvariate(350, 30),  # média 350, desvio 30
            emissions=random.normalvariate(400, 40),  # média 400, desvio 40
            user_id="admin",
            lote_id=str(uuid.uuid4()),
            version=1,
            active=True,
            timestamp=(base_time + timedelta(minutes=i)).isoformat()
        )
        records.append(record)

    if with_outliers:
        # inserir alguns outliers extremos
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
    def __init__(self, production_data_repository: ProductionDataRepository):
        self.production_data_repository = production_data_repository

    def execute(self, threshold: int = 3) -> dict:
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
            metrics = ["quantity", "energy_consumption", "recovered_solvent_volume", "emissions"]

            # Agrupa por lote_id
            grouped = defaultdict(lambda: defaultdict(list))
            for record in production_data:
                for metric in metrics:
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
                        if abs(v - mean) > threshold * std or v > ABSOLUTE_LIMITS[metric]
                    ]

                    results[lote_id][metric] = {
                        "mean": mean,
                        "std": std,
                        "outliers": outliers,
                    }

            return results

        except Exception as e:
            console.io.print(f"[bold red]Failed to detect production outliers: {str(e)}[/bold red]")
            return {}
