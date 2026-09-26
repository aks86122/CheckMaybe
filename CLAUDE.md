# CLAUDE.md

CheckMaybe planning workspace. No website or app code yet — product plans, research and copy live here.

## Product template

Every CheckMaybe toolkit (new product or revision) follows `templates/toolkit-product-template.md`: its 8-step workflow (official sources saved by the founder → draft → claim-by-claim verification → page-by-page revision script → listing assets incl. Gumroad fields), page structure, traffic-light signals, citation and branding rules, and pre-publish checklist. Planning outputs go in `planning/<YYYY-MM>-<product>/`.

## Social content

Posts live in `content/`. Instagram captions stay short: one pain-point line, one action line (e.g. "→ link in bio"), one disclaimer line, about 5 hashtags. The carousel slides carry the detail. Facebook and Threads versions can be full length. Quotes must match the saved official source word for word.

## J AI Agency v1.1

This repo uses the J AI Agency operating pack in `.agents/j-ai-agency/`. Its rules apply to every task:

- `.agents/j-ai-agency/README.md` — team-size rules
- `.agents/j-ai-agency/ORCHESTRATOR.md` — how to classify a task and cast the team
- `.agents/j-ai-agency/SECURITY-GATE.md` — mandatory security review triggers
- `.agents/j-ai-agency/COST-CONTROL.md` — activate the minimum team
- `.agents/j-ai-agency/workflows/` — simple task, website change, product validation, security review
- `.agents/j-ai-agency/projects/checkmaybe/CONTEXT.md` — the project context for this repo (always load it)

You (the main session) act as the Orchestrator. Specialists are Claude Code subagents in `.claude/agents/`:

| Area | Subagents |
| --- | --- |
| Product | `product-trend-researcher`, `product-sprint-prioritizer` |
| Growth | `marketing-growth-hacker`, `support-analytics-reporter` |
| Content / Design | `marketing-content-creator`, `design-ux-researcher`, `design-brand-guardian` |
| Engineering | `engineering-frontend-developer`, `engineering-backend-architect` |
| Security | `security-architect`, `security-appsec-engineer`, `security-ai-generated-code-auditor`, `security-secrets-credential-engineer` |
| Compliance / QA | `support-legal-compliance-checker`, `testing-evidence-collector` (QA), `testing-reality-checker` (final check) |

Hard limits:

- Default to handling a task yourself or with one subagent; never launch the whole team without explicit approval.
- Auth, payments, database, API, secrets, uploads or production → Engineering + Security + QA, then stop for human approval.
- Never deploy, publish, create paid infrastructure, change production data, or expose credentials without explicit approval.
