# Graded tasks

Total: 7 points. Submit one PR into your fork that contains all four deliverables.

## Task 1 -- Workflow analysis (2 points)

Create `submission/analysis.md` in your fork. For each of the nine flaws in `.github/workflows/ai-review-insecure.yml`, answer:

1. What is the flaw (1-2 sentences)?
2. Which lecture slide category covers it (prompt injection, secret leakage, output validation, privilege, sandboxing, cost/DoS, supply chain)?
3. What is the concrete exploit scenario? Who does what to trigger it?

Use one short paragraph per flaw. A numbered list is fine.

## Task 2 -- Demonstrate prompt injection (2 points)

Pick one of these three injection strategies:

- **PR description injection:** open a PR against your fork whose description instructs the AI to approve the change and ignore findings.
- **Comment injection:** add a Python source comment in a changed file that instructs the AI to emit a specific fake finding or skip a file.
- **Diff injection:** craft a diff whose added lines contain instructions that override the system prompt.

For your chosen strategy, include in `submission/injection.md`:

1. The payload you used.
2. A screenshot of the PR comment the workflow produced (prove the injection worked).
3. A one-line explanation of why the insecure workflow could not defend against it.

## Task 3 -- Hardened workflow (2 points)

Rename `.github/workflows/ai-review-hardened.yml.TODO` to `.github/workflows/ai-review-hardened.yml` and implement it. The hardened workflow must:

- Trigger on `pull_request`, **not** `pull_request_target`.
- Declare `permissions:` explicitly with the minimum set (`contents: read`, `pull-requests: write`).
- Set a `timeout-minutes` value.
- Use `actions/checkout` with a bounded `fetch-depth`.
- Load the API key only in the step that needs it, not job-wide.
- Validate the model's JSON response against a schema before posting any PR comment. Reject and log a non-matching response instead of commenting.
- Apply a findings filter (follow the pattern from `anthropics/claude-code-security-review/claudecode/findings_filter.py`).
- Guard external-contributor PRs with an approval gate (follow the pattern documented in the reference repo's README).

Delete `ai-review-insecure.yml` in the same PR.

Credit is given for referencing the specific file or pattern from the reference repo you reused. Cite it in a short comment at the top of your workflow.

## Task 4 -- Verification (1 point)

Add a file `submission/verification.md` showing:

1. The same injection payload from Task 2, now producing no compromised output against the hardened workflow.
2. A screenshot or log excerpt of the hardened workflow rejecting a malformed LLM response (you can force this by temporarily replacing the API call with one that returns invalid JSON).

## Submission

Open a single PR against `main` of your fork titled `lecture10 submission <your-name>`. Paste the PR URL into Moodle by the deadline. Late submissions lose 1 point per day.

## What will fail this lab

- Patching the insecure workflow in place instead of writing a new one.
- Passing the API key directly in a workflow file or committing it.
- Using `pull_request_target` in the hardened workflow.
- A hardened workflow that still concatenates PR metadata directly into the user prompt without a boundary delimiter or validation step.
