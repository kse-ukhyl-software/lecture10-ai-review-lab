## Flaw 1
Pull Request Target allows attackers to inject malicious code from the forked repos, creating PRs to original repo. Since PR is run inside base branch it gives them access to repository secrets.

**Category:** Privilege and sandboxing.

**Exploit Scenario:** An attacker opens a PR from a fork containing a malicious testing script. The workflow executes it, granting the untrusted code access to the repository's write token and secrets.

## Flaw 2
Write-All permissions allows attackers to do anything with objects in the repo. In the context of GH Actions it can be easily done through compromised user actions.

**Category:** Privilege and sandboxing.

**Exploit Scenario:** If an attacker compromises a workflow step via prompt injection or a malicious action, the write-all token allows them to push new code to the main branch or delete releases.

## Flaw 3
Providing API key on job level exposes it for each step of the job, even when it's not needed. This allows attackers to get it by injecting malicious code in some execution step of the job.

**Category:** Secret leakage.

**Exploit Scenario:** A malicious or typosquatted third-party action added to a later step in the workflow can quietly scrape the environment variables and steal the API key.

## Flaw 4
There is no timeout-minutes ceiling defined for the workflow. 

**Category:** Cost and denial of service.

**Exploit Scenario:** Attacker can inject code, that would lead to infinite text generation by LLM, which would lead to burning API costs and act as Denial of Service.

## Flaw 5
Zero depth gives a full access to the repo commit history. If developer accidentally committed secrets and forgot to rotate them and rewrite repo tree, it could lead to secret leakage.

**Category:** Data exposure.

**Exploit Scenario:** If a developer accidentally committed a secret in the past and removed it without rewriting the Git tree, an attacker can extract that lingering secret from the downloaded history.

## Flaw 6
No input limitations allows attackers to replace actual user prompt with malicious injections. This can be used to silence actual security report output.

**Category:** Prompt injection.

**Exploit Scenario:** An attacker writes a malicious instruction directly in the PR description. Because it is concatenated verbatim, the model cannot distinguish the attacker's text from the system's instructions.

## Flaw 7
The API request is raw, without any guidance and filtration, which allows attackers to invisibly inject whatever they want into model.

**Category:** Output validation.

**Exploit Scenario:** An attacker uses prompt injection to force the LLM to output a massive, free-form markdown block containing exfiltrated source code, and the workflow accepts it blindly.

## Flaw 8
The same as flaw 7, there is no strict schema or structure, so any output will be treated as trustworthy and as real security review.

**Category:** Output validation.

**Exploit Scenario:** An injected LLM outputs a fake "LGTM, no issues" message instead of a findings array. The workflow processes the manipulated text as a valid review.

## Flaw 9
The output of AI is returned directly as a markdown comment, which can be used to inject malicious links, images or fake profiles.

**Category:** Prompt injection, defense in depth.

**Exploit Scenario:** An attacker poisons the model to output markdown that includes phishing links or fake maintainer approval badges, tricking human reviewers into trusting the compromised code.

## Flaw 10
The pytest is run directly on the provided code from the PR, with combinantion of write-all and exposed API key, attacker could retrieve the API key or/and run malicious code. 

**Category:** Privilege and sandboxing, supply chain.

**Exploit Scenario:** An attacker modifies a Python test file in their PR to include a script that POSTs the ANTHROPIC_API_KEY to an external webhook when the tests run.