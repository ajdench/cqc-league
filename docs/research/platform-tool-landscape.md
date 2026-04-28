# Platform Tool Landscape

This page compares the software markets that overlap with a possible sports medical governance and CQC-readiness platform.

Use it with [Platform Opportunity](platform-opportunity-tool-landscape.md), [Platform Product Blueprint](platform-product-blueprint.md), and [Platform MVP and Guardrails](platform-mvp-and-guardrails.md).

## Market map

| Segment | Examples | Strong capabilities | Limits for Rugby League CQC use |
| --- | --- | --- | --- |
| CQC compliance and quality platforms | [Radar Healthcare CQC Compliance Software](https://radarhealthcare.com/product/cqc-compliance-software/), [Vantage Compliance and Quality Management](https://vantage-technologies.co.uk/compliance-and-quality-management/), [QCS](https://www.qcs.co.uk/) | CQC-aligned evidence, policies, audits, document control, action plans, incident/risk modules, dashboards, inspection readiness. | Not built around sports-ground exclusions, participant-only care, RFL medical standards, anti-doping, athlete confidentiality, loan players, match-day/training-ground records, or dual clinical/performance reporting. |
| Sports medicine EMR and athlete management | [Kitman Labs Performance Medicine](https://www.kitmanlabs.com/platform/performance-medicine/), [Teamworks AMS / Smartabase](https://teamworks.com/smartabase), [AthleteMonitoring EMR](https://www.athletemonitoring.com/electronic-medical-records/), [SportsWareOnLine](https://sportswareonline.com/), [Orreco Medical Notes](https://www.orreco.ai/modules/medical-notes) | Athlete health records, injury and illness logs, SOAP notes, return-to-play, concussion, availability, diagnostics, medication/TUE tracking, performance data integration. | Usually framed as athlete care/performance medicine rather than CQC assessment evidence, regulated activity decisions, provider registration packs, CQC factual accuracy response, board assurance, or CQC-style policy control. |
| Sports governance, safeguarding, and health and safety | [SportLoMo Governance and Safe Sport](https://www.sportlomo.com/governance-and-safe-sport/), [Globocol Health and Safety in Sport](https://www.globocol.com/health-safety-sport-software), [CPOMS StudentSafe for Sports Clubs](https://www.cpoms.co.uk/cpoms-studentsafe-for-sports-clubs/), [Sport:80 Compliance Management](https://www.sport80.com/uk/features/compliance-management) | Safeguarding, vetting, certification, incident and injury workflows, audit trails, policy acknowledgement, concussion/return-to-play controls, club/federation reporting. | Strong on sport compliance, but not a CQC/private healthcare governance platform. Clinical records, medicines, regulated activities, provider registration, CQC evidence categories, and quality-statement assurance would still need a separate layer. |
| Generic healthcare incident/risk/audit systems | [Radar Healthcare Audit Management](https://radarhealthcare.com/product/audit-management-software/), Datix-style incident systems, generic GRC/EHS tools | Audits, incidents, risks, action plans, dashboards, evidence trails, safety learning. | Often too broad, hospital/social-care oriented, or not athlete-workflow friendly. May not capture sports medical edge cases without extensive configuration. |
| Regulatory and digital-health guardrails | [CQC evidence categories](https://www.cqc.org.uk/guidance-regulation/providers/assessment/evidence-categories), [ICO special category data guidance](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/special-category-data/what-is-special-category-data/), [NHS clinical safety DCB0129](https://standards.nhs.uk/published-standards/clinical-risk-management-its-application-in-the-manufacture-of-health-it-systems), [MHRA software and AI as a medical device](https://www.gov.uk/government/publications/software-and-artificial-intelligence-ai-as-a-medical-device/software-and-artificial-intelligence-ai-as-a-medical-device) | Evidence taxonomy, health data duties, clinical risk management, medical-device boundary. | These are not products, but they shape product design, documentation, risk management, and go-to-market limits. |

## What this suggests

The opportunity is not to rebuild every component from scratch. A practical platform could sit between existing tools:

- CQC compliance platforms provide useful patterns for policies, audits, action plans, and evidence packs.
- Sports medicine EMRs provide useful patterns for athlete injury, illness, medicines, rehabilitation, and return-to-play workflows.
- Sports safeguarding and governance systems provide useful patterns for vetting, eligibility, safe sport, safeguarding, and club/federation reporting.

The distinctive product layer would be the **CQC/Rugby League interpretation layer**:

- is the service outside scope, excluded, contractor-led, or potentially registerable?
- what evidence proves the conclusion?
- which records support CQC-style assurance?
- what must be reported to the board?
- what service change triggers reassessment?

## Related pages

- [Platform Product Blueprint](platform-product-blueprint.md) turns this landscape into product modules.
- [Registration Decision Model](registration-decision-model.md) supplies the CQC scope workflow.
- [Source Map](source-map.md) lists the external products and regulatory sources.
