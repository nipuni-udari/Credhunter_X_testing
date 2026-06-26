# CredHunter-X Quick Severity Mix Test Project

This is a **small synthetic Python project** for fast CredHunter-X testing.
All secret-looking values are fake and non-functional.

It is designed to test:

- critical finding
- high finding
- medium warning
- low/pass finding
- ignored placeholders
- safe environment-variable references
- one candidate per line, avoiding multiple secrets on the same line

## Main file

```text
src/severity_mix.py
```

## Expected behaviour

Exact counts can vary slightly depending on LLM ranking and your CredHunter-X rules, but the intended result is:

| Category | Expected |
|---|---:|
| Blocking / critical | at least 1 |
| High | at least 1 |
| Medium / warning | at least 1 |
| Low / pass | at least 1 |
| Ignored placeholders | at least 2 |

The important check is not a fixed total count. The important check is that:

```text
GitHub/OpenAI/database-style keys are reportable,
medium key is warned,
local-dev key is low/pass,
placeholders are ignored,
os.getenv() values are ignored.
```

## GitHub Actions

The workflow is:

```text
.github/workflows/credhunter-severity-mix.yml
```

It runs CredHunter-X, uploads reports even if blocking secrets are found, and then fails the job at the end if the scan produced a blocking result.

Add this secret to the test repository:

```text
OPENAI_API_KEY
```

If your action repository is different, edit this line:

```yaml
uses: nipuni-udari/CredHunter-X@main
```

## Reports

The workflow uploads:

```text
credhunter-report.json
credhunter-report.sarif
credhunter-report.md
credhunter-report.html
```
