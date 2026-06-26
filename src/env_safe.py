"""Safe environment-variable usage examples."""

import os

# EXPECTED: safe / ignored — value is not hardcoded
RUNTIME_GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
RUNTIME_OPENAI_KEY = os.environ.get("OPENAI_API_KEY")
