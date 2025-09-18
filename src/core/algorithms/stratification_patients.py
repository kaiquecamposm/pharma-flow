from core.entities.clinical_data import ClinicalData


def stratify(value, limits):
    """
    Stratify a clinical data value based on given limits.
    """
    if value >= limits[1]:
        return 1
    elif value >= limits[2]:
        return 2
    else:
        return 3


def stratify_algorithm(clinical_data: list[ClinicalData]) -> list:
    """
    Apply stratification algorithms to clinical data.
    
    | Tipo                  | Unidade     | Observações para estratificação                                              |
    | --------------------- | ----------- | ---------------------------------------------------------------------------- |
    | Blood Pressure        | mmHg        | Pressão sistólica/diastólica; risco se >140/90 mmHg                          |
    | Heart Rate            | bpm         | Taquicardia se >100 bpm; bradicardia se <60 bpm                              |
    | Temperature           | °C          | Febre se >38°C, hipotermia se <36°C                                          |
    | Respiratory Rate      | breaths/min | Anormal se <12 ou >20 respirations/min                                       |
    | Oxygen Saturation     | %           | Hipoxemia se <92%                                                            |
    | Blood Glucose         | mg/dL       | Diabetes se jejum ≥126 mg/dL                                                 |
    | Cholesterol Levels    | mg/dL       | LDL alto >130 mg/dL, Total >200 mg/dL                                        |
    | Body Mass Index (BMI) | kg/m²       | <18,5 (baixo peso), 18,5–24,9 (normal), 25–29,9 (sobrepeso), ≥30 (obesidade) |
    """
    stratified_data = []

    thresholds = {
        "Blood Pressure": {
            "systolic": {3: 0, 2: 120, 1: 140},
            "diastolic": {3: 0, 2: 80, 1: 90}
        },
        "Heart Rate": {3: 0, 2: 60, 1: 100},
        "Temperature": {3: 35, 2: 36.5, 1: 38},
        "Respiratory Rate": {3: 0, 2: 12, 1: 20},
        "Oxygen Saturation": {3: 0, 2: 92, 1: 100},
        "Blood Glucose": {3: 0, 2: 100, 1: 126},
        "Cholesterol Levels": {3: 0, 2: 130, 1: 200},
        "Body Mass Index (BMI)": {3: 0, 2: 18.5, 1: 25},
    }

    for data in clinical_data:
        if data.data_type in thresholds:
            limits = thresholds[data.data_type]
            
            if data.data_type == "Blood Pressure":
                systolic, diastolic = map(float, data.value.split('/'))
                priority_systolic = stratify(systolic, limits["systolic"])
                priority_diastolic = stratify(diastolic, limits["diastolic"])
                priority = max(priority_systolic, priority_diastolic)
            
                stratified_data.append({
                    "patient_id": data.patient_id,
                    "data_type": data.data_type,
                    "value": data.value,
                    "unit": data.unit,
                    "priority": priority
                })
            else:
                priority = stratify(float(data.value), limits)
                stratified_data.append({
                    "patient_id": data.patient_id,
                    "data_type": data.data_type,
                    "value": data.value,
                    "unit": data.unit,
                    "priority": priority
                })

    return stratified_data