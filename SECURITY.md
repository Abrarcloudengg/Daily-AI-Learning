# Security Policy

## Supported versions

| Version | Supported |
| ------- | --------- |
| 2.x     | ✅ Yes    |
| 1.x     | ❌ No     |

## Reporting a vulnerability

**Please do not open a public issue for a security problem.**

Use GitHub's private reporting instead:

1. Go to the [Security tab](https://github.com/Abrarcloudengg/Daily-AI-Learning/security/advisories).
2. Click **Report a vulnerability**.
3. Describe the issue, the impact, and how to reproduce it.

You should get an acknowledgement within **7 days** and a fix or a decision
within **30 days**. Once a fix ships you will be credited in the release notes,
unless you would rather stay anonymous.

## In scope

- Command injection or arbitrary file writes through topic names, subject
  names, or configuration values.
- Leaking `OPENROUTER_API_KEY` into logs, generated lessons, the README, or
  commit history.
- Privilege escalation through the GitHub Actions workflows — for example a
  `pull_request_target` misconfiguration that exposes repository secrets to a
  fork.
- Path traversal out of `generated/` when writing a lesson.

## Out of scope

- The content of AI-generated lessons. A model can be wrong; that is a quality
  issue, not a vulnerability. Open a normal issue.
- Rate limits, quota exhaustion, or billing on your own OpenRouter account.
- Vulnerabilities in OpenRouter or in the upstream models — report those to the
  relevant vendor.

## If you leak your own key

It happens. Rotate it immediately:

1. Revoke the key at <https://openrouter.ai/keys>.
2. Create a new one.
3. Update your local `.env` **and** the `OPENROUTER_API_KEY` repository secret
   under *Settings → Secrets and variables → Actions*.

Deleting the commit is not enough — anything pushed to GitHub should be treated
as permanently public.

## How this project protects your key

- `.env` is in `.gitignore`, and `daily-ai doctor` fails if `.env` is ever
  tracked by git.
- The key is read from the environment at call time. It is never stored on an
  object, written to a file, or included in a log record.
- Text from a failed HTTP request passes through a redaction step before it is
  logged.
- Every subprocess call uses an argument list. `shell=True` appears nowhere in
  the codebase.
