# Platform Opportunity

This page is the hub for product research on an online platform that helps professional sports teams understand CQC exposure, maintain CQC-style governance evidence, and run the day-to-day records, audits, and assurance workflows that support safe medical services.

It is intentionally short. The detailed tool landscape, product blueprint, MVP, and digital-health guardrails have been split into linked pages so board, clinical, product, and engineering readers can move directly to the material they need.

## Why split the platform research?

The content design guidance used for this wiki does not set a universal maximum page length. GOV.UK says page length depends on the content and user need, but warns against broad "everything you need to know" pages because they are hard to navigate. Nielsen Norman Group research, summarised by Newcastle University's digital design guidance, also reinforces that people usually scan web pages rather than reading every word.

For this wiki, the practical rule is:

- keep hub pages short;
- split long research into task-based pages;
- keep each page focused on one reader need;
- cross-link pages so the LLM output and human navigation both preserve context.

## Product hypothesis

There is a gap between three existing software markets:

1. **CQC compliance platforms** are strong at policies, audits, evidence stores, and inspection readiness, but are usually designed for care homes, clinics, hospitals, primary care, or social care rather than professional sport.
2. **Sports medicine and athlete management systems** are strong at injury, illness, rehabilitation, availability, and performance medicine records, but usually do not map records to CQC regulated activities, evidence categories, or CQC assessment response packs.
3. **Sports governance and safeguarding tools** are strong at vetting, safeguarding, incident reporting, concussion workflows, and safe sport governance, but usually do not provide private healthcare registration logic or CQC evidence mapping.

The product opportunity is a **sports medical governance and CQC-readiness platform**: a system that keeps club medical operations sport-specific while making CQC evidence, records, and decision-making explicit where the club approaches regulated healthcare.

## Split pages

- [Platform Tool Landscape](platform-tool-landscape.md) compares CQC compliance platforms, sports medicine EMRs, sports governance tools, and wider compliance systems.
- [Platform Product Blueprint](platform-product-blueprint.md) maps CQC evidence categories into product modules, records, evidence packs, and board dashboards.
- [Platform MVP and Guardrails](platform-mvp-and-guardrails.md) sets out build/buy/integrate options, minimum viable product, health data controls, clinical safety, and medical-device boundary risks.

## Core internal links

- [Registration Decision Model](registration-decision-model.md) supplies the service-scope workflow.
- [Assurance Pack Templates](assurance-pack-templates.md) supplies the initial stock documentation and evidence fields.
- [Governance Operating Model](governance-operating-model.md) supplies board, committee, and operational routines.
- [Private Healthcare Synergies](private-healthcare-synergies.md) explains what can be borrowed from independent healthcare providers.
- [RFL Medical Standards Map](rfl-medical-standards-map.md) anchors sport-specific evidence.
- [Source Map](source-map.md) lists the external sources used.
