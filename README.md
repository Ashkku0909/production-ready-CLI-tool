# 🔍 code-lens

A local CLI developer assistant that parses code snippets or terminal errors and
sends them to the **Gemini API** for analysis and suggested fixes.

## Features

- **`lens analyze "<prompt>"`** — Send any code, error, or question to Gemini for
  instant AI-powered analysis, right from your terminal.
- **Secure API key management** via `.env` file.
- Built with `typer`, `google-genai`, and modern Python packaging (PEP 621).

## Prerequisites

- Python **3.10** or higher
- A valid [Gemini API key](https://aistudio.google.com/apikey)

## Setup

### 1. Clone & navigate

```bash
cd code-lens
```

### 2. Configure your API key

```bash
cp .env.example .env
```

Then edit `.env` and replace `your_api_key_here` with your actual Gemini API key:

```
GEMINI_API_KEY=AIzaSy...
```

### 3. Install in editable mode

```bash
pip install -e .
```

## Usage

```bash
# Analyze a code error
lens analyze "TypeError: 'NoneType' object is not subscriptable in my Flask app"

# Ask a coding question
lens analyze "How do I handle async database sessions in SQLAlchemy 2.0?"

# Check the installed version
lens version
```

## License

MIT
