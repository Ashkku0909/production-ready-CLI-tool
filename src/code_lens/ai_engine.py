"""AI Engine module for code-lens — handles Gemini API interactions."""

import os
import sys

from dotenv import load_dotenv
from google import genai


def _get_client() -> genai.Client:
    """Initialize and return a Gemini client using the API key from the environment.

    Returns:
        genai.Client: A configured Gemini client instance.

    Raises:
        SystemExit: If the GEMINI_API_KEY environment variable is not set.
    """
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print(
            "❌ Error: GEMINI_API_KEY not found.\n"
            "   Please create a `.env` file based on `.env.example` and add your API key.",
            file=sys.stderr,
        )
        sys.exit(1)

    return genai.Client(api_key=api_key)


def analyze_text(prompt: str, model: str = "gemini-2.0-flash") -> str:
    """Send a prompt to the Gemini API and return the model's response.

    Args:
        prompt: The text prompt to send to Gemini for analysis.
        model: The Gemini model name to use. Defaults to 'gemini-2.0-flash'.

    Returns:
        str: The text response from the Gemini model.

    Raises:
        SystemExit: If the API call fails.
    """
    client = _get_client()

    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt,
        )
        return response.text

    except Exception as exc:
        print(f"❌ Error: API call failed — {exc}", file=sys.stderr)
        sys.exit(1)
