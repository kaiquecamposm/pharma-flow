from core.commands.apply_stratification_in_patients import (
    apply_stratification_in_patients_command,
)
from core.commands.detected_outliers_in_clinical_data import (
    detected_outliers_in_clinical_data_command,
)
from core.commands.detected_outliers_in_production_data import (
    detected_outliers_in_production_data_command,
)
from core.commands.generate_sprint_report import generate_sprint_report_command
from core.commands.get_profile import get_profile_command
from core.commands.register_clinical_data import register_clinical_data_command
from core.commands.register_lote import register_lote_command
from core.commands.register_patient import register_patient_command
from core.commands.register_user import register_user_command
from core.commands.update_clinical_data import update_clinical_data_command
from core.commands.view_all_audit_logs import view_all_audit_logs_command
from core.commands.view_all_clinical_data import view_all_clinical_data_command
from core.commands.view_all_lotes_and_indicators_command import (
    view_all_lotes_and_indicators_command,
)
from utils.show_menu import show_menu


def patients_menu(user):
    show_menu("Patients Menu", {
        "Register Patient": lambda: register_patient_command(user.id),
        "Back to Main Menu": None
    })


def users_menu(user):
    show_menu("Users Menu", {
        "View Profile": lambda: get_profile_command(user.id),
        "Register User": lambda: register_user_command(user.id),
        "Back to Main Menu": None
    })


def clinical_data_menu(user):
    show_menu("Clinical Data Menu", {
        "Register Clinical Data": lambda: register_clinical_data_command(user.id),
        "Update Clinical Data": lambda: update_clinical_data_command(user.id),
        "View Clinical Data": lambda: view_all_clinical_data_command(user.id),
        "Back to Main Menu": None
    })


def lotes_menu(user):
    show_menu("Lotes Menu", {
        "Register Lote": lambda: register_lote_command(user.id),
        "View Lotes and Indicators": lambda: view_all_lotes_and_indicators_command(user.id),
        "Back to Main Menu": None
    })


def analysis_menu(user):
    show_menu("Analysis Menu", {
        "Stratification in Patients": lambda: apply_stratification_in_patients_command(user.id),
        "Detected Outliers in Clinical Data": lambda: detected_outliers_in_clinical_data_command(user.id),
        "Detected Outliers in Production Data": lambda: detected_outliers_in_production_data_command(user.id),
        "Back to Main Menu": None
    })


def audit_menu(user):
    show_menu("Audit Menu", {
        "Audit Logs": view_all_audit_logs_command,
        "Sprint Report": lambda: generate_sprint_report_command(user.id),
        "Back to Main Menu": None
    })
