from dataclasses import dataclass
from typing import Optional

from core.entities.clinical_data import ClinicalData
from core.repositories.clinical_data_repository import ClinicalDataRepository
from core.repositories.patient_repository import PatientRepository
from utils import console


@dataclass
class UpdateClinicalDataUseCase:
    def __init__(self, patient_repository: PatientRepository, clinical_data_repository: ClinicalDataRepository):
        self.patient_repository = patient_repository
        self.clinical_data_repository = clinical_data_repository

    def execute(self, patient_id, id, user_id, data_type, value, unit, description) -> Optional[ClinicalData]:
        try:
            patient = self.patient_repository.get_by_id(patient_id)

            if patient:
                updated_clinical_data = self.clinical_data_repository.update(
                    id=id,
                    user_id=user_id,
                    data_type=data_type,
                    value=value,
                    unit=unit,
                    description=description
                )

                return updated_clinical_data
            return None

        except Exception as e:
            raise console.io.print_exception(f"Failed to update clinical data: {str(e)}")