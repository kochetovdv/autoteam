# Resource registry

Everything the product needs besides code and money: accounts, access, infrastructure, data, human actions. Money — `autoteam-budget`; here — things and access. Secret values never enter this file — only a pointer to where they live.

| ID | Type | Resource | Status | Pointer / owner | Expiry | Blocks packages |
|----|-----|--------|--------|----------------------|---------------|------------------|
| R-001 | account \| access \| infrastructure \| data \| human action | | have \| needed \| requested (date) | | | |

Rules:

- A missing resource does not stop the cycle: the package is marked `Blocked-by-resource`, the rest keeps moving.
- Creating an account / paying / passing identity verification — only the human can do that; such rows go into the human action queue (the cycle-start digest) with the consequence made transparent: "without R-00X, package Y stalls after checkpoint Z".
- A resource with a limit shared across products (LLM account, hosting account) is marked "shared"; dividing the shared — the human's call.
- The "expiry" field (domain, certificate, plan) is checked by the operations lens at acceptance.
- Secret created — the registry holds a pointer to the vault; the value goes neither into git nor into chat (`autoteam-security`).
