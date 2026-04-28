# Product Research Roadmap

This page records the next research and build tasks for a Rugby League CQC governance platform. It is intended to be updated as work is completed, so the wiki stays aligned with the product thinking rather than becoming a static research dump.

## Current checklist

| Status | Item | Output in the wiki | Notes |
| --- | --- | --- | --- |
| [ ] | 1. Define target users and buying groups | Product persona page | Separate club board, Head of Medical, clinicians, safeguarding/welfare, league body, and external provider needs. |
| [ ] | 2. Define the minimum viable compliance pack | Evidence-pack page or templates update | Convert the board summary into stock documents, registers, audit forms, and board reports. |
| [x] | 3. Map RFL Medical Standards clause-by-clause | [RFL Clause Evidence Map](rfl-clause-evidence-map.md) | Completed as a first-pass map from RFL clauses to evidence, owner, cadence, CQC lens, and platform field needs. |
| [ ] | 4. Design the platform information architecture | Product blueprint update | Define modules, data objects, permissions, exports, integrations, and evidence-pack assembly. |
| [ ] | 5. Prototype a CQC scope decision wizard | Registration decision model update | Turn the registration boundary questions into a structured club workflow with stored rationale and reassessment triggers. |
| [x] | 6. Deepen market and tool research | [Platform Tool Landscape](platform-tool-landscape.md) | Completed as a fuller market map across CQC compliance, sports EMR, sports governance, safeguarding, and regulatory guardrails. |

## Working priorities

The current product hypothesis is that the strongest MVP is a **governance and evidence layer** for professional sports medical services, rather than a full replacement for existing sports medicine EMRs.

The platform should initially help clubs answer four practical questions:

1. Does this service model create CQC registration risk?
2. What evidence proves the club's conclusion?
3. Which RFL Medical Standards controls are complete, overdue, or weak?
4. What board pack, CQC response pack, or league assurance pack can be generated from the evidence?

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

The pack should turn the research into reusable documents:

- CQC scope decision record;
- statement of medical service model;
- RFL Medical Standards dashboard;
- clinical governance meeting template;
- contractor due diligence checklist;
- incident, serious injury, concussion, medicines, and complaint templates;
- annual board assurance report.

### 3. RFL clause-by-clause map

The first-pass detailed map is in [RFL Clause Evidence Map](rfl-clause-evidence-map.md). It should be refined as the platform data model is built, especially around:

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

### 5. CQC scope decision wizard

The [Registration Decision Model](registration-decision-model.md) should become a decision workflow:

- identify activity;
- identify provider/control model;
- test sports-ground and temporary sporting-event exclusions;
- test diagnostics, remote advice, ambulance transport, medicines, and clinic triggers;
- capture evidence and legal/clinical review;
- trigger reassessment when the service model changes.

### 6. Market and tool research

The expanded [Platform Tool Landscape](platform-tool-landscape.md) should be used to decide whether to build, buy, or integrate. The current working assumption is:

- build the CQC/RFL interpretation and evidence layer;
- integrate with sports EMRs where clubs already use them;
- avoid building clinical decision support unless clinical safety and medical-device requirements are deliberately addressed.

## Related pages

- [Platform Opportunity](platform-opportunity-tool-landscape.md)
- [Platform Tool Landscape](platform-tool-landscape.md)
- [Platform Product Blueprint](platform-product-blueprint.md)
- [Platform MVP and Guardrails](platform-mvp-and-guardrails.md)
- [RFL Clause Evidence Map](rfl-clause-evidence-map.md)
