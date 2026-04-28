# Product Research Roadmap

This page records the next research tasks for a Rugby League CQC governance platform. It is intentionally research-first: the wiki should establish what clubs, clinicians, boards, regulators, and league rules require before treating anything as a product specification.

## Current checklist

| Status | Item | Output in the wiki | Notes |
| --- | --- | --- | --- |
| Deferred | 1. Define target users and buying groups | Product persona page | Still needed, but not the next research pass. |
| Research baseline added | 2. Define the minimum viable compliance pack | [Minimum Compliance Pack Research](minimum-compliance-pack-research.md) | Research inventory added. Needs validation before it becomes a final pack. |
| Research baseline added | 3. Map RFL Medical Standards clause-by-clause | [RFL Clause Evidence Map](rfl-clause-evidence-map.md) | First-pass map strengthened with research maturity, status triage, and validation gaps. |
| Deferred | 4. Design the platform information architecture | Product blueprint update | Should wait until items 2, 3, 5, and 6 are better understood. |
| Research baseline added | 5. Research CQC scope decision workflow | [CQC Scope Decision Research](cqc-scope-decision-research.md) | Reframed from "prototype a wizard" to factual research and decision evidence. |
| Research baseline added | 6. Deepen market and tool research | [Platform Tool Landscape](platform-tool-landscape.md) | Reframed as market learning, capability gaps, and research still needed before build/buy decisions. |

## Working priorities

The current priority is to complete research for items **2, 3, 5, and 6** before moving further into solution design.

The research should answer four practical questions:

1. What evidence would a club reasonably need to hold?
2. Which RFL requirements are mandatory, best practice, information-only, or competition-specific?
3. What facts determine the CQC scope decision?
4. Which existing tools solve parts of the problem, and what gaps remain?

## Backlog detail

### 1. Target users and buying groups

The wiki should separate user needs by role:

- board and executive leaders need risk, assurance, and decision records;
- Head of Medical needs operational control, clinical governance, and evidence production;
- clinicians need efficient records, handovers, and professional independence;
- safeguarding and welfare leads need escalation routes and protected information flows;
- league or competition bodies may need aggregated assurance without inappropriate access to confidential medical records;
- external providers need contract, scope, indemnity, and evidence boundaries.

### 2. Minimum viable compliance pack

The pack research should identify which documents and records are genuinely necessary before deciding what to build:

- CQC scope decision record;
- medical service description;
- RFL standards evidence dashboard;
- clinical governance meeting record;
- contractor due diligence file;
- incident, serious injury, concussion, medicines, and complaint records;
- annual board assurance report.

Current output: [Minimum Compliance Pack Research](minimum-compliance-pack-research.md).

### 3. RFL clause-by-clause map

The first-pass detailed map is in [RFL Clause Evidence Map](rfl-clause-evidence-map.md). It should be treated as a research baseline, not a final control library. It still needs:

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

Current output: [CQC Scope Decision Research](cqc-scope-decision-research.md).

### 6. Market and tool research

The expanded [Platform Tool Landscape](platform-tool-landscape.md) should be used to understand adjacent markets before deciding whether to build, buy, or integrate. Current research should focus on:

- which capabilities already exist in CQC compliance tools;
- which capabilities already exist in sports EMRs;
- which capabilities already exist in sports governance/safeguarding systems;
- which product claims create clinical safety, information governance, or medical-device risk;
- what evidence clubs would need to procure or integrate any tool safely.

## Related pages

- [Platform Opportunity](platform-opportunity-tool-landscape.md)
- [Minimum Compliance Pack Research](minimum-compliance-pack-research.md)
- [CQC Scope Decision Research](cqc-scope-decision-research.md)
- [Platform Tool Landscape](platform-tool-landscape.md)
- [Platform Product Blueprint](platform-product-blueprint.md)
- [Platform MVP and Guardrails](platform-mvp-and-guardrails.md)
- [RFL Clause Evidence Map](rfl-clause-evidence-map.md)
