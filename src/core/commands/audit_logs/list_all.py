from time import sleep

from core.entities.user import User
from core.middlewares.authorize import authorize
from core.use_cases.factories.make_list_all_audit_logs import (
    make_list_all_audit_logs,
)
from utils import console
from utils.clear_terminal import clear


@authorize("audit")
def list_all_audit_logs_command(user: User):
    console.io.print("[bold cyan]--- List All Audit Logs ---[/bold cyan]\n")

    list_all_audit_logs_use_case = make_list_all_audit_logs()
    audit_logs = list_all_audit_logs_use_case.execute()

    if audit_logs:
        for idx, data in enumerate(audit_logs, start=1):
            if idx > 1:
                console.io.print("-" * 40)
            console.io.print(f"[bold]{idx}.[/bold] User ID: {data.user_id}")
            console.io.print(f"Action: {data.action}")
            console.io.print(f"Target ID: {data.target_id}")
            console.io.print(f"Target Type: {data.target_type}")
            console.io.print(f"Details: {data.details}")
            console.io.print(f"Date Recorded: {data.timestamp}")
    else:
        raise ValueError(console.io.print("\n[bold red]Failed to retrieve audit logs.[/bold red]"))

    complete_prompt = console.io.input("\n[bold yellow]Press Enter to return to the main menu...[/bold yellow]")
    sleep(1)
    clear()

    if complete_prompt:
        return