# Grafana Cloud vs. Axiom — log shipping options

Infra note comparing free options to ship this server's logs off-box. Both work off a single free account and a lightweight shipper container; the difference is log-only vs. full observability stack.

## The two options

### Axiom — log-first, generous free quota
Log storage and search built for volume. `Vector` or `Fluent Bit` tails container/server logs and ships them straight to Axiom. Query language is fast and log-native.

- Best if the job is just: collect logs, search them later.
- No real metrics, dashboards, or alerting layer — it's not trying to be one.
- Setup is a single shipper config pointed at an API token.

### Grafana Cloud — logs + metrics + dashboards
Logs go through `Loki`, shipped by `Alloy` or `Promtail`. The same free account also gets Prometheus metrics and Grafana dashboards, so container CPU/RAM and logs live side by side.

- Best if you want a real dashboard for the server over time, not just a log tail.
- Alerting on log patterns or metric thresholds is built in.
- Slightly more moving parts to configure than a single shipper.

## Free tier comparison (as of 2026)

| | Axiom | Grafana Cloud |
|---|---|---|
| Log ingest | 500 GB / month | 50 GB / month |
| Retention | 30 days | 14 days |
| Metrics included | No | Yes — 10k Prometheus series |
| Dashboards | Basic query UI | Full Grafana dashboards |
| Alerting | Limited | Yes, on logs + metrics |
| Shipper for Docker | Vector / Fluent Bit | Grafana Alloy / Promtail |
| Setup effort | Low | Low–medium |

## Recommendation

**Just want to search log output when something breaks?** Use Axiom. The free ingest quota is 10x larger, retention is longer, and the shipper config is a five-minute job.

**Want an actual dashboard for the server** — CPU, memory, container health, and logs in one place, with alerts — Grafana Cloud is worth the slightly heavier setup, since the free tier already includes metrics and Grafana itself.

## For this Dockge host specifically

Either option reads container logs the same way — mount `/var/lib/docker/containers` or use the Docker log driver, point the shipper at it, done. Starting with Axiom first for zero-friction log capture; can add Grafana Cloud later if dashboards become worth having.

## Axiom setup (this repo)

Stack: `stacks/axiom-vector/` — a Vector container that tails all Docker container logs via the Docker log driver and ships them to Axiom.

Requires an Axiom account, a dataset, and an API token, set in `stacks/axiom-vector/.env` (not committed).
