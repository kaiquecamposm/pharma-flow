from time import sleep

from core.entities.audit_log import AuditLog
from core.use_cases.factories.make_create_audit_log import (
    make_create_audit_log_use_case,
)
from core.use_cases.factories.make_get_profile import make_get_profile_use_case
from utils import console
from utils.clear_terminal import clear


def get_profile_command(user_id: str):
    console.io.print("[bold cyan]--- My Profile ---[/bold cyan]\n")

    get_profile_use_case = make_get_profile_use_case()
    profile = get_profile_use_case.execute(user_id)

    create_audit_log_use_case = make_create_audit_log_use_case()

    if profile:
        console.io.print(f"[bold green]ID:[/bold green] {profile.id}")
        console.io.print(f"[bold green]Full Name:[/bold green] {profile.full_name}")
        console.io.print(f"[bold green]Email:[/bold green] {profile.email.__len__() * '*'}")
        console.io.print(f"[bold green]Password:[/bold green] {profile.password.__len__() * '*'}")
        console.io.print(f"[bold green]Role:[/bold green] {profile.role_name}")
        console.io.print(f"[bold green]Active:[/bold green] {'Yes' if profile.active else 'No'}")

        create_audit_log_use_case.execute(AuditLog(
            user_id=user_id,
            action="VIEW_PROFILE",
            target_id=user_id,
            target_type="User",
            details=f"User {profile.full_name} viewed their profile."
        ))
    else:
        console.io.print("\n[bold red]Profile not found.[/bold red]")

    continue_prompt = console.io.input("\n[bold yellow]Press Enter to return to the main menu...[/bold yellow]")
    sleep(1)
    clear()

    if continue_prompt:
        return