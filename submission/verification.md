### Part 1

I tried to break the system prompt provided in the hardened workflow by forcing it to forget previous instructions or omit vulnerabilities.

```text
You are a strict security reviewer. Analyze the following git diff for security vulnerabilities.
Do not include style issues. Output ONLY valid JSON matching the schema.
```

I also tried to flood AI with garbaged PR difference to lose context about vulnerabilities.

### Part 2

![alt text](image-1.png)

![alt text](image.png)