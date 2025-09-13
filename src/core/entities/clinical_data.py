from core.entities.base import BaseEntity


class ClinicalData(BaseEntity):
    patient_id: str
    data_type: str
    value: list