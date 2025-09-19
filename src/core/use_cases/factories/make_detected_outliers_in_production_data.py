from core.repositories.json.json_production_data_repository import (
    JSONProductionDataRepository,
)
from core.use_cases.detected_outliers_in_production_data import (
    DetectedOutliersInProductionDataUseCase,
)


# Factory to create an instance of DetectedOutliersInProductionDataUseCase
def make_detected_outliers_in_production_data_use_case() -> DetectedOutliersInProductionDataUseCase:
    production_data_repository = JSONProductionDataRepository()

    use_case = DetectedOutliersInProductionDataUseCase(production_data_repository)

    return use_case