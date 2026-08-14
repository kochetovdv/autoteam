# Privacy: the regime is derived from jurisdiction

A reference of regimes for the map. A regime is not assigned "out of habit" — it follows from where the subjects and the processing are.

Personal data is a process, not a checkbox at the end. Skill: `autoteam-security` + checklist `templates/privacy-checklist.md`.

## The jurisdiction rule

1. What data (categories: account, payment, geolocation, biometrics…).
2. Where the subjects are (residents of which countries) and where storage/processing happens.
3. Which regime applies. Do **not** slap a single national regime onto the whole world.

| Regime | When |
|-------|--------|
| **GDPR** (EU/EEA and often "offering services in the EU") | subjects in the EU or targeting the EU |
| **CCPA/CPRA** | subjects in California, applicability thresholds by revenue/volume |
| **UK GDPR** | subjects in the United Kingdom |
| National regimes (LGPD, PIPL, local personal data laws) | per the subjects' and operator's country — record it in the map, do not invent full compliance |

Multiple markets — multiple regimes in one map. The common baseline is the stricter one: whatever requires explicit consent / localization / deletion — do it for the corresponding user segment.

## The map (artifact)

`docs/privacy/jurisdiction-map.md` in the **product** (not in autoteam):

- data categories;
- legal bases (consent, contract, legitimate interest — in your own words);
- storage and retention period;
- who has access (roles);
- cross-border transfers;
- subject rights (access, deletion, withdrawal) — which screens/APIs cover them;
- applicable regimes as a list.

No map — estimation and architecture flag the risk; don't block UI polish on other screens, but **do block** releasing the collection of new personal data.

## Minimum in code

- Don't log tokens, passwords, full card numbers, raw identity documents.
- Secrets are not in git.
- Deletion/export is a task with an owner, not "later".
