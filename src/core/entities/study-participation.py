from dataclasses import dataclass


@dataclass
class StudyParticipant:
    study_id: str
    patient_id: str