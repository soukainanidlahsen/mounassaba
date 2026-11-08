# Mounassaba Security and Privacy Findings

**Audit date:** 2026-11-08  
**Scope:** Static backend/configuration review and safe local checks. No penetration test, mobile binary, hosted service, production database, or dependency advisory scan was available.

## Summary

No mobile security surface exists in the repository because there is no mobile application. No concrete SQL injection, SSRF, or exploitable business API issue was confirmed; the relevant application APIs and domain logic are absent. This is not a clean security bill of health: production readiness is blocked by an unsupported Django series, development defaults in the WSGI path, a non-runnable PostgreSQL configuration, incomplete transport hardening, and no privacy/release evidence.

The local `.env` was not opened. The SQLite database was not inspected for personal rows. No real credentials were printed. No destructive or active attack testing was performed.

## Findings

### SEC-01 — HIGH — Unsupported Django release series

- **Affected component:** Django runtime and `backend/requirements.txt:1` (`Django>=5.0,<5.1`); local venv has Django 5.0.14.
- **Evidence:** The official Django supported-version table marks Django 5.0 unsupported and lists security support ending 2025-04-02. [Official Django support table](https://www.djangoproject.com/download/)
- **Attack scenario / condition:** An application deployed on this series remains without upstream fixes if a relevant vulnerability is discovered or exploited. This audit did not validate a specific exploitable CVE.
- **Impact:** Elevated exposure to known/future framework flaws and inability to receive upstream security updates.
- **Reproduction:** `python -m pip freeze` showed Django 5.0.14; requirement range excludes supported feature/LTS series.
- **Remediation:** Select a currently supported Django series, update compatible packages, run migration/regression/security checks, and lock the tested dependency set.
- **Release blocker:** Yes.
- **Complexity:** MEDIUM-HIGH.

### SEC-02 — HIGH — WSGI defaults to development settings

- **Affected component:** `backend/config/wsgi.py:5`, `backend/manage.py:7-10`, `backend/config/settings/development.py:10-20`.
- **Evidence:** Both entry points default to `config.settings.development`; development settings set `DEBUG=True` and SQLite.
- **Attack scenario / condition:** If a production launcher imports WSGI without explicitly setting `DJANGO_SETTINGS_MODULE=config.settings.production`, it can run with development settings. No deployment configuration was present to verify the override.
- **Impact:** Debug responses may disclose sensitive implementation details, and the service may use an unintended local database/configuration.
- **Reproduction:** Static configuration inspection; no production server was launched.
- **Remediation:** Make production settings selection explicit in deployment configuration and add a startup/deployment assertion that rejects debug mode and SQLite in production.
- **Release blocker:** Yes until the actual deployed startup path is verified.
- **Complexity:** LOW.

### SEC-03 — HIGH — Production PostgreSQL configuration cannot initialize

- **Affected component:** `backend/config/settings/production.py:12-21`; `backend/requirements.txt:1-9`; `backend/.env.example:9-10`.
- **Evidence:** Production uses Django's PostgreSQL backend, but neither `psycopg` nor `psycopg2` is declared/installed. Production configuration expects split `DB_*` variables; the example shows only a commented `DATABASE_URL`. A safe production check with an ephemeral placeholder password failed with `ImproperlyConfigured: Error loading psycopg2 or psycopg module` before attempting a database connection.
- **Attack scenario / condition:** Not a direct exploit; this is an availability/deployment failure when attempting production startup. A failed or improvised deployment may encourage unsafe configuration workarounds.
- **Impact:** No verified production service can start with the repository's declared dependencies and supplied configuration contract.
- **Remediation:** Declare a supported PostgreSQL driver; align settings and environment docs; verify startup in isolated staging without connecting to or altering the user's local database.
- **Release blocker:** Yes.
- **Complexity:** LOW-MEDIUM.

### SEC-04 — MEDIUM — Production transport policy lacks explicit redirect/HSTS

- **Affected component:** `backend/config/settings/production.py:23-31` and any external TLS termination layer.
- **Evidence:** Production settings disable debug and set secure session/CSRF cookies and `X_FRAME_OPTIONS`, but do not set `SECURE_SSL_REDIRECT` or `SECURE_HSTS_SECONDS`. No proxy/load-balancer configuration exists in the repository.
- **Attack scenario / condition:** A public service is reachable over plaintext HTTP and no upstream layer redirects or blocks it.
- **Impact:** Session credentials or other traffic could be exposed in transit; the actual deployment edge is unknown.
- **Remediation:** Document and verify TLS termination; enforce HTTPS at the edge and configure trusted proxy/security settings and HSTS safely for the production domain.
- **Release blocker:** Yes until HTTPS enforcement is demonstrated.
- **Complexity:** MEDIUM.

### SEC-05 — MEDIUM — Replace-me secret example is not guarded at startup

- **Affected component:** `backend/.env.example:4-7`; `backend/config/settings/base.py:18-20`; `production.py` inherits base settings.
- **Evidence:** The example supplies a replace-me `SECRET_KEY` value; base settings read the environment value but contain no explicit check that the placeholder or a weak key is rejected in production. The actual ignored `.env` was not read.
- **Attack scenario / condition:** An operator copies the example unchanged into production or uses a predictable secret.
- **Impact:** Django signing, session, and token-related security can be undermined if the weak example value is used.
- **Remediation:** Generate a unique high-entropy production secret, keep it in a secret manager, reject placeholder/weak values in production startup, and rotate any exposed real value.
- **Release blocker:** Yes if production secret strength/rotation is not verified.
- **Complexity:** LOW.

### SEC-06 — MEDIUM — No privacy notice, account lifecycle rights, or processing evidence

- **Affected component:** Account model/API, future mobile collection screens, database operations, and third-party hosting/notification services.
- **Evidence:** `backend/accounts/models.py:5-15` includes inherited identity fields and optional phone; no registration UI, privacy notice, consent/disclosure, account deletion/export, retention, processor, or transfer documentation exists in the repository.
- **Attack scenario / condition:** A release collects/uses identifiable information without a reviewed purpose, notice, retention, user-rights process, or applicable CNDP formalities.
- **Impact:** Privacy harm and potential legal/regulatory exposure. Applicability and obligations depend on actual data flows, processing parties, and hosting.
- **Remediation:** Map data and purposes; minimize fields; document retention, access/deletion, processors, hosting/transfers, and user disclosures; obtain qualified Moroccan legal/CNDP review. The CNDP publishes Law 09-08 and guidance on processing, formalities, and transfers. [CNDP legal texts](https://www.cndp.ma/textes-et-lois/), [CNDP conditions](https://www.cndp.ma/conditions/), [CNDP notifications](https://www.cndp.ma/notifier-un-traitement/)
- **Release blocker:** Yes, until reviewed for the real product data flow. This is a compliance review gate, not a legal conclusion.
- **Complexity:** MEDIUM (technical/docs); legal review separate.

### SEC-07 — MEDIUM — Future API authorization policy is not sufficient by itself

- **Affected component:** DRF defaults in `backend/config/settings/base.py:140-154`; empty account/provider URL modules.
- **Evidence:** Default permission is `IsAuthenticatedOrReadOnly`; there are no object-level permission classes or marketplace views. Current API roots return 404, so no active marketplace object-access exploit was reproduced.
- **Attack scenario / condition:** A future mutating view is added without explicit role, ownership, and state-transition checks. Any authenticated user allowed by the global default could then be able to write to resources outside their ownership if the view is not scoped.
- **Impact:** Potential cross-account data access, privilege escalation, or unauthorized booking changes after endpoints are introduced.
- **Remediation:** Define a role/action matrix; implement query scoping and object permissions; test horizontal/vertical access denial and invalid state transitions for every endpoint.
- **Release blocker:** Yes for any marketplace API release.
- **Complexity:** MEDIUM.

### SEC-08 — INFO — Mobile-specific security cannot be assessed

- **Affected component:** Future mobile binary, token storage, deep links, TLS/client networking, local logs, OS backup, clipboard/screenshots, and permissions.
- **Evidence:** No mobile source, manifest, app binary, or mobile dependency exists in the repository.
- **Attack scenario / condition:** Not assessable; there is no mobile client to test.
- **Impact:** Secure storage, endpoint validation, deep-link handling, and leakage risk remain unknown until implementation exists.
- **Remediation:** Reassess the actual client after a platform/framework is selected; test storage, logs, transport, lifecycle, permissions, and release build settings on supported OS versions.
- **Release blocker:** Yes for a mobile release because the client itself is absent.
- **Complexity:** NOT ESTIMABLE before implementation.

## Not confirmed / not testable

- No raw SQL, upload handler, arbitrary URL fetch, custom serializer, or deserialization pathway was found. SQL injection, SSRF, path traversal, mass assignment, and file-upload safety therefore have no application handler to assess; absence of a handler is not a passed security test.
- No rate limiting/throttling is configured for the future API; no API endpoints currently exist. Add abuse controls before exposing public signup/search/booking routes.
- CORS is environment allow-list based (`base.py:129-135`); production origin values were not available for review.
- No security headers/TLS behavior was tested over a real public deployment.
- No dependency scanner was available (`pip-audit` absent), so no package-by-package vulnerability-free claim is made.
