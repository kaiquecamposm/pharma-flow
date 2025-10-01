from collections import defaultdict
from dataclasses import dataclass
from typing import Dict

import numpy as np

from core.algorithms.apply_clinical_rules import apply_clinical_rules
from core.repositories.audit_log_repository import AuditLogRepository
from core.repositories.clinical_data_repository import ClinicalDataRepository
from core.repositories.patient_repository import PatientRepository


@dataclass
class DetectedOutliersInClinicalDataUseCase:
    def __init__(self, patient_repository: PatientRepository, clinical_data_repository: ClinicalDataRepository, audit_log_repository: AuditLogRepository):
        self.patient_repository = patient_repository
        self.clinical_data_repository = clinical_data_repository
        self.audit_log_repository = audit_log_repository
    
    
    def execute(self, user_id, threshold: int = 3) -> Dict:
        """
        Detect outliers in clinical data grouped by patient and data_type.

        Time Complexity Analysis:

        - Fetch all patients:
            - O(P), P = total number of patients

        - For each patient:
            - Fetch clinical data by patient_id:
                - O(C_i), C_i = number of clinical data entries for patient i
            - Group values by data_type:
                - O(C_i), iterates over all clinical data for the patient
            - Compute mean, std, and detect outliers:
                - O(C_i) for mean/std + O(C_i) for outlier detection → O(C_i) total
            - Apply clinical rules per value → O(C_i) 
            - Total per patient → O(C_i)
        
        - Summed over all patients:
            - O(sum(C_i) for i in 1..P) = O(N), N = total clinical data entries across all patients

        - Audit log insertion:
            - O(1)

        Total Complexity:
            - O(P + N) ≈ O(N), dominated by iterating over all clinical data entries
            (P is usually much smaller than N, so N dominates)

        Best / Average / Worst Case:
            - Linear in the total number of clinical data entries
            - Independent of data distribution per patient
        """
        try:
            patients = self.patient_repository.list_all()

            if not patients:
                raise ValueError("\n[bold red]No patients found.[/bold red]")

            results = defaultdict(dict)

            for patient in patients:
                clinical_data = self.clinical_data_repository.list_by_patient_id(patient.id)

                if not clinical_data:
                    continue  # no clinical data for this patient

                # group values by type
                grouped = defaultdict(list)

                for cld in clinical_data:
                    try:
                        value = int(str(cld["value"]).split("/")[0])  # ex: "135/90" → get 135
                        grouped[cld["data_type"]].append(value)
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

            self.audit_log_repository.add(
                user_id=user_id,
                action="DETECTED_OUTLIERS_IN_CLINICAL_DATA",
                target_id="*MULTIPLE*",
                target_type="Patient, ClinicalData",
                details=f"Detected outliers for {len(results)} patients."
            )

            return results
        except Exception as e:
            raise Exception(f"\nFailed to detect clinical outliers: {str(e)}")
