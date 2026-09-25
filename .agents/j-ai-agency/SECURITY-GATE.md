# Security Gate
Mandatory for auth/authz, Stripe/payment flows, webhooks, secrets, DB/migrations, personal data, uploads, dependencies, infrastructure, CI/CD, production, and security-sensitive AI code.

Review: threat surface; auth/authz; validation/injection; secrets; privacy/data exposure; dependencies; logs/errors; abuse cases; minimal remediation; verification.

Hard rules:
- Never store credentials in agent Markdown/source-controlled context.
- Never deploy automatically.
- Security findings do not authorize broad refactors.
- Critical unresolved risk blocks production recommendation.
