# CQC League Governance Wiki

This wiki captures research on [Care Quality Commission (CQC)](https://www.cqc.org.uk/) governance requirements and how they may apply to professional Rugby League club medical services in England.

The core conclusion is practical: most match-day and training-ground treatment for players is likely to sit inside CQC's sports-ground or temporary sporting-event exclusions for [treatment of disease, disorder or injury](https://www.cqc.org.uk/guidance-regulation/providers/registration/scope-registration/regulated-activities/treatment-disease-disorder-or-injury), but a club can still create CQC exposure if it operates a broader private healthcare service, diagnostics pathway, clinic, remote triage service, or subcontracted service where the club controls regulated healthcare activity.

!!! warning "Scope"
    This is a research and governance design aid, not legal advice. Registration decisions should be checked against the latest CQC guidance and, for borderline service models, with specialist regulatory counsel or CQC.

## How to use this wiki

- Use [Board Briefing](research/board-briefing.md) as the initial board-facing summary from the Head of Medical.
- Use [Board CQC Response and Outcomes](research/board-cqc-response.md) for assessment response, factual accuracy, positive and negative findings, and enforcement planning.
- Start with [CQC Governance Baseline](research/cqc-governance-baseline.md) for the regulatory architecture.
- Read [CQC Assurance Domains and Quality Statements](research/cqc-assurance-domains-quality-statements.md) for the assessment lens CQC uses to judge quality.
- Use [CQC Registration Edge Cases](research/cqc-registration-edge-cases.md) for diagnostics, injections, remote advice, ambulance transport, contractors, and public clinic services.
- Use [Professional Rugby League Application](research/rugby-league-application.md) to map sports-club medical provision to likely CQC triggers and exclusions.
- Use [Worked Examples](research/worked-examples.md) to test realistic club service models against the registration and assurance logic.
- Use [RFL Medical Standards Map](research/rfl-medical-standards-map.md) to connect the 2026 RFL Medical Standards to CQC-style assurance.
- Use [Private Healthcare Synergies](research/private-healthcare-synergies.md) to borrow governance controls from independent healthcare providers.
- Use [Medicines, Prescribing, and Anti-Doping](research/medicines-prescribing-anti-doping.md) for the highest-risk operational interface between clinical care and elite sport.
- Use [Registration Decision Model](research/registration-decision-model.md) as the working checklist before launching or changing a medical service.
- Use [CQC Scope Decision Research](research/cqc-scope-decision-research.md) and [CQC Scope Question Bank](research/cqc-scope-question-bank.md) to identify the facts and evidence needed before any decision tool is designed.
- Use [Governance Operating Model](research/governance-operating-model.md) as a board-to-pitch operating template.
- Use [Minimum Compliance Pack Research](research/minimum-compliance-pack-research.md) and [Minimum Compliance Pack Scenario Matrix](research/minimum-compliance-pack-scenario-matrix.md) to understand the evidence pack before turning it into final templates or software fields.
- Use [Assurance Pack Templates](research/assurance-pack-templates.md) to turn the research into repeatable governance documents.
- Use [Product Research Roadmap](research/product-research-roadmap.md), [Platform Opportunity](research/platform-opportunity-tool-landscape.md), [Tool Landscape](research/platform-tool-landscape.md), [Wiki Visual Tooling Register](research/wiki-visual-tooling-register.md), [Product Blueprint](research/platform-product-blueprint.md), and [MVP and Guardrails](research/platform-mvp-and-guardrails.md) to shape an online product that combines CQC readiness, sports medical records, evidence management, visual explanation, and governance tooling.
- Use [Research Scope and Assumptions](research/research-scope-assumptions.md) before treating item 1 as product users or buying groups.
- Use [Scope Decision Record](research/scope-decision-record.md) for the current working audience and output: an online CQC inspection preparation platform for professional sports clubs, using a Championship Rugby League Club as the starting example.
- Use [Research Validation Plan](research/research-validation-plan.md) before moving from research into solution design.

## Site structure

The research is split into logical sections:

- **Board and Decisions**: board briefing, CQC response, registration decision workflow, CQC scope research, question bank, and worked examples.
- **CQC Framework**: regulatory baseline, assessment model, edge cases, and private healthcare synergies.
- **Rugby League Application**: sport-specific application, RFL standards overview, clause evidence map, clause status register, medicines, prescribing, and anti-doping.
- **Operating Model and Evidence**: governance routines, minimum compliance pack research, templates, and evidence packs.
- **Platform Product Research**: product roadmap, research scope, scope decision, validation plan, opportunity, tool landscape, visual tooling, tool comparison, product modules, MVP, and guardrails.

## LLM Wiki outputs

The [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) build uses [mkdocs-llms-source](https://pypi.org/project/mkdocs-llms-source/) so the published site behaves as an LLM-friendly wiki:

- `/llms.txt`: curated LLM index generated from the navigation.
- `/llms-full.txt`: concatenated source content for LLM context.
- per-page Markdown copies alongside the HTML pages.

## External reference anchors

- Current CQC registration scope starts with [CQC: Scope of registration](https://www.cqc.org.uk/guidance-regulation/providers/registration/scope-registration).
- The initial board-facing output is [Board Briefing](research/board-briefing.md).
- The sport-specific regulatory boundary is explored in [CQC Registration Edge Cases](research/cqc-registration-edge-cases.md).
- CQC decision-tool research is separated in [CQC Scope Decision Research](research/cqc-scope-decision-research.md) and [CQC Scope Question Bank](research/cqc-scope-question-bank.md) so the wiki does not jump straight to a software answer.
- Applied service models are tested in [Worked Examples](research/worked-examples.md).
- Rugby League-specific obligations are mapped from the [RFL Medical Standards 2026](https://www.rugby-league.com/uploads/docs/Medical%20Standards%202026.pdf).
- The minimum evidence pack is researched in [Minimum Compliance Pack Research](research/minimum-compliance-pack-research.md) and tested against practical scenarios in [Minimum Compliance Pack Scenario Matrix](research/minimum-compliance-pack-scenario-matrix.md) before being turned into templates.
- Medicines and anti-doping controls use [UKAD Search Check Apply](https://www.ukad.org.uk/searchcheckapply) and [GMC prescribing guidance](https://www.gmc-uk.org/professional-standards/the-professional-standards/good-practice-in-prescribing-and-managing-medicines-and-devices).
- The product opportunity is split across [Product Research Roadmap](research/product-research-roadmap.md), [Platform Opportunity](research/platform-opportunity-tool-landscape.md), [Tool Landscape](research/platform-tool-landscape.md), [Wiki Visual Tooling Register](research/wiki-visual-tooling-register.md), [Product Blueprint](research/platform-product-blueprint.md), and [MVP and Guardrails](research/platform-mvp-and-guardrails.md), including external examples from CQC compliance platforms, sports medicine EMRs, safeguarding systems, visual documentation tooling, and digital health compliance guidance.
- [Research Scope and Assumptions](research/research-scope-assumptions.md) reframes item 1 as audience, decision context, and boundary rather than product buying personas.
- [Scope Decision Record](research/scope-decision-record.md) records the current working scope as an online CQC inspection preparation platform for professional sports clubs, using a Championship Rugby League Club as the starting example.
- The [Research Validation Plan](research/research-validation-plan.md) records what must be confirmed with club, RFL, CQC/legal, vendor, and information-governance sources.
