from core.commands.audit_logs.view_all import view_all_audit_logs_command
from core.commands.clinical_data.detected_outliers import (
    detected_outliers_in_clinical_data_command,
)
from core.commands.clinical_data.register import register_clinical_data_command
from core.commands.clinical_data.update import update_clinical_data_command
from core.commands.clinical_data.view_all import view_all_clinical_data_command
from core.commands.lotes.register import register_lote_command
from core.commands.lotes.view_all_lotes_and_indicators import (
    view_all_lotes_and_indicators_command,
)
from core.commands.patients.apply_stratification import (
    apply_stratification_in_patients_command,
)
from core.commands.patients.archive import archive_patient_command
from core.commands.patients.register import register_patient_command
from core.commands.production_data.detected_outliers import (
    detected_outliers_in_production_data_command,
)
from core.commands.sprint_report.generate import generate_sprint_report_command
from core.commands.users.get_profile import get_profile_command
from core.commands.users.register import register_user_command
from utils.show_menu import show_menu


def patients_menu(user):
    show_menu("Patients Menu", {
        "Register Patient": lambda: register_patient_command(user.id),
        "Archive Patient": lambda: archive_patient_command(user.id),
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
