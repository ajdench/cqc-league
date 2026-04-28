# Platform Product Blueprint

This page maps CQC evidence and Rugby League medical governance into possible platform modules.

Use it with [Product Research Roadmap](product-research-roadmap.md), [Platform Tool Landscape](platform-tool-landscape.md), [Assurance Pack Templates](assurance-pack-templates.md), and [Governance Operating Model](governance-operating-model.md).

## CQC evidence model the platform should support

CQC's current provider assessment approach uses five key questions and evidence categories. CQC describes six evidence categories: people's experience, feedback from staff and leaders, feedback from partners, observation, processes, and outcomes.

The product should not simply store files. It should map operational evidence to the relevant evidence category, CQC domain, service model, location, team category, and club risk.

| CQC evidence category | Sports medical evidence examples | Platform feature |
| --- | --- | --- |
| People's experience | Player feedback, academy parent feedback, complaint themes, consent and confidentiality feedback. | Player-safe feedback forms, confidential surveys, complaint log, trend dashboard. |
| Feedback from staff and leaders | Head of Medical reports, clinician speaking-up records, staff debriefs, board medical assurance minutes. | Structured debriefs, board report builder, staff survey, speaking-up workflow. |
| Feedback from partners | Contractor quality reports, ambulance/venue feedback, NHS/private clinic referral feedback, league/club welfare feedback. | Contractor portal, partner evidence upload, referral outcome tracker. |
| Observation | Match-day medical room checks, training-ground audits, emergency action plan drills, equipment observations. | Mobile audit checklist, photo evidence, drill records, corrective actions. |
| Processes | Policies, SOPs, service scope decisions, clinical records, medicines logs, CQC registration analyses. | Policy library, version control, decision model, clinical forms, medicines/TUE workflow. |
| Outcomes | Injury trends, return-to-play delays, concussion compliance, incident recurrence, audit closure, complaint response times. | Dashboards, outcome metrics, exception reporting, board assurance packs. |

This links directly to [CQC Assurance Domains and Quality Statements](cqc-assurance-domains-quality-statements.md) and the [Board Medical Assurance Report](assurance-pack-templates.md#3-board-medical-assurance-report).

## Core product modules

### 1. Registration and scope decision engine

The platform should guide the club through the [Registration Decision Model](registration-decision-model.md), not replace expert judgement. It should record:

- user group: players, academy, staff, officials, public, schools, sponsors;
- location: stadium, training ground, away fixture, mobile unit, third-party premises, remote service;
- activity: treatment, diagnostics, screening, prescribing, injections, remote triage, transport, rehabilitation, mental health;
- sports-ground or sporting-event exclusion analysis;
- provider/control analysis: club, contractor, joint service, registered provider;
- decision outcome: outside scope, sports exclusion, contractor registered, contractor exempt, likely club registration, legal/CQC advice needed.

The decision output should populate the [CQC scope assessment template](assurance-pack-templates.md#1-cqc-scope-assessment), produce a board-readable summary, and trigger periodic reassessment when the service changes.

### 2. Adaptable documentation library

The platform should include stock documents that are adaptable by sport, league, team type, and service model:

- statement of purpose;
- medical governance policy;
- clinical records policy;
- incident and serious event policy;
- complaints policy;
- safeguarding clinical interface policy;
- medicines, prescribing, controlled drugs, and anti-doping policy;
- emergency action plan template;
- contractor due diligence checklist;
- data protection and confidentiality policy;
- remote advice and triage SOP;
- diagnostics and screening governance SOP.

These should be version-controlled and linked to evidence categories, regulations, RFL obligations, and board approval dates. The templates in [Assurance Pack Templates](assurance-pack-templates.md) are the first minimum content set.

### 3. Digital clinical and sports medical records

A sports team needs structured clinical records without turning coach-facing performance notes into unrestricted health records. Useful modules include:

- injury and illness record;
- pitchside assessment and treatment note;
- training-ground treatment note;
- SOAP note;
- concussion/HIA/return-to-play record;
- rehabilitation and restriction plan;
- referral and diagnostics tracker;
- medication and anti-doping/TUE log;
- consent and information-sharing preferences;
- loan-player and transfer handover record;
- academy parental communication log.

The product should respect the confidentiality risks described in [Medicines, Prescribing, and Anti-Doping](medicines-prescribing-anti-doping.md) and should separate clinical notes from coach/performance availability summaries.

### 4. Evidence vault and CQC pack builder

The platform should let a club assemble evidence by CQC domain, evidence category, regulated activity candidate, location, team category, season, board reporting period, and incident/audit action.

Outputs should include:

- CQC registration readiness pack;
- CQC assessment evidence pack;
- CQC factual accuracy response bundle;
- board medical assurance report;
- contractor assurance pack;
- annual governance review pack.

This is the productised version of [Governance Operating Model](governance-operating-model.md) and [Assurance Pack Templates](assurance-pack-templates.md).

### 5. Incident, complaint, safeguarding, and duty-of-candour workflow

The platform should combine sport incident reporting with healthcare-style governance:

- injury, medicines, equipment, safeguarding, data, complaint, contractor, and emergency-transfer categories;
- immediate action and escalation;
- root cause analysis;
- action plan and closure evidence;
- RFL reporting flag;
- CQC notification/duty-of-candour review flag;
- safeguarding lead notification;
- board-level trend reporting.

This is where sports governance tools show strong patterns, but the CQC layer would add healthcare governance and provider evidence mapping.

### 6. Workforce, credentials, training, and privileges

The platform should maintain professional registration, role and scope, indemnity, DBS/safeguarding checks where relevant, RFL medical role requirements, IMMOFP/iIMMOFP evidence, concussion training, emergency care qualifications, anti-doping education, and medicines permissions.

This connects [RFL Medical Standards Map](rfl-medical-standards-map.md) with CQC staffing, fit-person, and well-led assurance.

### 7. Medicines, anti-doping, and therapeutic use exemptions

This module should include medicine administration and prescribing logs, allergy checks, Global DRO/UKAD check references, TUE flags, controlled-drug controls, batch/expiry records, medicines incident reporting, audit, stock checks, player advice, and follow-up records.

The [Medicines and anti-doping log](assurance-pack-templates.md#7-medicines-and-anti-doping-log) is the minimum viable record model.

## Related pages

- [Platform MVP and Guardrails](platform-mvp-and-guardrails.md) turns this blueprint into an implementation route.
- [Assurance Pack Templates](assurance-pack-templates.md) supplies the first version of forms and reports.
- [Product Research Roadmap](product-research-roadmap.md) tracks the next research and build tasks.
- [RFL Clause Evidence Map](rfl-clause-evidence-map.md) defines the clause-level evidence the platform should support.
