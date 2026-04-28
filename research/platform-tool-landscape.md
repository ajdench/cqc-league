# Platform Tool Landscape

This page compares the software markets that overlap with a possible sports medical governance and CQC-readiness platform.

Use it with [Product Research Roadmap](product-research-roadmap.md), [Platform Opportunity](platform-opportunity-tool-landscape.md), [Platform Product Blueprint](platform-product-blueprint.md), and [Platform MVP and Guardrails](platform-mvp-and-guardrails.md).

This page completes roadmap item 6: deepen market and tool research.

## Market map

| Segment | Examples | Strong capabilities | Limits for Rugby League CQC use |
| --- | --- | --- | --- |
| CQC compliance and quality platforms | [Radar Healthcare CQC Compliance Software](https://radarhealthcare.com/product/cqc-compliance-software/), [Vantage Compliance and Quality Management](https://vantage-technologies.co.uk/compliance-and-quality-management/), [QCS](https://www.qcs.co.uk/) | CQC-aligned evidence, policies, audits, document control, action plans, incident/risk modules, dashboards, inspection readiness. | Not built around sports-ground exclusions, participant-only care, RFL medical standards, anti-doping, athlete confidentiality, loan players, match-day/training-ground records, or dual clinical/performance reporting. |
| Sports medicine EMR and athlete management | [Kitman Labs Performance Medicine](https://www.kitmanlabs.com/platform/performance-medicine/), [Teamworks AMS / Smartabase](https://teamworks.com/smartabase), [AthleteMonitoring EMR](https://www.athletemonitoring.com/electronic-medical-records/), [SportsWareOnLine](https://sportswareonline.com/), [Orreco Medical Notes](https://www.orreco.ai/modules/medical-notes) | Athlete health records, injury and illness logs, SOAP notes, return-to-play, concussion, availability, diagnostics, medication/TUE tracking, performance data integration. | Usually framed as athlete care/performance medicine rather than CQC assessment evidence, regulated activity decisions, provider registration packs, CQC factual accuracy response, board assurance, or CQC-style policy control. |
| Sports governance, safeguarding, and health and safety | [SportLoMo Governance and Safe Sport](https://www.sportlomo.com/governance-and-safe-sport/), [Globocol Safeguarding in Sport](https://www.globocol.com/safeguarding-sport-software), [CPOMS StudentSafe for Sports Clubs](https://www.cpoms.co.uk/cpoms-studentsafe-for-sports-clubs/), [Sport:80 Compliance Management](https://www.sport80.com/uk/features/compliance-management) | Safeguarding, vetting, certification, incident and injury workflows, audit trails, policy acknowledgement, concussion/return-to-play controls, club/federation reporting. | Strong on sport compliance, but not a CQC/private healthcare governance platform. Clinical records, medicines, regulated activities, provider registration, CQC evidence categories, and quality-statement assurance would still need a separate layer. |
| Generic healthcare incident/risk/audit systems | [Radar Healthcare Audit Management](https://radarhealthcare.com/product/audit-management-software/), Datix-style incident systems, generic GRC/EHS tools | Audits, incidents, risks, action plans, dashboards, evidence trails, safety learning. | Often too broad, hospital/social-care oriented, or not athlete-workflow friendly. May not capture sports medical edge cases without extensive configuration. |
| Regulatory and digital-health guardrails | [CQC evidence categories](https://www.cqc.org.uk/guidance-regulation/providers/assessment/evidence-categories), [ICO special category data guidance](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/special-category-data/what-is-special-category-data/), [NHS clinical safety DCB0129](https://standards.nhs.uk/published-standards/clinical-risk-management-its-application-in-the-manufacture-of-health-it-systems), [MHRA software and AI as a medical device](https://www.gov.uk/government/publications/software-and-artificial-intelligence-ai-as-a-medical-device/software-and-artificial-intelligence-ai-as-a-medical-device) | Evidence taxonomy, health data duties, clinical risk management, medical-device boundary. | These are not products, but they shape product design, documentation, risk management, and go-to-market limits. |

## Evaluation criteria

The useful comparison is not "which product is best?" but "which product category already solves part of the CQC/Rugby League problem?"

| Criterion | Why it matters for a professional club |
| --- | --- |
| CQC evidence mapping | The platform must organise evidence under CQC's evidence categories, quality statements, and provider governance expectations. |
| Sports medical workflow | The platform must work around fixtures, training, pitch-side incidents, concussion, return-to-play, player loans, and medical confidentiality. |
| RFL Medical Standards coverage | The platform must support mandatory staff, EAP, equipment, anti-doping, concussion, cardiac screening, infection control, and record-keeping evidence. |
| Clinical record boundary | The product must either store clinical notes safely or integrate with a specialist EMR without weakening evidence traceability. |
| Board assurance | Board users need risk, exceptions, overdue evidence, service-model changes, and assurance packs, not raw confidential medical notes. |
| Contractor/provider model | Clubs may use external doctors, ambulance providers, diagnostics providers, or screening providers. The platform needs contracts, credentials, scope, and registration/exemption evidence. |
| Data protection and permissions | Player health data is special category data. Role-based access, audit trails, disclosure logs, retention, and export controls are core requirements. |
| Clinical safety and medical-device boundary | If the system moves from evidence and records into recommendations or decision support, [NHS DCB0129](https://standards.nhs.uk/published-standards/clinical-risk-management-its-application-in-the-manufacture-of-health-it-systems) and [MHRA software guidance](https://www.gov.uk/government/publications/software-and-artificial-intelligence-ai-as-a-medical-device/software-and-artificial-intelligence-ai-as-a-medical-device) become design constraints. |

## Category findings

### CQC compliance and quality platforms

[Radar Healthcare](https://radarhealthcare.com/product/cqc-compliance-software/) is a strong example of the regulated-provider pattern: CQC evidence, audits, action plans, incident/risk management, document control, workforce compliance, and reporting. [Vantage](https://vantage-technologies.co.uk/compliance-and-quality-management/) presents a similar quality-management and compliance pattern for healthcare providers. [QCS](https://www.qcs.co.uk/qcs-compliance-centre/) is more policy and procedure oriented, with regulated-sector compliance content and update discipline. [Log my Care](https://www.logmycare.co.uk/blog/cqc-recommends-going-digital) is useful as a social-care digital-record and CQC-readiness reference, but its care-home/home-care workflow is not a sports medical workflow.

The lesson is that CQC-readiness products are good at evidence, policies, audits, actions, and inspection packs. They are weak on sports-specific concepts such as concussion, athlete availability, RFL mandatory equipment, match-day medical cover, loan-player handovers, anti-doping, and the sports-ground exclusion.

### Sports medicine EMR and athlete management

[Kitman Labs Performance Medicine](https://www.kitmanlabs.com/platform/performance-medicine/), [Teamworks AMS / Smartabase](https://teamworks.com/smartabase), [AthleteMonitoring](https://www.athletemonitoring.com/electronic-medical-records/), [SportsWareOnLine](https://sportswareonline.com/), and [Orreco Medical Notes](https://www.orreco.ai/modules/medical-notes) show mature patterns for athlete health records, injury and illness tracking, SOAP notes, documents, medical screening, concussion, medications, rehabilitation, dashboards, and performance-data integration.

The lesson is that sports EMRs are likely better than a new CQC product at day-to-day clinical records. The gap is that they do not usually generate CQC registration rationale, board-level CQC assurance, RFL clause evidence packs, CQC factual accuracy responses, or regulated-provider governance documentation.

### Sports governance, safeguarding, and compliance platforms

[SportLoMo](https://www.sportlomo.com/governance-and-safe-sport/), [Globocol](https://www.globocol.com/safeguarding-sport-software), [CPOMS StudentSafe for Sports Clubs](https://www.cpoms.co.uk/cpoms-studentsafe-for-sports-clubs/), and [Sport:80](https://www.sport80.com/uk/features/compliance-management) show strong sports-governance patterns: safeguarding, welfare, credentials, vetting, certifications, policy acknowledgements, incident workflows, eligibility, concussion/return-to-play controls, dashboards, and federation-level reporting.

The lesson is that sport already has software patterns for governance and compliance. The missing layer is healthcare-provider governance: regulated activity scope, clinical record integrity, confidentiality, medicines, diagnostics, contractor healthcare oversight, and CQC-style evidence.

### Digital health and regulatory guardrails

The platform must respect CQC's [evidence categories](https://www.cqc.org.uk/guidance-regulation/providers/assessment/evidence-categories), the ICO's [special category data](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/special-category-data/what-is-special-category-data/) rules for health data, [NHS DCB0129](https://standards.nhs.uk/published-standards/clinical-risk-management-its-application-in-the-manufacture-of-health-it-systems) if manufacturing health IT with clinical risk, and [MHRA software and AI as a medical device guidance](https://www.gov.uk/government/publications/software-and-artificial-intelligence-ai-as-a-medical-device/software-and-artificial-intelligence-ai-as-a-medical-device) if the system starts to make or materially influence clinical decisions.

The lesson is to keep the MVP on evidence, workflow, assurance, reminders, and structured documentation. Clinical decision support should be a deliberate later decision, not an accidental feature.

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

## Build, buy, or integrate view

| Need | Best route | Rationale |
| --- | --- | --- |
| CQC/RFL interpretation, scope decisions, evidence packs | Build | This is the distinctive gap in the market. |
| Day-to-day clinical notes and athlete EMR | Integrate first | Sports EMRs already do this well and clubs may already have one. |
| Workforce credentials and training | Build light, integrate later | Minimum version needs RFL/professional registration tracking; larger clubs may integrate with HR or sports-governance tools. |
| Safeguarding and welfare case management | Integrate or clearly separate | Safeguarding tools already exist and access boundaries are sensitive. |
| Board dashboard and action plan | Build | The board needs a CQC/RFL assurance view across evidence sources. |
| Medical-device or clinical decision support | Avoid in MVP | Higher regulatory, safety, and assurance burden. |

## Procurement questions

For any tool being bought or integrated, the club should ask:

- Can it export records and evidence in a usable format for CQC, RFL, board, insurer, or legal review?
- Can it separate confidential clinical notes from board-visible assurance?
- Does it support role-based access, audit trails, retention rules, and disclosure logs?
- Can evidence be mapped to RFL Medical Standards and CQC quality statements?
- Can it handle match-day, training-ground, travel, loan-player, and contractor workflows?
- Does it integrate through API or structured export?
- Is UK GDPR and special category data handling documented?
- Does the vendor make any clinical decision-support claims that could create clinical safety or medical-device obligations?

## Product gap statement

No researched product appears to combine all of the following in one Rugby League-specific package:

- CQC registration boundary decision support for sports medical services;
- RFL Medical Standards clause evidence mapping;
- board assurance packs that avoid inappropriate disclosure of player clinical data;
- integration-ready links to athlete EMRs and sports governance platforms;
- contractor/provider due diligence for doctors, diagnostics, cardiac screening, ambulance cover, and clinic services;
- CQC factual accuracy and assessment-response packs.

That gap supports the working MVP in [Platform MVP and Guardrails](platform-mvp-and-guardrails.md): a governance and evidence layer that can sit above or beside existing systems.

## Related pages

- [Product Research Roadmap](product-research-roadmap.md) tracks the next work.
- [Platform Product Blueprint](platform-product-blueprint.md) turns this landscape into product modules.
- [Registration Decision Model](registration-decision-model.md) supplies the CQC scope workflow.
- [RFL Clause Evidence Map](rfl-clause-evidence-map.md) defines the sport-specific evidence checklist the platform should support.
- [Source Map](source-map.md) lists the external products and regulatory sources.
