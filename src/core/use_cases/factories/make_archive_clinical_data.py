from core.repositories.json.json_clinical_data_repository import (
    JSONClinicalDataRepository,
)
from core.use_cases.archive_clinical_data import ArchiveClinicalDataUseCase


# Factory to create an instance of ArchiveClinicalDataUseCase
def make_archive_clinical_data_use_case() -> ArchiveClinicalDataUseCase:
    clinical_data_repository = JSONClinicalDataRepository()

    use_case = ArchiveClinicalDataUseCase(clinical_data_repository=clinical_data_repository)

    return use_case