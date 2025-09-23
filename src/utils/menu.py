from core.commands.audit_logs.list_all import (
    list_all_audit_logs_command,
)
from core.commands.clinical_data.archive import archive_clinical_data_command
from core.commands.clinical_data.detected_outliers import (
    detected_outliers_in_clinical_data_command,
)
from core.commands.clinical_data.list_all import (
    list_all_clinical_data_command,
)
from core.commands.clinical_data.register import register_clinical_data_command
from core.commands.clinical_data.update import update_clinical_data_command
from core.commands.lotes.archive import archive_lote_command
from core.commands.lotes.list_all_lotes_and_indicators import (
    list_all_lotes_and_indicators_command,
)
from core.commands.lotes.register import register_lote_command
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
        "Archive Clinical Data": lambda: archive_clinical_data_command(user.id),
        "Update Clinical Data": lambda: update_clinical_data_command(user.id),
        "List All Clinical Data": lambda: list_all_clinical_data_command(user.id),
        "Back to Main Menu": None
    })


def lotes_menu(user):
    show_menu("Lotes Menu", {
        "Register Lote": lambda: register_lote_command(user.id),
        "Archive Lote": lambda: archive_lote_command(user.id),
        "List All Lotes and Indicators": lambda: list_all_lotes_and_indicators_command(user.id),
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
        "Audit Logs": list_all_audit_logs_command,
        "Sprint Report": lambda: generate_sprint_report_command(user.id),
        "Back to Main Menu": None
    })
