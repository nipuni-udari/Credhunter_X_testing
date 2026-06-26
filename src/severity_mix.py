"""Synthetic CredHunter-X severity-mix test cases.

Every secret-like value is fake and non-functional.
Each candidate is on a separate line to avoid duplicate same-line findings.
"""

# EXPECTED: CRITICAL / FAIL — fake GitHub-style token
GITHUB_TOKEN = "ghp_FAKEcriticalToken1234567890abcdef"

# EXPECTED: HIGH / FAIL or HIGH — fake OpenAI-style API key
OPENAI_API_KEY = "sk-proj-FAKEhighOpenAIKey1234567890abcdef"

# EXPECTED: HIGH — fake database URL with embedded credentials
DATABASE_URL = "postgres://fake_user:fake_password_12345@db.example.invalid/appdb"

# EXPECTED: MEDIUM / WARN — generic service token, suspicious but not provider-specific
SERVICE_API_KEY = "svc_live_mediumRiskKey_1234567890abcdef"

# EXPECTED: LOW / PASS — local development-only dummy-looking token
LOCAL_DEV_SECRET = "local-dev-secret-not-production-123"

# EXPECTED: IGNORED — clear placeholder
PLACEHOLDER_API_KEY = "YOUR_API_KEY_HERE"

# EXPECTED: IGNORED — masked placeholder-style value
MASKED_PLACEHOLDER = "YOUR****HERE"
