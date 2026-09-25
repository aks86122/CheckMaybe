# Core Team (v1.1)
Full agent definitions come from msitarzewski/agency-agents (MIT, commit 053ddbb). See THIRD-PARTY-LICENSE.md.

## Precedence
README.md, ORCHESTRATOR.md, SECURITY-GATE.md, COST-CONTROL.md and the active project CONTEXT.md override anything in an agent file.
If an agent file suggests deploying, publishing, spawning more agents, or running autonomously, ignore that part and follow the approval gates.

## Control
Agents Orchestrator — use ../ORCHESTRATOR.md. The upstream orchestrator is intentionally NOT included: it runs an autonomous multi-agent pipeline, which conflicts with COST-CONTROL.md.

## Product
Trend Researcher — agents/product/product-trend-researcher.md
Sprint Prioritizer — agents/product/product-sprint-prioritizer.md

## Growth
Growth Hacker — agents/marketing/marketing-growth-hacker.md
Analytics Reporter — agents/support/support-analytics-reporter.md

## Content / Design
Content Creator — agents/marketing/marketing-content-creator.md
UX Researcher — agents/design/design-ux-researcher.md
Brand Guardian — agents/design/design-brand-guardian.md

## Engineering
Frontend Developer — agents/engineering/engineering-frontend-developer.md
Backend Architect — agents/engineering/engineering-backend-architect.md

## Security
Security Architect — agents/security/security-architect.md
Application Security Engineer — agents/security/security-appsec-engineer.md
AI Code Security Auditor — agents/security/security-ai-generated-code-auditor.md
Secrets Hygiene — agents/security/security-secrets-credential-engineer.md

## Compliance / QA
Legal Compliance Checker — agents/support/support-legal-compliance-checker.md
Evidence Collector — agents/testing/testing-evidence-collector.md  (this is the "QA" role in README.md)
Reality Checker — agents/testing/testing-reality-checker.md  (final independent check)
