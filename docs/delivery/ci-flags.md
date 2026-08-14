# CI and feature flags

## CI

Minimum, if there is git hosting: build, unit, contract schema lint if a contract exists. No CI — the human inspects evidence in the handoff; the agent does not lie about a "green pipeline".

Do not inflate the OS matrix. First, the tests that catch contract regressions and race conditions.

## Feature flags

A flag comes with an owner and a removal date. An eternal flag = a branch in the code. Do not use a flag instead of a data migration. Releasing a flag is releasing behavior: who sees it, how to roll back.
