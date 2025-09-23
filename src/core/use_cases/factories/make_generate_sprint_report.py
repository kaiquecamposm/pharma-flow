from core.repositories.json.json_clinical_data_repository import (
    JSONClinicalDataRepository,
)
from core.repositories.json.json_production_data_repository import (
    JSONProductionDataRepository,
)
from core.use_cases.generate_sprint_report import GenerateSprintReportUseCase


# Factory to create an instance of GenerateSprintReportUseCase
def make_generate_sprint_report_use_case() -> GenerateSprintReportUseCase:
    clinical_data_repository = JSONClinicalDataRepository()
    production_data_repository = JSONProductionDataRepository()

    use_case = GenerateSprintReportUseCase(
        clinical_data_repository=clinical_data_repository,
        production_data_repository=production_data_repository
    )

    return use_case