"""CLI entry point for code-lens — a local AI-powered developer assistant."""

import typer

from code_lens.ai_engine import analyze_text

app = typer.Typer(
    name="lens",
    help="🔍 code-lens — AI-powered local developer assistant. "
         "Parses code or terminal errors and sends them to Gemini for analysis.",
)


@app.command()
def analyze(
    prompt: str = typer.Argument(
        ...,
        help="The code snippet, error message, or question to send to Gemini for analysis.",
    ),
) -> None:
    """Send a prompt to the Gemini API and display the AI analysis."""
    typer.echo("\n🔍 Analyzing with Gemini...\n")
    result = analyze_text(prompt)
    typer.echo("─" * 60)
    typer.echo(result)
    typer.echo("─" * 60)
    typer.echo("\n✅ Analysis complete.\n")


@app.command()
def version() -> None:
    """Print the installed version of code-lens."""
    from code_lens import __version__

    typer.echo(f"code-lens v{__version__}")
