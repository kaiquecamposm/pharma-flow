from collections import defaultdict
from dataclasses import dataclass

import numpy as np

from core.constants.production_rules import ENVIRONMENTAL_RULES
from core.repositories.audit_log_repository import AuditLogRepository
from core.repositories.production_data_repository import ProductionDataRepository
from utils import console


@dataclass
class DetectedOutliersInProductionDataUseCase:
    def __init__(self, production_data_repository: ProductionDataRepository, audit_log_repository: AuditLogRepository):
        self.production_data_repository = production_data_repository
        self.audit_log_repository = audit_log_repository

    
    def execute(self, user_id, threshold = 3) -> dict:
        """
        Detect outliers in production data grouped by lote.

        Time Complexity Analysis:

        - Fetch all production data:
            - O(p), p = total production records

        - Group data by lote and metric:
            - Iterates over all production records and metrics → O(p * m), m = number of metrics (constant here, m=3)
            - Effectively O(p) since m is small and fixed

        - Compute mean, std, and detect outliers for each lote and metric:
            - Let L = number of lotes, V = max number of values per metric per lote
            - For each lote and metric:
                - Mean/std calculation → O(V)
                - Outlier detection → O(V)
            - Total → O(L * V) ≈ O(p) because all production records are distributed across lotes

        - Audit log insertion:
            - O(1)

        Total Complexity:
        - O(p), linear in the number of production data entries

        Best / Average / Worst Case:
        - Linear scan over production data; complexity dominated by grouping and outlier detection
        """
        try:
            production_data = self.production_data_repository.list_all()

            if not production_data:
                console.io.print("\n[bold red]No production data found.[/bold red]")
                return

            results = defaultdict(dict)
            METRICS = ["energy_consumption", "solvent_volume", "emissions"]

            # Group data by lote and metric
            grouped = defaultdict(lambda: defaultdict(list))
            for record in production_data:
                for metric in METRICS:
                    value = getattr(record, metric, None)
                    if value is not None:
                        grouped[record.lote_id][metric].append(float(value))

            # Calculed mean, std and detect outliers
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
            raise Exception(f"\nFailed to detect production outliers: {str(e)}")
