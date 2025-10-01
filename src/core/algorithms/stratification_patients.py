from core.entities.clinical_data import ClinicalData


def stratify(value, limits):
    """
    Stratify a clinical data value based on given limits.

    Time Complexity Analysis:

    - Only 2 comparisons (if/elif) are performed
    - Does not depend on input size
    Total Complexity: O(1) (constant time)
    """
    if value >= limits[1]:
        return 1
    elif value >= limits[2]:
        return 2
    else:
        return 3

def process_bp(value, limits):
    systolic, diastolic = map(float, value.split('/'))
    return max(stratify(systolic, limits["systolic"]),
               stratify(diastolic, limits["diastolic"]))

def process_generic(value, limits):
    return stratify(float(value), limits)

processors = {
    "Blood Pressure": process_bp,
    "Heart Rate": process_generic,
    "Temperature": process_generic,
    "Respiratory Rate": process_generic,
    "Oxygen Saturation": process_generic,
    "Blood Glucose": process_generic,
    "Cholesterol Levels": process_generic,
    "Body Mass Index (BMI)": process_generic,
}

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


def stratify_algorithm(clinical_data: list[ClinicalData]) -> list:
    """
    Apply stratification algorithms to clinical data.

    Time Complexity Analysis:

    - Loop over clinical_data → O(n), n = number of clinical data entries
    - Lookup in thresholds dict → O(1)
    - stratify() call → O(1)
    - For Blood Pressure, split('/') and float conversion → O(1)
    
    Total Complexity: O(n) (linear)
    Best / Average / Worst Case: Linear in the number of clinical data entries
    """
    stratified_data = []

    for data in clinical_data:
        if data.data_type in thresholds:
            priority = processors[data.data_type](data.value, thresholds[data.data_type])
            stratified_data.append({
                "patient_id": data.patient_id,
                "data_type": data.data_type,
                "value": data.value,
                "unit": data.unit,
                "priority": priority
            })

    return stratified_data