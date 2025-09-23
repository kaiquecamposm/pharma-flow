from collections import defaultdict
from datetime import datetime

import numpy as np

from core.constants.production_rules import ENVIRONMENTAL_RULES
from core.entities.sprint_report import SprintReport
from core.repositories.clinical_data_repository import ClinicalDataRepository
from core.repositories.production_data_repository import ProductionDataRepository


class GenerateSprintReportUseCase:
    def __init__(self, clinical_data_repository: ClinicalDataRepository, production_data_repository: ProductionDataRepository):
        self.clinical_data_repository = clinical_data_repository
        self.production_data_repository = production_data_repository

    def _parse_value(self, data_type: str, value: str):
        """
        Converte valores de ClinicalData em números, se possível.
        Exemplo:
            Blood Pressure "120/80" -> {"systolic": 120, "diastolic": 80}
            Temperature "36.7" -> 36.7
        """
        try:
            if data_type == "Blood Pressure":
                systolic, diastolic = value.split("/")
                return {
                    "systolic": float(systolic),
                    "diastolic": float(diastolic)
                }
            elif data_type in ["Temperature", "Heart Rate", "Respiratory Rate",
                               "Oxygen Saturation", "Blood Glucose",
                               "Cholesterol Levels", "Body Mass Index (BMI)"]:
                return float(value)
        except Exception:
            return value

    def _generate_regulatory_indicators(self, grouped_clinical_data: dict) -> dict:
        regulatory_indicators = {}

        # Blood Pressure
        if "Blood Pressure" in grouped_clinical_data:
            systolic_values = [v["systolic"] for v in grouped_clinical_data["Blood Pressure"] if isinstance(v, dict)]
            diastolic_values = [v["diastolic"] for v in grouped_clinical_data["Blood Pressure"] if isinstance(v, dict)]
            if systolic_values and diastolic_values:
                mean_sys = np.mean(systolic_values)
                mean_dia = np.mean(diastolic_values)
                regulatory_indicators["Blood Pressure"] = {
                    "mean_systolic": mean_sys,
                    "mean_diastolic": mean_dia,
                    "status": "ALERT" if mean_sys > 140 or mean_dia > 90 else "OK"
                }

        # Heart Rate
        if "Heart Rate" in grouped_clinical_data:
            hr_values = [v for v in grouped_clinical_data["Heart Rate"] if isinstance(v, (int, float))]
            if hr_values:
                mean_hr = np.mean(hr_values)
                regulatory_indicators["Heart Rate"] = {
                    "mean": mean_hr,
                    "status": "ALERT" if mean_hr < 60 or mean_hr > 100 else "OK"
                }

        # Temperature
        if "Temperature" in grouped_clinical_data:
            temps = [v for v in grouped_clinical_data["Temperature"] if isinstance(v, (int, float))]
            if temps:
                mean_temp = np.mean(temps)
                regulatory_indicators["Temperature"] = {
                    "mean": mean_temp,
                    "status": "ALERT" if mean_temp < 36.0 or mean_temp > 38.0 else "OK"
                }

        # Respiratory Rate
        if "Respiratory Rate" in grouped_clinical_data:
            rr_values = [v for v in grouped_clinical_data["Respiratory Rate"] if isinstance(v, (int, float))]
            if rr_values:
                mean_rr = np.mean(rr_values)
                regulatory_indicators["Respiratory Rate"] = {
                    "mean": mean_rr,
                    "status": "ALERT" if mean_rr < 12 or mean_rr > 20 else "OK"
                }

        # Oxygen Saturation
        if "Oxygen Saturation" in grouped_clinical_data:
            ox_values = [v for v in grouped_clinical_data["Oxygen Saturation"] if isinstance(v, (int, float))]
            if ox_values:
                mean_ox = np.mean(ox_values)
                regulatory_indicators["Oxygen Saturation"] = {
                    "mean": mean_ox,
                    "status": "ALERT" if mean_ox < 92 else "OK"
                }

        # Blood Glucose
        if "Blood Glucose" in grouped_clinical_data:
            glucose_values = [v for v in grouped_clinical_data["Blood Glucose"] if isinstance(v, (int, float))]
            if glucose_values:
                mean_glucose = np.mean(glucose_values)
                regulatory_indicators["Blood Glucose"] = {
                    "mean": mean_glucose,
                    "status": "ALERT" if mean_glucose > 126 else "OK"
                }

        # Cholesterol Levels
        if "Cholesterol Levels" in grouped_clinical_data:
            ldl_values = [v.get("ldl") for v in grouped_clinical_data["Cholesterol Levels"] if isinstance(v, dict) and "ldl" in v]
            total_values = [v.get("total") for v in grouped_clinical_data["Cholesterol Levels"] if isinstance(v, dict) and "total" in v]
            entry = {}
            if ldl_values:
                mean_ldl = np.mean(ldl_values)
                entry["mean_ldl"] = mean_ldl
                entry["ldl_status"] = "ALERT" if mean_ldl > 130 else "OK"
            if total_values:
                mean_total = np.mean(total_values)
                entry["mean_total"] = mean_total
                entry["total_status"] = "ALERT" if mean_total > 200 else "OK"
            if entry:
                regulatory_indicators["Cholesterol Levels"] = entry

        # Body Mass Index (BMI)
        if "Body Mass Index (BMI)" in grouped_clinical_data:
            bmi_values = [v for v in grouped_clinical_data["Body Mass Index (BMI)"] if isinstance(v, (int, float))]
            if bmi_values:
                mean_bmi = np.mean(bmi_values)
                if mean_bmi < 18.5:
                    status = "UNDERWEIGHT"
                elif mean_bmi <= 24.9:
                    status = "NORMAL"
                elif mean_bmi <= 29.9:
                    status = "OVERWEIGHT"
                else:
                    status = "OBESE"
                regulatory_indicators["Body Mass Index (BMI)"] = {
                    "mean": mean_bmi,
                    "status": status
                }

        return regulatory_indicators

    def _generate_environmental_indicators(self, production_data: list) -> dict:
        # --- Environmental Indicators ---
        environmental_indicators = {}

        if production_data:
            total_energy = sum([p.energy_consumption for p in production_data if p.energy_consumption is not None])
            solvent_recovery = np.mean([p.recovered_solvent_volume for p in production_data if p.recovered_solvent_volume is not None])
            emissions = [p.emissions for p in production_data if p.emissions is not None]

            # Energy consumption
            energy_status = "ALERT" if total_energy > ENVIRONMENTAL_RULES["energy_consumption"]["max_total"] else "OK"
            environmental_indicators["energy_consumption"] = {
                "total": total_energy,
                "status": energy_status
            }

            # Solvent recovery
            solvent_status = "ALERT" if solvent_recovery < ENVIRONMENTAL_RULES["solvent_recovery"]["min_efficiency"] else "OK"
            environmental_indicators["solvent_recovery"] = {
                "mean": solvent_recovery,
                "status": solvent_status
            }

            # Emissions
            if emissions:
                mean_emissions = float(np.mean(emissions))
                max_emissions = float(np.max(emissions))
                min_emissions = float(np.min(emissions))

                if mean_emissions > ENVIRONMENTAL_RULES["emissions"]["max_mean"] or max_emissions > ENVIRONMENTAL_RULES["emissions"]["max_peak"]:
                    emissions_status = "ALERT"
                else:
                    emissions_status = "OK"

                environmental_indicators["emissions"] = {
                    "mean": mean_emissions,
                    "max": max_emissions,
                    "min": min_emissions,
                    "status": emissions_status
                }
        
        return environmental_indicators

    def execute(self, user_id: str, start_date: datetime, end_date: datetime) -> SprintReport:
        """
        Generate a sprint report for the given period.
        """
        # Fetch data for the period
        clinical_data = self.clinical_data_repository.list_by_period(start_date, end_date)
        production_data = self.production_data_repository.list_by_period(start_date, end_date)

        # --- Regulatory Indicators ---
        regulatory_indicators = defaultdict(dict)

        grouped_clinical_data = defaultdict(list)
        for record in clinical_data:
            parsed_value = self._parse_value(record.data_type, record.value)
            grouped_clinical_data[record.data_type].append(parsed_value)

        regulatory_indicators = self._generate_regulatory_indicators(grouped_clinical_data)

        # --- Environmental Indicators ---
        environmental_indicators = self._generate_environmental_indicators(production_data)

        # Create SprintReport entity
        report = SprintReport(
            start_date=start_date,
            end_date=end_date,
            generated_by=user_id,
            generated_at=datetime.now(),
            regulatory_indicators=regulatory_indicators,
            environmental_indicators=environmental_indicators
        )

        return report
