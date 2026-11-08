# Mounassaba Production Readiness Checklist

**Audit date:** 2026-11-08  
**Current release status:** **NOT READY**

Legend: **PASS** = evidence verified; **FAIL** = known requirement missing; **BLOCKED** = cannot test because implementation/environment is absent; **NOT VERIFIED** = evidence required before release.

## Product and platform

| Gate | Status | Evidence / required action |
|---|---|---|
| Approved launch scope documented | PASS for audit assumptions | Request-based bookings, no online payments, manual approval, French-first, city/region search are audit baseline. |
| Target mobile platforms/framework selected | FAIL | No mobile framework/project; decide Android, iOS, or both and platform strategy. |
| Releaseable mobile client exists | FAIL | No mobile app sources or binaries. |
| Customer journey end-to-end | FAIL | No UI, account API, provider search, or booking workflow. |
| Provider journey end-to-end | FAIL | No provider profile/listing/approval/booking workflow. |
| Admin marketplace moderation | FAIL | Only custom user is registered in Django Admin. |
| French-first localization | BLOCKED | No mobile UI or translation resources. |
| City/region search | FAIL | No location fields or search endpoint. |

## Backend, data, and integration

| Gate | Status | Evidence / required action |
|---|---|---|
| Public auth/API contracts | FAIL | API roots return 404; add routes, schemas, validation, errors, versioning/docs. |
| Role and object-level authorization | NOT VERIFIED / FAIL | No product API or permissions tests. Define and verify ownership boundaries. |
| Provider/listing approval and visibility | FAIL | No domain models or moderation. |
| Booking ownership and state integrity | FAIL | No booking data model, transaction, state machine, or tests. |
| PostgreSQL production initialization | FAIL | Driver absent; current production settings check fails before DB connection. |
| Safe, rehearsed migrations | NOT VERIFIED | Only initial account migration exists; test against isolated DB and database copy before release. |
| Backup and restore procedure | FAIL | No documented or tested procedure. |
| Media upload/storage access controls | FAIL | No upload workflow or production storage setup. |

## Security and privacy

| Gate | Status | Evidence / required action |
|---|---|---|
| Supported framework/dependency baseline | FAIL | Django 5.0.14 is unsupported; upgrade and scan dependencies. |
| Production settings selected and debug off | NOT VERIFIED / FAIL | WSGI defaults to development. Verify actual deployment environment. |
| TLS enforced and security headers verified | NOT VERIFIED / FAIL | No deployment edge; production settings omit explicit redirect/HSTS. |
| Production secret is unique and protected | NOT VERIFIED | `.env` not inspected; production secret strength not evidenced. |
| API abuse protection | FAIL | No rate limiting/throttling configured for future public API. |
| Privacy notice, collection purpose, retention, rights | FAIL | No mobile disclosure/account deletion/export/retention docs. |
| Moroccan data-protection/CNDP review | NOT VERIFIED | Obtain qualified review of real processing, hosting, and transfer flows. |
| Mobile local storage/network/deep-link security | BLOCKED | No mobile app exists. |
| Dependency vulnerability scan | BLOCKED | `pip-audit` unavailable; no scanner report. |

## Quality and operations

| Gate | Status | Evidence / required action |
|---|---|---|
| Automated tests exist | FAIL | Django test runner found zero tests. |
| Critical customer/provider/API tests pass | FAIL | No relevant tests or workflows. |
| Mobile build and signing reproducible | FAIL | No Android/iOS project or signing configuration. |
| CI build/test pipeline | FAIL | No CI workflow. |
| Accessibility and device matrix verified | BLOCKED | No mobile UI or supported-device matrix. |
| Performance target measured | NOT VERIFIED | No workload, SLO, or performance environment. |
| Monitoring, health checks, alerts | FAIL | No deployment/observability configuration. |
| Incident rollback/release procedure | FAIL | No release or rollback documentation. |
| Store metadata/privacy declarations | BLOCKED | No app identity/binary/privacy disclosures to evaluate. |
| User support/privacy policy URL | NOT VERIFIED | No evidence in repository. |

**Release rule:** Do not submit to a store or expose a public production service until all FAIL and release-blocking NOT VERIFIED items are resolved and supported by test/deployment evidence. Optional future Arabic/RTL, distance search, and payments are not launch blockers under the current MVP assumptions.
