# Platform MVP and Guardrails

This page sets out implementation choices and risk controls for a sports medical governance and CQC-readiness platform.

Use it with [Platform Opportunity](platform-opportunity-tool-landscape.md), [Platform Tool Landscape](platform-tool-landscape.md), and [Platform Product Blueprint](platform-product-blueprint.md).

## Build, buy, or integrate

| Strategy | When it fits | Risks |
| --- | --- | --- |
| Build a specialist sports CQC platform | Best if the product aims to own the CQC/RFL governance layer and serve clubs across sports. | Must manage clinical data, information governance, clinical safety, and possible medical-device boundary. |
| Integrate with athlete EMR systems | Best where clubs already use Kitman Labs, Smartabase/Teamworks, AthleteMonitoring, SportsWare, or Orreco for medical records. | Need reliable APIs, permissions, and evidence mapping without duplicating records. |
| Integrate with CQC compliance tools | Best where a provider already uses Radar Healthcare, Vantage, QCS, or similar for wider healthcare compliance. | These tools may not understand sports workflows, RFL standards, or participant-only exclusions. |
| Start as documentation/evidence layer | Best for MVP: decision model, document pack, audits, evidence vault, board reporting. | Less useful if clubs need daily clinical record capture from day one. |
| Start as digital recording tool | Best if the immediate pain is match-day/training-ground records, incident logs, and medicines. | Without the CQC evidence layer it becomes another sports medical record product. |

The most pragmatic MVP is a **governance and evidence layer** with lightweight record capture, designed to integrate with specialist athlete EMR systems later.

## Proposed MVP

1. **CQC scope decision workflow** using the [Registration Decision Model](registration-decision-model.md).
2. **Stock documentation pack** based on [Assurance Pack Templates](assurance-pack-templates.md).
3. **Evidence vault** mapped to CQC key questions, evidence categories, and RFL medical standards.
4. **Incident and complaint workflow** with CQC, safeguarding, and RFL flags.
5. **Medicines and anti-doping log** with UKAD/Global DRO reference fields.
6. **Workforce credentials register** for medical staff, contractors, and role privileges.
7. **Board dashboard and export pack** for the Head of Medical and board of directors.

## Product guardrails

### CQC framework versioning

CQC assessment terminology and scoring are changing. The platform should version its CQC mappings by date and source, and preserve the evidence basis for each mapping. Do not hard-code one static set of quality statements as if it will remain unchanged.

Relevant sources include [CQC evidence categories](https://www.cqc.org.uk/guidance-regulation/providers/assessment/evidence-categories), [CQC assessment](https://www.cqc.org.uk/guidance-regulation/providers/assessment), and CQC's consultation on [improving how it assesses and rates providers](https://www.cqc.org.uk/about-us/how-we-involve-you/consultations/improving-how-we-assess-and-rate-providers/part-1).

### Health data and confidentiality

Player medical data is special category health data. The [ICO guidance on special category data](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/special-category-data/what-is-special-category-data/) explicitly includes information about injury, diagnosis, treatment, test results, medical opinions, and future health status.

The product should support:

- role-based access;
- audit logs;
- coach-facing summaries separated from clinical records;
- consent records;
- retention rules;
- subject access and export processes;
- data-controller and processor records for club, contractor, league, and platform roles.

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

- [Platform Product Blueprint](platform-product-blueprint.md) defines the proposed modules.
- [Medicines, Prescribing, and Anti-Doping](medicines-prescribing-anti-doping.md) explains the highest-risk operational workflow.
- [Source Map](source-map.md) lists external sources.
