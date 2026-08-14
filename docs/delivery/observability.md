# Observability

When mandatory (otherwise an L2+ release fails in "we can't see it" mode):

- an incoming request has an id visible in the API log and, where possible, in the UI error;
- a 5xx error and an outbound-call timeout are logged with code and entity, without secrets;
- for background work: "is the worker alive", last successful job, queue stall.

Metrics: latency, errors, queue/pool saturation. Cross-process tracing — if a request hops API→worker→DB and incidents can't be fixed without it.

Dashboard and alerts — per product; the minimum is grep by `request_id` in the runbook.
