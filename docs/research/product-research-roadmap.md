# Product Research Roadmap

This page records the next research tasks for a Rugby League CQC governance platform. It is intentionally research-first: the wiki should establish what clubs, clinicians, boards, regulators, and league rules require before treating anything as a product specification.

## Current checklist

| Status | Item | Output in the wiki | Notes |
| --- | --- | --- | --- |
| Scope page added | 1. Define research audience and decision context | [Research Scope and Assumptions](research-scope-assumptions.md) | Reframed away from product buyers. The next decision is scope, audience, and immediate output. |
| Scenario matrix added | 2. Define the minimum viable compliance pack | [Minimum Compliance Pack Research](minimum-compliance-pack-research.md) and [Minimum Compliance Pack Scenario Matrix](minimum-compliance-pack-scenario-matrix.md) | Research inventory tested against six scenarios. Still needs external validation before final pack design. |
| Status register added | 3. Map RFL Medical Standards clause-by-clause | [RFL Clause Evidence Map](rfl-clause-evidence-map.md) and [RFL Clause Status Register](rfl-clause-status-register.md) | Status, Championship relevance, record visibility, and validation gaps added. Still needs RFL/Head of Medical validation. |
| Deferred | 4. Design the platform information architecture | Product blueprint update | Should wait until items 2, 3, 5, and 6 are better understood. |
| Question bank added | 5. Research CQC scope decision workflow | [CQC Scope Decision Research](cqc-scope-decision-research.md) and [CQC Scope Question Bank](cqc-scope-question-bank.md) | Question bank added and tested against the six scenarios. Still needs regulatory validation. |
| Capability comparison added | 6. Deepen market and tool research | [Platform Tool Landscape](platform-tool-landscape.md) and [Tool Capability Comparison](tool-capability-comparison.md) | Capability comparison and vendor verification questions added. Still needs vendor/current-system validation. |

## Working priorities

The current priority is to settle item **1** as a research scope question, then use that decision to decide how far to take items **2, 3, 5, and 6**.

The research should answer five practical questions:

1. Who is the research for, and what decision should it support?
2. What evidence would a club reasonably need to hold?
3. Which RFL requirements are mandatory, best practice, information-only, or competition-specific?
4. What facts determine the CQC scope decision?
5. Which existing tools solve parts of the problem, and what gaps remain?

## Backlog detail

### 1. Research audience and decision context

This item is now reframed in [Research Scope and Assumptions](research-scope-assumptions.md). The research should not start with a product buying group. It should first decide:

- whether the concrete reference is Sheffield Eagles, a generic Championship club, professional Rugby League, or professional sport more broadly;
- whether the immediate output is a board/Head of Medical pack, a reusable framework, a validation plan, or future platform research;
- which audiences need to make decisions now;
- which product-shaped work should remain deferred.

### 2. Minimum viable compliance pack

The pack research should identify which documents and records are genuinely necessary before deciding what to build:

- CQC scope decision record;
- medical service description;
- RFL standards evidence dashboard;
- clinical governance meeting record;
- contractor due diligence file;
- incident, serious injury, concussion, medicines, and complaint records;
- annual board assurance report.

Current output: [Minimum Compliance Pack Research](minimum-compliance-pack-research.md) and [Minimum Compliance Pack Scenario Matrix](minimum-compliance-pack-scenario-matrix.md).

### 3. RFL clause-by-clause map

The first-pass detailed map is in [RFL Clause Evidence Map](rfl-clause-evidence-map.md), with status and visibility detail in [RFL Clause Status Register](rfl-clause-status-register.md). It should be treated as a research baseline, not a final control library. It still needs:

- exact mandatory versus best-practice status;
- competition-specific differences;
- evidence owner;
- evidence cadence;
- platform fields and export format.

### 4. Platform information architecture

The existing [Platform Product Blueprint](platform-product-blueprint.md) should be expanded into data objects and permissions:

- club, venue, service, provider, clinician, fixture, training session, player, incident, record, audit, action, evidence item, policy, board report;
- role-based access for medical confidentiality, board assurance, safeguarding, and external contractors;
- exports for CQC, RFL, board, insurer, and clinical audit use.

### 5. CQC scope decision research

The [Registration Decision Model](registration-decision-model.md) should be expanded into a decision research protocol before it becomes any software workflow:

- identify activity;
- identify provider/control model;
- test sports-ground and temporary sporting-event exclusions;
- test diagnostics, remote advice, ambulance transport, medicines, and clinic triggers;
- capture evidence and legal/clinical review points;
- trigger reassessment when the service model changes.

Current output: [CQC Scope Decision Research](cqc-scope-decision-research.md) and [CQC Scope Question Bank](cqc-scope-question-bank.md).

### 6. Market and tool research

The expanded [Platform Tool Landscape](platform-tool-landscape.md) should be used to understand adjacent markets before deciding whether to build, buy, or integrate. Current research should focus on:

- which capabilities already exist in CQC compliance tools;
- which capabilities already exist in sports EMRs;
- which capabilities already exist in sports governance/safeguarding systems;
- which product claims create clinical safety, information governance, or medical-device risk;
- what evidence clubs would need to procure or integrate any tool safely.

Current output: [Platform Tool Landscape](platform-tool-landscape.md) and [Tool Capability Comparison](tool-capability-comparison.md).

## Related pages

- [Research Validation Plan](research-validation-plan.md)
- [Research Scope and Assumptions](research-scope-assumptions.md)
- [Platform Opportunity](platform-opportunity-tool-landscape.md)
- [Minimum Compliance Pack Research](minimum-compliance-pack-research.md)
- [Minimum Compliance Pack Scenario Matrix](minimum-compliance-pack-scenario-matrix.md)
- [CQC Scope Decision Research](cqc-scope-decision-research.md)
- [CQC Scope Question Bank](cqc-scope-question-bank.md)
- [RFL Clause Status Register](rfl-clause-status-register.md)
- [Tool Capability Comparison](tool-capability-comparison.md)
- [Platform Tool Landscape](platform-tool-landscape.md)
- [Platform Product Blueprint](platform-product-blueprint.md)
- [Platform MVP and Guardrails](platform-mvp-and-guardrails.md)
- [RFL Clause Evidence Map](rfl-clause-evidence-map.md)
