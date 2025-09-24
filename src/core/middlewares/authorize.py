from functools import wraps
from time import sleep

MODULE_ACCESS = {
    "users": ["Admin"],
    "patients": ["Admin", "Researcher"],
    "clinical_data": ["Admin", "Researcher"],
    "lotes": ["Admin", "Lab Technician"],
    "analysis": ["Admin", "Researcher", "Lab Technician"],
    "education": ["Admin", "Researcher", "Lab Technician", "Auditor"],
    "audit": ["Admin", "Auditor"]
}

def authorize(module_name: str):
    """
    Middleware to authorize user access based on their role for a specific module.
    Usage:
        @authorize("module_name")
        def some_function(user, ...):
            ...
    """
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            allowed_roles = MODULE_ACCESS.get(module_name, [])
            if user.role_name not in allowed_roles:
                from utils import console
                console.io.print(f"[bold red]Access denied:[/bold red] User role '{user.role_name}' cannot access {module_name}.")
                sleep(2)
                return None
            return func(user, *args, **kwargs)
        return wrapper
    return decorator
