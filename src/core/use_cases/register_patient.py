from dataclasses import dataclass

from core.entities.patient import Patient
from core.repositories.audit_log_repository import AuditLogRepository
from core.repositories.patient_repository import PatientRepository


@dataclass
class RegisterPatientUseCase:
    def __init__(self, patient_repository: PatientRepository, audit_log_repository: AuditLogRepository):
        self.patient_repository = patient_repository
        self.audit_log_repository = audit_log_repository

    def execute(self, user_id, full_name, email, dob, gender, active) -> Patient:
        """
        Registers a new patient in the system.

        Time Complexity Analysis:

        - get_by_email(email) → O(n), n = total number of patients (linear search in list)
        - add patient → O(1) (append to list)
        - audit log insertion → O(1)

        Total Complexity: O(n)
        Best / Average / Worst Case: Linear in the number of patients
        """
        try:
            is_exist_email = self.patient_repository.get_by_email(email)

            if is_exist_email:
                raise ValueError("\n[bold red]Email already registered.[/bold red]")
            
            saved_patient = self.patient_repository.add(
                full_name=full_name,
                email=email,
                dob=dob,
                gender=gender,
                active=active,
            )

            if saved_patient is None:
                raise ValueError("\n[bold red]Failed to register patient.[/bold red]")

            self.audit_log_repository.add(
                user_id=user_id,
                action="REGISTER_PATIENT",
                target_id=saved_patient.id,
                target_type="Patient",
                details=f"Registered patient with email: {email}",
            )

            return saved_patient
        except Exception as e:
            raise Exception(f"\nFailed to register patient: {str(e)}")