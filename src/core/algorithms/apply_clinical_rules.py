from core.constants.clinical_rules import CLINICAL_RULES


def apply_clinical_rules(data_type: str, value: float):
    rules = CLINICAL_RULES.get(data_type, {})
    
    if data_type == "Heart Rate":
        if value < rules["min"]:
            return "low"
        elif value > rules["max"]:
            return "high"
        else:
            return "normal"

    if data_type == "Temperature":
        if value < rules["min"]:
            return "low"   # hypothermia
        elif value > rules["max"]:
            return "high" # fever
        else:
            return "normal"

    if data_type == "Oxygen Saturation":
        return "high" if value < rules["min"] else "normal"
    
    if data_type == "Respiratory Rate":
        if value < rules["min"]:
            return "low"
        elif value > rules["max"]:
            return "high"
        else:
            return "normal"
        
    if data_type == "Blood Pressure":
        systolic, diastolic = map(int, str(value).split("/"))
        if systolic < rules["systolic_min"] or diastolic < rules["diastolic_min"]:
            return "low"
        elif systolic > rules["systolic_max"] or diastolic > rules["diastolic_max"]:
            return "high"
        else:
            return "normal"
    
    if data_type == "Blood Glucose":
        return "high" if value >= rules["fasting"] else "normal"
    
    if data_type == "Cholesterol Levels":
        ldl, total = map(int, str(value).split("/"))
        if ldl > rules["ldl_max"] or total > rules["total_max"]:
            return "high"
        else:
            return "normal"
        
    if data_type == "Body Mass Index (BMI)":
        if value < rules["underweight"]:
            return "low"
        elif value <= rules["normal_max"]:
            return "normal"
        elif value <= rules["overweight_max"]:
            return "high"
            

    return "normal"
