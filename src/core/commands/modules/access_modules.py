from time import sleep

from rich.prompt import Prompt

from core.entities.user import User
from core.middlewares.authorize import authorize
from core.use_cases.factories.make_access_environmental_education_modules import (
    make_access_environmental_education_modules_use_case,
)
from core.use_cases.factories.make_generate_module_certificate import (
    make_generate_module_certificate_use_case,
)
from core.use_cases.factories.make_list_all_environmental_education_modules_and_progress import (
    make_list_all_environmental_education_modules_and_progress_use_case,
)
from core.use_cases.factories.make_update_education_progress import (
    make_update_education_progression_use_case,
)
from utils import console
from utils.clear_terminal import clear


@authorize("education")
def access_modules_command(user: User):
    console.io.print("[bold cyan]--- Access Modules ---[/bold cyan]\n")

    list_all_environmental_education_modules_and_progress_use_case = make_list_all_environmental_education_modules_and_progress_use_case()
    modules_with_progression = list_all_environmental_education_modules_and_progress_use_case.execute(user.id)

    if not modules_with_progression:
        console.io.print("[bold yellow]No modules available at the moment. Please check back later.[/bold yellow]")
        sleep(1)
        clear()
        return

    for idx, item in enumerate(modules_with_progression, start=1):
        console.io.print(f"[bold green]{idx}. {item.title}[/bold green]")
        console.io.print(f"   Description: {item.description}")
        console.io.print(f"   Progress: {item.progress}%\n")

    module_choice = int(Prompt.ask("\n[bold yellow]Select a module to access[/bold yellow]"))
    clear()

    if not 1 <= module_choice <= len(modules_with_progression):
        console.io.print("[bold red]Invalid choice. Please select a valid module number.[/bold red]")
        sleep(1)
        clear()
        return

    module_id = modules_with_progression[module_choice - 1].id

    access_environmental_education_modules_use_case = make_access_environmental_education_modules_use_case()
    result = access_environmental_education_modules_use_case.execute(user.id, module_id)

    console.io.print(f"\n[bold green]{result["module"].title} - {result["module"].description} (your current progress {result["progress"].score * 100}%) [/bold green]\n")

    console.io.print(f"[bold blue]You have accessed the module: {result["module"].title}[/bold blue]")

    console.io.print(result["module"].content)

    quiz_choice = Prompt.ask("\n[bold yellow]Press R to return to the module list or Q to quiz[/bold yellow]")

    clear()

    if quiz_choice.lower() == 'q':
        console.io.print("\n[bold cyan]--- Quiz ---[/bold cyan]\n")
        
        console.io.print(f"[bold green]Q: {result['module'].quiz["question"]}[/bold green]\n")

        for a_idx, answer in enumerate(result['module'].quiz["options"], start=1):
            console.io.print(f"   {a_idx}. {answer}")

        user_answer = int(Prompt.ask("\n[bold yellow]Your answer (number)[/bold yellow]"))

        clear()

        score = 0

        if not result['module'].quiz["options"][user_answer - 1] == result['module'].quiz["answer"]:
            console.io.print(f"\n[bold red]Incorrect! The correct answer was: {result['module'].quiz['answer']}[/bold red]\n")
            sleep(1)
            return

        console.io.print("[bold green]Correct![/bold green]")
        
        score = 1
        total_completed = 0

        for module in modules_with_progression:
            if module.progress > 0 and score == 1:
                total_completed += 1

        percentage_score = total_completed * 100 // modules_with_progression.__len__()
        console.io.print(f"[bold blue]\nYou scored {total_completed} out of {modules_with_progression.__len__()} ({percentage_score}%).[/bold blue]\n")

        update_education_progress_use_case = make_update_education_progression_use_case()
        updated_education_progress = update_education_progress_use_case.execute(user.id, module_id, score)

        if not updated_education_progress:
            console.io.print("[bold red]Failed to update your progress. Please try again later.[/bold red]")
            return

        generate_module_certificate_use_case = make_generate_module_certificate_use_case()
        generate_module_certificate = generate_module_certificate_use_case.execute(user.id, module_id)

        if generate_module_certificate:
            console.io.print(f"[bold green]Congratulations! You've completed the module and earned a certificate: {generate_module_certificate.id}[/bold green]")

        console.io.print("[bold green]Your progress has been updated![/bold green]")
    elif quiz_choice.lower() == 'r':
        return

    continue_prompt = console.io.input("\n[bold yellow]Press Enter to return to the main menu...[/bold yellow]")
    sleep(1)
    clear()

    if continue_prompt:
        return