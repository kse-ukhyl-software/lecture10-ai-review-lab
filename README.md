# Lecture 10 -- AI-Powered Code Review Lab

**Course:** CI/CD Security (KSE, Spring 2026)
**Lecture:** 10 -- AI-Powered Security Tools in CI/CD

## What this lab is

This repository ships a GitHub Actions workflow that calls the Anthropic API via `curl` to review pull requests. **The workflow is intentionally insecure.** Every design decision in `.github/workflows/ai-review-insecure.yml` violates at least one best practice from Lecture 10.

Your job is:

1. Read the insecure workflow and identify why each piece is unsafe.
2. Demonstrate at least one of the attacks the workflow enables.
3. Replace the insecure workflow with a hardened one, reusing the patterns from [anthropics/claude-code-security-review](https://github.com/anthropics/claude-code-security-review).

See [TASKS.md](TASKS.md) for the graded checklist and [docs/insecure-workflow-analysis.md](docs/insecure-workflow-analysis.md) for a hint sheet that maps each flaw to a specific lecture slide.

## Repo layout

```
.
|-- README.md                          this file
|-- TASKS.md                           graded tasks + submission format
|-- sample-app/                        tiny Flask API with seeded vulnerabilities
|   |-- app.py                         the target the AI will review
|   |-- requirements.txt
|   `-- tests/test_smoke.py            sanity tests
|-- .github/workflows/
|   |-- ai-review-insecure.yml         the bad workflow (DO NOT fix in place)
|   `-- ai-review-hardened.yml.TODO    stub you must rewrite and rename to .yml
`-- docs/
    |-- insecure-workflow-analysis.md  per-flaw hints mapped to lecture slides
    `-- hardening-checklist.md         checklist for the hardened workflow
```

## Getting started

1. Fork this repository into your own GitHub account.
2. In your fork, add a repository secret named `ANTHROPIC_API_KEY` with a key that has access to the Claude API. Use a low-budget key -- the insecure workflow does not rate-limit itself.
3. Read Lecture 10 slides before touching anything.
4. Work through [TASKS.md](TASKS.md) in order.
5. Submit via a single PR into your fork. Include the PR URL in Moodle.

## Warning

Do not enable the insecure workflow on a repository that contains real secrets or proprietary code. The workflow sends file contents and PR metadata to a third-party API with no redaction. Keep the lab repo self-contained.

## References

- Lecture 10 slides (on Moodle)
- [anthropics/claude-code-security-review](https://github.com/anthropics/claude-code-security-review) -- the reference the hardened workflow must reuse
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)
- [GitHub Actions security hardening](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)
