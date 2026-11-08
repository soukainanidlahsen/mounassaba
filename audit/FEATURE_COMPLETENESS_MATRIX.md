# Mounassaba Feature Completeness Matrix

**Audit date:** 2026-11-08  
**MVP basis:** request-based bookings; no online payments; manual provider/listing approval; French-first; Moroccan city/region search; Arabic/RTL and distance search deferred.

| Feature | Expected | Implemented | Tested | Status | Evidence |
|---|---|---|---|---|---|
| Android/iOS mobile client | Releaseable mobile application for approved platforms | No mobile project found | No mobile build/test possible | NOT IMPLEMENTED | Repository inventory contains no Android, iOS, Flutter, React Native, Expo, or other mobile sources/manifests. |
| Customer registration | Customer can register and access marketplace | No registration API or UI | No | NOT IMPLEMENTED | `backend/accounts/urls.py:1-3` empty; no views/serializers; no mobile client. |
| Customer login/logout | Authenticated customer session/token lifecycle | JWT authentication configured, no token routes or client | No | PARTIALLY IMPLEMENTED | `backend/config/settings/base.py:140-165`; test client only reached Admin login redirect. |
| Token obtain/refresh | Documented JWT issue/refresh flows | No token obtain/refresh URLs | No | NOT IMPLEMENTED | `accounts/urls.py:1-3`; no token views. |
| Profile management | Customer/provider profile creation and editing | `CustomUser` only with inherited fields and optional phone | No | PARTIALLY IMPLEMENTED | `backend/accounts/models.py:1-15`; Admin registration only. |
| Provider registration/onboarding | Provider submits profile and listing | No provider model or onboarding route | No | NOT IMPLEMENTED | `backend/providers/models.py:1`; `providers/urls.py:1-3`. |
| Provider verification/manual approval | Staff approve/suspend provider | No provider verification status or workflow | No | NOT IMPLEMENTED | No provider entity, moderation route, or admin screen. |
| Service categories and listings | Providers publish services; only approved listings visible | No category/listing model or endpoint | No | NOT IMPLEMENTED | No catalog models/views/URLs. |
| Portfolio/image management | Provider uploads and manages images safely | Pillow installed and media paths configured only | No | NOT IMPLEMENTED | `requirements.txt:5`; `base.py:115-121`; no file field/upload endpoint. |
| Provider discovery | Customer browses approved providers/listings | No list endpoint or UI | Smoke request returned 404 at provider API root | NOT IMPLEMENTED | `providers/urls.py:1-3`; observed `GET /api/providers/` = 404. |
| City/region search | Filter providers by Moroccan city/region | No location fields, search view, or UI | No | NOT IMPLEMENTED | No provider/location model or endpoint. |
| Price/category filters | Filter provider services | DRF filter backends configured globally; no view/queryset | No | PARTIALLY IMPLEMENTED | `base.py:147-153`; no list API exists. |
| Customer booking request | Customer requests provider service/date | No event/booking model or endpoint | No | NOT IMPLEMENTED | No booking code; account/provider routes empty. |
| Provider accept/reject | Provider changes own request state | No state machine, transaction, or authorization | No | NOT IMPLEMENTED | No booking entity or workflow. |
| Booking status/cancellation | Customer/provider tracks and cancels according to policy | No status/history/cancellation behavior | No | NOT IMPLEMENTED | No workflow code/tests. |
| Booking ownership/conflict handling | Prevent cross-user edits, duplicate/conflicting requests | No object-level permissions or booking logic | No | NOT IMPLEMENTED | No booking/API code. |
| Admin authentication | Staff can access administrative interface | Django Admin mounted; unauthenticated GET redirects | Route only smoke-tested | IMPLEMENTED BUT NOT VERIFIED | `backend/config/urls.py:7-8`; observed `GET /admin/` = 302. Authenticated operation not tested. |
| Admin marketplace moderation | Approve providers/listings, suspend accounts, oversee bookings | Only custom user registered | No | PARTIALLY IMPLEMENTED | `backend/accounts/admin.py:1-8`; no provider/listing/booking models or admin. |
| Notifications | Users receive request/status updates | No email/push/in-app event system; dev console email backend only | No | NOT IMPLEMENTED | `development.py:23-25`; no providers/SDKs/tasks. |
| Online payments | Not part of initial MVP | No payment code | N/A | NOT APPLICABLE | Explicit MVP assumption: defer online payments. |
| Reviews and chat | Not required for initial MVP unless separately approved | No implementation | N/A | NOT APPLICABLE | Future/optional scope; not counted as launch blocker. |
| French-first mobile UI | French customer/provider journeys | No UI or localization resources | No | NOT IMPLEMENTED | No frontend/mobile source. |
| Arabic/RTL | Future feature, not MVP gate | No UI | N/A | NOT APPLICABLE | Explicitly deferred by audit scope. |
| Distance/radius search | Future feature, not MVP gate | No geo implementation | N/A | NOT APPLICABLE | City/region search is MVP; distance search deferred. |
| Offline/network recovery | Graceful mobile behavior under interruption | No mobile networking layer | No | NOT IMPLEMENTED | No mobile app or network tests. |
| Privacy/account deletion | Clear disclosures, data rights/deletion process | No product disclosure/deletion flow found | No | NOT IMPLEMENTED | No frontend or account lifecycle API/docs. Legal applicability itself requires review. |
| Automated test suite | Unit/API/mobile integration/regression coverage | Test dependencies only; no project tests | `manage.py test` found 0 tests | BLOCKED | No test source/configuration. |
| Backend production runtime | Reproducible PostgreSQL-backed production config | Production config references PostgreSQL; driver/config mismatch | Check failed before DB connect | BLOCKED | `production.py:12-21`; no psycopg dependency; missing driver error. |
| Android release build | Reproducible signed AAB/APK | No Gradle project, manifest, signing config | Cannot execute | NOT IMPLEMENTED | No Android files in repository. |
| iOS release build | Reproducible signed archive/IPA | No Xcode project, bundle ID, signing setup | Cannot execute | NOT IMPLEMENTED | No iOS files in repository. |

## Journey status

### Customer: registration → login → search → profile → booking → status

**NOT IMPLEMENTED.** Registration and token routes are absent; no provider listing/profile entity exists; no search endpoint/client; no booking model or status flow exists.

### Provider: registration → profile → approval → listing → request → accept/reject

**NOT IMPLEMENTED.** Provider module has no model, routes, approval status, listing moderation, booking inbox, or request state transitions.

### Administrator: login → approve provider/listing → moderate → audit

**PARTIALLY IMPLEMENTED.** Django Admin is mounted and the custom user model is registered. No marketplace entities or moderation screens exist. Only unauthenticated redirect behavior was tested.
