# Platform Opportunity and Tool Landscape

This page turns the CQC/Rugby League research into a product opportunity: an online platform that helps professional sports teams understand when CQC registration may apply, maintain CQC-style governance evidence, and run the day-to-day records, audits, and assurance workflows that support safe medical services.

Read this page with the [Registration Decision Model](registration-decision-model.md), [Assurance Pack Templates](assurance-pack-templates.md), [Governance Operating Model](governance-operating-model.md), and [Medicines, Prescribing, and Anti-Doping](medicines-prescribing-anti-doping.md).

!!! warning "Product scope"
    This is a product research note, not legal advice, clinical software certification, or a decision that any Rugby League club is CQC-registerable. A platform should preserve legal/clinical review points rather than automate them away.

## Product hypothesis

There is a gap between three existing software markets:

1. **CQC compliance platforms** are strong at policies, audits, action plans, evidence stores, and inspection readiness, but are usually designed for care homes, clinics, hospitals, primary care, or social care rather than professional sport.
2. **Sports medicine and athlete management systems** are strong at injury, illness, rehabilitation, availability, and performance medicine records, but usually do not map records to CQC regulated activities, quality statements, evidence categories, or CQC assessment response packs.
3. **Sports governance and safeguarding tools** are strong at vetting, safeguarding, incident reporting, concussion workflows, safe sport governance, and eligibility controls, but usually do not provide private healthcare registration logic, CQC evidence mapping, clinical governance templates, or provider-level assurance.

The product opportunity is a **sports medical governance and CQC-readiness platform**: a system that keeps club medical operations sport-specific while making CQC evidence, records, and decision-making explicit where the club approaches regulated healthcare.

## Market landscape

| Segment | Examples | Strong capabilities | Limits for Rugby League CQC use |
| --- | --- | --- | --- |
| CQC compliance and quality platforms | [Radar Healthcare CQC Compliance Software](https://radarhealthcare.com/product/cqc-compliance-software/), [Vantage Compliance and Quality Management](https://vantage-technologies.co.uk/compliance-and-quality-management/), [QCS](https://www.qcs.co.uk/) | CQC-aligned evidence, policies, audits, document control, action plans, incident/risk modules, dashboards, inspection readiness. | Not built around sports-ground exclusions, participant-only care, RFL medical standards, anti-doping, athlete confidentiality, loan players, match-day/training-ground records, or dual clinical/performance reporting. |
| Sports medicine EMR and athlete management | [Kitman Labs Performance Medicine](https://www.kitmanlabs.com/platform/performance-medicine/), [Teamworks AMS / Smartabase](https://teamworks.com/smartabase), [AthleteMonitoring EMR](https://www.athletemonitoring.com/electronic-medical-records/), [SportsWareOnLine](https://sportswareonline.com/), [Orreco Medical Notes](https://www.orreco.ai/modules/medical-notes) | Athlete health records, injury and illness logs, SOAP notes, return-to-play, concussion, availability, diagnostics, medication/TUE tracking, performance data integration. | Usually framed as athlete care/performance medicine rather than CQC assessment evidence, regulated activity decisions, provider registration packs, CQC factual accuracy response, board assurance, or CQC-style policy control. |
| Sports governance, safeguarding, and health and safety | [SportLoMo Governance and Safe Sport](https://www.sportlomo.com/governance-and-safe-sport/), [Globocol Health and Safety in Sport](https://www.globocol.com/health-safety-sport-software), [CPOMS StudentSafe for Sports Clubs](https://www.cpoms.co.uk/cpoms-studentsafe-for-sports-clubs/), [Sport:80 Compliance Management](https://www.sport80.com/uk/features/compliance-management) | Safeguarding, vetting, certification, incident and injury workflows, audit trails, policy acknowledgement, concussion/return-to-play controls, club/federation reporting. | Strong on sport compliance, but not a CQC/private healthcare governance platform. Clinical records, medicines, regulated activities, provider registration, CQC evidence categories, and quality-statement assurance would still need a separate layer. |
| Generic healthcare incident/risk/audit systems | [Radar Healthcare Audit Management](https://radarhealthcare.com/product/audit-management-software/), Datix-style incident systems, generic GRC/EHS tools | Audits, incidents, risks, action plans, dashboards, evidence trails, safety learning. | Often too broad, hospital/social-care oriented, or not athlete-workflow friendly. May not capture sports medical edge cases without extensive configuration. |
| Regulatory and digital-health guardrails | [CQC evidence categories](https://www.cqc.org.uk/guidance-regulation/providers/assessment/evidence-categories), [ICO special category data guidance](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/special-category-data/what-is-special-category-data/), [NHS clinical safety DCB0129](https://standards.nhs.uk/published-standards/clinical-risk-management-its-application-in-the-manufacture-of-health-it-systems), [MHRA software and AI as a medical device](https://www.gov.uk/government/publications/software-and-artificial-intelligence-ai-as-a-medical-device/software-and-artificial-intelligence-ai-as-a-medical-device) | Evidence taxonomy, health data duties, clinical risk management, medical-device boundary. | These are not products, but they shape product design, documentation, risk management, and go-to-market limits. |

## CQC evidence model the platform should support

CQC's current provider assessment approach uses five key questions and evidence categories. CQC describes six evidence categories: people's experience, feedback from staff and leaders, feedback from partners, observation, processes, and outcomes. The product should not simply store files. It should map each piece of operational evidence to the relevant evidence category, CQC domain, service model, and club risk.

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

The platform should let a club assemble evidence by:

- CQC domain: safe, effective, caring, responsive, well-led;
- evidence category;
- regulated activity candidate;
- location;
- team category: first team, academy, women's, wheelchair, reserves;
- season and fixture;
- board reporting period;
- incident or audit action.

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

This is where sports tools such as SportLoMo, Globocol, CPOMS, and Sport:80 show strong patterns, but the CQC layer would add healthcare governance and provider evidence mapping.

### 6. Workforce, credentials, training, and privileges

The platform should maintain:

- professional registration and expiry checks;
- role, scope, and privileges;
- indemnity and insurance;
- DBS/safeguarding checks where relevant;
- RFL medical role requirements;
- IMMOFP/iIMMOFP evidence;
- concussion training;
- emergency care qualifications;
- anti-doping education;
- prescribing authority and medicines permissions.

This connects [RFL Medical Standards Map](rfl-medical-standards-map.md) with CQC staffing, fit-person, and well-led assurance.

### 7. Medicines, anti-doping, and therapeutic use exemptions

This module should be treated as high-risk because it sits at the intersection of clinical care, anti-doping, player welfare, and club reputation. It should include:

- medicine administration and prescribing log;
- allergy and contraindication checks;
- Global DRO/UKAD check reference;
- TUE requirement flag;
- controlled-drug controls where relevant;
- batch/expiry records;
- medicines incident reporting;
- audit and stock check;
- player advice and follow-up record.

The [Medicines and anti-doping log](assurance-pack-templates.md#7-medicines-and-anti-doping-log) is the minimum viable record model.

## Build, buy, or integrate

| Strategy | When it fits | Risks |
| --- | --- | --- |
| Build a specialist sports CQC platform | Best if the product aims to own the CQC/RFL governance layer and serve clubs across sports. | Must manage clinical data, information governance, clinical safety, and possible medical-device boundary. |
| Integrate with athlete EMR systems | Best where clubs already use Kitman Labs, Smartabase/Teamworks, AthleteMonitoring, SportsWare, or Orreco for medical records. | Need reliable APIs, permissions, and evidence mapping without duplicating records. |
| Integrate with CQC compliance tools | Best where a provider already uses Radar Healthcare, Vantage, QCS, or similar for wider healthcare compliance. | These tools may not understand sports workflows, RFL standards, or participant-only exclusions. |
| Start as documentation/evidence layer | Best for MVP: decision model, document pack, audits, evidence vault, board reporting. | Less useful if clubs need daily clinical record capture from day one. |
| Start as digital recording tool | Best if the immediate pain is match-day/training-ground records, incident logs, and medicines. | Without the CQC evidence layer it becomes another sports medical record product. |

The most pragmatic MVP is a **governance and evidence layer** with lightweight record capture, designed to integrate with specialist athlete EMR systems later.

## Product guardrails

### CQC framework versioning

CQC assessment terminology and scoring are changing. The platform should version its CQC mappings by date and source, and preserve the evidence basis for each mapping. Do not hard-code one static set of quality statements as if it will remain unchanged.

Relevant sources include [CQC evidence categories](https://www.cqc.org.uk/guidance-regulation/providers/assessment/evidence-categories), [CQC assessment](https://www.cqc.org.uk/guidance-regulation/providers/assessment), and CQC's consultation on [improving how it assesses and rates providers](https://www.cqc.org.uk/about-us/how-we-involve-you/consultations/improving-how-we-assess-and-rate-providers/part-1).

### Health data and confidentiality

Player medical data is special category health data. The [ICO guidance on special category data](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/special-category-data/what-is-special-category-data/) explicitly includes information about injury, diagnosis, treatment, test results, medical opinions, and future health status. The product should support role-based access, audit logs, coach-facing summaries, consent records, retention rules, and subject access/export processes.

### Clinical safety and medical-device boundary

If the platform only records, organises, and reports information, it may remain a governance/records system. If it starts recommending diagnosis, treatment, return-to-play decisions, risk stratification, or clinical action, the product may need clinical safety and medical-device analysis.

Relevant guardrails include [NHS DCB0129 clinical risk management](https://standards.nhs.uk/published-standards/clinical-risk-management-its-application-in-the-manufacture-of-health-it-systems), [NHS clinical safety developer guidance](https://digital.nhs.uk/developer/guides-and-documentation/introduction-to-healthcare-technology/clinical-safety), and [MHRA software and AI as a medical device guidance](https://www.gov.uk/government/publications/software-and-artificial-intelligence-ai-as-a-medical-device/software-and-artificial-intelligence-ai-as-a-medical-device).

### Registration boundary is a workflow, not a badge

The platform should not label a service "CQC compliant" as a static status. It should maintain a living evidence trail:

- what service was assessed;
- which source guidance was used;
- what facts were relied on;
- who approved the conclusion;
- when it must be reviewed;
- what service changes invalidate the conclusion.

## Proposed MVP

1. **CQC scope decision workflow** using the [Registration Decision Model](registration-decision-model.md).
2. **Stock documentation pack** based on [Assurance Pack Templates](assurance-pack-templates.md).
3. **Evidence vault** mapped to CQC key questions, evidence categories, and RFL medical standards.
4. **Incident and complaint workflow** with CQC, safeguarding, and RFL flags.
5. **Medicines and anti-doping log** with UKAD/Global DRO reference fields.
6. **Workforce credentials register** for medical staff, contractors, and role privileges.
7. **Board dashboard and export pack** for the Head of Medical and board of directors.

## Research still needed

- Interview Heads of Medical at Championship, Super League, women's, academy, and community clubs.
- Compare current use of athlete EMR systems in Rugby League and football clubs.
- Test whether clubs want an independent platform or an evidence layer that integrates with existing systems.
- Validate minimum viable document pack with sports regulatory lawyers and CQC specialists.
- Define data-controller and processor models for club, contractor, league, and platform.
- Assess whether any proposed decision-support features would trigger MHRA software-as-medical-device obligations.
- Map RFL Medical Standards 2026 clause-by-clause into product controls and evidence fields.
- Build a sample board dashboard using the [Board Medical Assurance Report](assurance-pack-templates.md#3-board-medical-assurance-report).

## Related pages

- [Registration Decision Model](registration-decision-model.md) supplies the service-scope workflow.
- [Assurance Pack Templates](assurance-pack-templates.md) supplies the initial stock documentation and evidence fields.
- [Governance Operating Model](governance-operating-model.md) supplies board, committee, and operational routines.
- [Private Healthcare Synergies](private-healthcare-synergies.md) explains what can be borrowed from independent healthcare providers.
- [RFL Medical Standards Map](rfl-medical-standards-map.md) anchors sport-specific evidence.
- [Source Map](source-map.md) lists the external sources used.
