import platform
import getpass

from rich.console import Console
from rich.panel import Panel

console = Console()

user = getpass.getuser()
system = platform.freedesktop_os_release().get("PRETTY_NAME", platform.system())
python_version = platform.python_version()

message = (
    f"[bold #cba6f7]Hello, {user}![/]\n\n"
    f"[#94e2d5]System:[/]  {system}\n"
    f"[#94e2d5]Python:[/]  {python_version}\n\n"
    "[#a6adc8]My first project on Linux.[/]"
)

console.print(Panel(message, title="hello-linux", border_style="#89b4fa",
expand=False))
