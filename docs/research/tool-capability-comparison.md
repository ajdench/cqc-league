# Tool Capability Comparison

This page hardens item 6 by comparing relevant tool categories against the evidence needs now emerging from the wiki. It should be read with [Platform Tool Landscape](platform-tool-landscape.md) and [Minimum Compliance Pack Scenario Matrix](minimum-compliance-pack-scenario-matrix.md).

This remains research. It does not select a vendor or define a build decision.

## Capability comparison

| Capability | Healthcare/CQC operations tools | Sports EMR/AMS tools | Sports governance/safeguarding tools | Research implication |
| --- | --- | --- | --- | --- |
| CQC policy and inspection readiness | Strong in tools such as Agilio TeamNet, Radar, QCS, and Vantage. | Usually not CQC-specific. | Usually not CQC-specific. | Useful comparator for evidence packs and audit discipline. |
| Significant events, incidents, and action tracking | Strong in healthcare compliance tools; variable by vendor. | Present where sports injury/medical incidents are captured. | Strong for safeguarding/welfare incidents. | Need to separate clinical incidents, safeguarding, RFL reporting, and CQC-style governance. |
| Workforce training and acknowledgements | Strong in Agilio-style healthcare operations and some compliance tools. | Variable. | Strong where vetting/certification is central. | Useful for RFL medical staff, CPD, anti-doping, mental health training, and policy acknowledgement. |
| Athlete clinical records | Generally weak or generic. | Strong in Kitman Labs, Teamworks AMS, AthleteMonitoring, SportsWareOnLine, and Orreco-style systems. | Usually weak. | A CQC/RFL evidence layer should not assume it can replace sports EMR without research. |
| Concussion and return-to-play | Generic in CQC tools; stronger in sport-specific platforms. | Strong in mature sports EMRs, especially where SCAT/SCOAT/baselines are supported. | Sometimes present as eligibility/compliance workflow. | Need to test whether exports satisfy RFL and board assurance needs. |
| Medicines, stock, TUE, anti-doping | Present in some healthcare and sports EMR systems, but not always anti-doping-specific. | Often stronger for athlete context. | Usually limited. | Must verify Global DRO/TUE evidence, restricted access, and audit trail. |
| Contractor due diligence | Strong pattern in healthcare compliance tools. | Usually not a core feature. | Variable. | Important for cardiac screening, ambulance/event cover, diagnostics, and external clinicians. |
| CQC scope decision evidence | General CQC context may exist. | Usually absent. | Usually absent. | This remains the most distinctive research gap. |
| Board assurance without clinical detail | Strong dashboard pattern in compliance tools; sports EMRs may expose availability summaries. | Strong for performance/availability, weaker for CQC governance. | Strong for safeguarding/compliance status. | Need to validate what board should see and what must remain restricted. |
| Data export/API | Vendor-specific. | Mature vendors often advertise export/API capabilities. | Variable. | Procurement must test export quality, not just feature claims. |

## Vendor verification questions

| Vendor/category | Questions to ask before relying on it |
| --- | --- |
| Agilio TeamNet / healthcare operations tools | Can policies, significant events, staff training, review dates, safety alerts, and audit trails be configured around RFL standards? Can it separate confidential player clinical data from board assurance? Can it export evidence packs? |
| Radar / healthcare risk and audit tools | Can incidents, audits, risks, and actions be mapped to RFL clauses and CQC evidence categories? Can contractor due diligence and match-day evidence be handled without over-configuration? |
| QCS / policy and compliance content tools | Is the value mainly policy content, or can evidence, actions, and board assurance be operationalised? Can sports-specific documents be maintained cleanly? |
| Vantage / compliance and quality management | Can quality management workflows support sports medical edge cases, contractors, and RFL evidence? What export and permission model is available? |
| Kitman Labs / sports EMR | Can concussion, medicines, TUE, screening, injury, and clinical records be exported into governance evidence without exposing unnecessary clinical detail? |
| Teamworks AMS / Smartabase | Can forms, dashboards, athlete records, and exports support RFL/CQC evidence mapping? What API/export options exist? |
| AthleteMonitoring / SportsWareOnLine / Orreco | Which clinical records, SOAP notes, medicine, injury, and return-to-play fields are exportable, and how is confidentiality controlled? |
| Sport:80 / SportLoMo / CPOMS / Globocol | Can safeguarding, vetting, eligibility, incident, and compliance workflows integrate with medical governance without conflating safeguarding records and clinical notes? |

## Research conclusions

- Healthcare operations tools look strongest for policies, training, significant events, review dates, audit trails, and inspection-readiness patterns.
- Sports EMR/AMS tools look strongest for day-to-day athlete medical records, concussion, injury lifecycle, medication, screening, and return-to-play evidence.
- Sports governance/safeguarding tools look strongest for eligibility, vetting, safeguarding, welfare, policy acknowledgement, and federation-style reporting.
- No researched category has yet been shown to cover CQC scope reasoning, RFL clause evidence, board-safe assurance, contractor provider-control analysis, and sports clinical records in one package.
- The next research should test exports and permissions against the [Minimum Compliance Pack Scenario Matrix](minimum-compliance-pack-scenario-matrix.md), not just compare marketing claims.

## Related pages

- [Platform Tool Landscape](platform-tool-landscape.md)
- [Minimum Compliance Pack Scenario Matrix](minimum-compliance-pack-scenario-matrix.md)
- [CQC Scope Question Bank](cqc-scope-question-bank.md)
- [Research Validation Plan](research-validation-plan.md)
- [Source Map](source-map.md)
