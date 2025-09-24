from time import sleep

from rich.prompt import Prompt

from core.entities.user import User
from core.middlewares.authorize import authorize
from core.use_cases.factories.make_access_environmental_education_modules import (
    make_access_environmental_education_modules_use_case,
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

    if modules_with_progression:
        for idx, item in enumerate(modules_with_progression, start=1):
            console.io.print(f"[bold green]{idx}. {item.title}[/bold green]")
            console.io.print(f"   Description: {item.description}")
            console.io.print(f"   Progress: {item.progress}%\n")
    else:
        raise ValueError(console.io.print("[bold red]Failed to retrieve modules data.[/bold red]"))

    module_choice = int(Prompt.ask("\n[bold yellow]Select a module to access[/bold yellow]"))
    clear()

    if 1 <= module_choice <= len(modules_with_progression):
        module_id = modules_with_progression[module_choice - 1].id

        access_environmental_education_modules_use_case = make_access_environmental_education_modules_use_case()
        result = access_environmental_education_modules_use_case.execute(user.id, module_id)

        console.io.print(f"\n[bold green]{result["module"].title} - {result["module"].description} (your current progress {result["progress"].score}%) [/bold green]\n")

        console.io.print(f"[bold blue]You have accessed the module: {result["module"].title}[/bold blue]")

        console.io.print(result["module"].content)

        quiz_choice = Prompt.ask("\n[bold yellow]Press R to return to the module list or Q to quiz[/bold yellow]")

        clear()

        if quiz_choice.lower() == 'q':
            console.io.print("\n[bold cyan]--- Quiz ---[/bold cyan]\n")
            score = 0
            
            console.io.print(f"[bold green]Q: {result['module'].quiz["question"]}[/bold green]\n")

            for a_idx, answer in enumerate(result['module'].quiz["options"], start=1):
                console.io.print(f"   {a_idx}. {answer}")

            user_answer = int(Prompt.ask("\n[bold yellow]Your answer (number)[/bold yellow]"))

            clear()

            if result['module'].quiz["options"][user_answer - 1] == result['module'].quiz["answer"]:
                console.io.print("[bold green]Correct![/bold green]\n")
                score += 1
            else:
                console.io.print(f"[bold red]Wrong! The correct answer was: {result['module'].quiz['answer']}[/bold red]\n")

            total_questions = len(result["module"].quiz["options"])
            percentage_score = (score / total_questions) * 100
            console.io.print(f"[bold blue]You scored {score} out of {total_questions} ({percentage_score}%).[/bold blue]")

            update_education_progress_use_case = make_update_education_progression_use_case()
            updated_education_progress = update_education_progress_use_case.execute(user.id, module_id, score)

            if not updated_education_progress:
                console.io.print("[bold red]Failed to update your progress. Please try again later.[/bold red]")

            console.io.print("[bold green]Your progress has been updated![/bold green]")
        elif quiz_choice.lower() == 'r':
            return
    else:
        console.io.print("[bold red]Invalid choice. Please select a valid module number.[/bold red]")


    continue_prompt = console.io.input("\n[bold yellow]Press Enter to return to the main menu...[/bold yellow]")
    sleep(1)
    clear()

    if continue_prompt:
        return