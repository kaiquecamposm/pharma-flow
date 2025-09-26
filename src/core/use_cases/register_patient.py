from dataclasses import dataclass

from core.entities.patient import Patient
from core.repositories.audit_log_repository import AuditLogRepository
from core.repositories.patient_repository import PatientRepository
from utils import console


@dataclass
class RegisterPatientUseCase:
    def __init__(self, patient_repository: PatientRepository, audit_log_repository: AuditLogRepository):
        self.patient_repository = patient_repository
        self.audit_log_repository = audit_log_repository

    def execute(self, user_id, full_name, email, dob, gender, active) -> Patient:
        """
        Register a new patient.
        Business rules:
        - Ensure the email is unique (not already registered).
        """
        try:
            is_exist_email = self.patient_repository.get_by_email(email)

            if is_exist_email:
                raise ValueError("\n[bold red]Email already registered.[/bold red]")
            
            saved_patient = self.patient_repository.add({
                "full_name": full_name,
                "email": email,
                "dob": dob,
                "gender": gender,
                "active": active,
            })

            if saved_patient is None:
                raise ValueError("\n[bold red]Failed to register patient.[/bold red]")

            self.audit_log_repository.add({
                "user_id": user_id,
                "action": "REGISTER_PATIENT",
                "target_id": saved_patient.id,
                "target_type": "Patient",
                "details": f"Registered patient with email: {email}",
            })

            return saved_patient
        except Exception as e:
            raise console.io.print(f"\n[bold red]Failed to register patient: {str(e)}[/bold red]")