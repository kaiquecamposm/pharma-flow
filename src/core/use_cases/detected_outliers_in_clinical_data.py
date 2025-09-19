from collections import defaultdict
from dataclasses import dataclass

import numpy as np

from core.algorithms.apply_clinical_rules import apply_clinical_rules
from core.repositories.clinical_data_repository import ClinicalDataRepository
from core.repositories.patient_repository import PatientRepository
from utils import console


@dataclass
class DetectedOutliersInClinicalDataUseCase:
    def __init__(self, patient_repository: PatientRepository, clinical_data_repository: ClinicalDataRepository):
        self.patient_repository = patient_repository
        self.clinical_data_repository = clinical_data_repository

    def execute(self, threshold: int = 3) -> dict:
        """
        Detect outliers in clinical data grouped by patient and data_type.
        An outlier is defined as a value that is more than `threshold` standard deviations away from the mean.
        """
        try:
            patients = self.patient_repository.list_all()
            if not patients:
                raise ValueError("\n[bold red]No patients found.[/bold red]")

            results = defaultdict(dict)

            for patient in patients:
                clinical_data = self.clinical_data_repository.get_by_patient_id(patient.id)

                # group values by type
                grouped = defaultdict(list)

                for cld in clinical_data:
                    try:
                        value = float(str(cld.value).split("/")[0])  # ex: "135/90" → get 135
                        grouped[cld.data_type].append(value)
                    except ValueError:
                        continue  # ignore non-numeric values

                # calculate mean, std and outliers
                for data_type, values in grouped.items():
                    if len(values) < 2:
                        continue  # need at least 2 values to calculate std
                    
                    mean = np.mean(values)
                    std = np.std(values)

                    outliers = [] 

                    for v in values:
                        status = apply_clinical_rules(data_type, v)
                        if status != "normal":
                            outliers.append(v)
                            continue

                        # Statistical outlier detection using Median Absolute Deviation (MAD)
                        if abs(v - mean) > threshold * std:
                            outliers.append(v)

                    results[patient.id][data_type] = {
                        "mean": mean,
                        "std": std,
                        "outliers": outliers,
                    }

            return results
        except Exception as e:
            console.io.print(f"[bold red]Failed to detect outliers: {str(e)}[/bold red]")
            return {}
