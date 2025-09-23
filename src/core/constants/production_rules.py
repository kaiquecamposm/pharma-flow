ENVIRONMENTAL_RULES = {
    "energy_consumption": {
        "max_total": 1_000_000  # fictitious limit in kWh for the period
    },
    "solvent_recovery": {
        "min_efficiency": 300.0  # acceptable minimum average recovery value
    },
    "emissions": {
        "max_mean": 500.0,   # average limit for emissions
        "max_peak": 1000.0   # peak limit for emissions
    }
}
