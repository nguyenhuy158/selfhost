import typer
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from typing import Optional

from . import __version__
from .providers.github import GitHubProvider

app = typer.Typer(help="CLI tool to list and manage your self-hosted tools.")
console = Console()

def version_callback(value: bool):
    if value:
        console.print(f"selfhost version: [bold cyan]{__version__}[/bold cyan]")
        raise typer.Exit()

@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        callback=version_callback,
        is_eager=True,
        help="Show the version and exit.",
    ),
):
    """
    SelfHost - List your useful tools shared on GitHub.
    """
    if ctx.invoked_subcommand is None:
        list_tools()

@app.command()
def list_tools():
    """List all available tools from GitHub."""
    provider = GitHubProvider()
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task("Fetching tools from GitHub...", total=None)
        result = provider.fetch_tools()

    if not result.success:
        console.print(f"[bold red]Error:[/bold red] {result.message}")
        raise typer.Exit(code=1)

    if not result.tools:
        console.print("[yellow]No tools found.[/yellow]")
        return

    table = Table(title="[bold blue]Available Tools[/bold blue]")
    table.add_column("Tool", style="cyan", no_wrap=True)
    table.add_column("Version", style="magenta")
    table.add_column("Description", style="green")
    table.add_column("Install & Run (uvx)", style="yellow")

    for tool in result.tools:
        table.add_row(tool.name, tool.version, tool.description, tool.install_cmd)

    console.print(table)
    console.print(f"\nFound [bold cyan]{len(result.tools)}[/bold cyan] tools.")

if __name__ == "__main__":
    app()
