import re

from utils import console


def execute(email: str) -> str:
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_regex, email):
        console.io.print("[bold red]Invalid email format.[/bold red]")
        return
    
    return email