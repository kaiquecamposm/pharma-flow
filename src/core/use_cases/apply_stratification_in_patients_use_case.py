from dataclasses import dataclass

from core.algorithms.stratification_patients import stratify_algorithm
from core.repositories.clinical_data_repository import ClinicalDataRepository
from core.repositories.patient_repository import PatientRepository
from utils import console


@dataclass
class ApplyStratificationInPatientsUseCase:
    def __init__(self, patient_repository: PatientRepository, clinical_data_repository: ClinicalDataRepository):
        self.patient_repository = patient_repository
        self.clinical_data_repository = clinical_data_repository

    def execute(self) -> list:
        """
        Apply stratification algorithms to patients.
        """
        try:
            results = []

            patients = self.patient_repository.list_all()

            if patients is None:
                raise ValueError("\n[bold red]No patients found.[/bold red]")

            for patient in patients:
                clinical_data = self.clinical_data_repository.get_by_patient_id(patient.id)
                
                if clinical_data:
                    stratifications = stratify_algorithm(clinical_data)
                    
                    for stratification in stratifications:
                        stratification_result = {}
                        
                        stratification_result = {
                            "patient_id": stratification["patient_id"],
                            "clinical_data": {
                                "data_type": stratification["data_type"],
                                "value": stratification["value"],
                                "unit": stratification["unit"],
                            },
                            "priority": stratification["priority"],  
                        }

                        results.append(stratification_result)
                else:
                    console.io.print(f"[bold yellow]No clinical data found for patient ID {patient.id}.[/bold yellow]")

            results_sorted = sorted(results, key=lambda x: x['priority'])

            return results_sorted
        except Exception as e:
            raise console.io.print(f"[bold red]Failed to get user profile: {str(e)}[/bold red]")