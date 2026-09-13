<!--
number: 15
part: Part III — Developer environment
description: Postgres, MySQL, SQLite, Redis, MongoDB and friends on a Mac — Homebrew services vs containers vs Postgres.app, GUI clients, local HTTPS and custom domains, and a sane local-dev workflow.
-->
# Databases & local development services

Two philosophies for local services: **install natively via Homebrew** (fastest, always on, shares your filesystem) or **run in containers** (isolated, version-per-project, throwaway). Both are fine; the mistake is mixing them for the *same* service and then wondering which Postgres is answering on 5432.

## Which approach

| | Homebrew service / Postgres.app | Containers (OrbStack/Docker Compose) |
|---|---|---|
| Speed | Native; no VM overhead; fastest for heavy queries and large imports | Very fast on OrbStack; a little file-share overhead for bind-mounted data |
| Versions | One major version per formula (`postgresql@17`); switching is fiddly | Any version per project, side by side, trivially |
| Isolation | Shared server, many databases | Each project its own server; `down -v` wipes it |
| Always-on cost | Runs at login if you `brew services start` — small battery/memory cost | Only when the project is up |
| Team parity | Differs from CI/production | Same image as CI/production |
| Recommendation | **Solo/student with one Postgres for everything; SQLite; Redis** | **Anything with a `compose.yaml`; multiple versions; team projects** |

Many developers end up with: **SQLite natively** (it's a library, not a server), **one Homebrew Postgres for scratch work**, and **Compose for real projects**.

## PostgreSQL

### Native (Homebrew)

```sh
brew install postgresql@17
brew services start postgresql@17         # runs as your user, data in /opt/homebrew/var/postgresql@17
# keg-only: put its bin on PATH (Homebrew prints the exact line)
echo 'export PATH="/opt/homebrew/opt/postgresql@17/bin:$PATH"' >> ~/.zshrc
createdb $(whoami)                        # so plain `psql` connects
psql -c "select version();"
```

Your macOS username is a superuser with no password (local trust auth) — fine for a laptop, never for anything reachable. Create per-project roles anyway to mirror production: `createuser -P app && createdb -O app app_dev`. Config: `/opt/homebrew/var/postgresql@17/postgresql.conf`; logs: `/opt/homebrew/var/log/postgresql@17.log`. Upgrade majors with `brew postgresql-upgrade-database` (back up first).

**Postgres.app** (postgresapp.com, free) is the friendliest native option: a menu bar app that bundles several major versions with PostGIS, click to start/stop, no service management. Add `/Applications/Postgres.app/Contents/Versions/latest/bin` to PATH for `psql`. Great for students.

**Postgres client only** (talking to a container or cloud DB): `brew install libpq` (keg-only) and add its bin to PATH, or `brew link --force libpq`. **pgcli** (`uv tool install pgcli`) is a far nicer interactive client than `psql` (autocomplete, syntax highlighting).

### In a container

The Compose snippet in Chapter 13. One-off: `docker run -d --name pg -e POSTGRES_PASSWORD=pg -p 5432:5432 -v pgdata:/var/lib/postgresql/data postgres:17`. Use a **named volume** (not a bind mount) for the data directory — bind-mounted Postgres data on macOS is slower and has had permission quirks. If you also run a Homebrew Postgres, map the container to another port (`5433:5432`) or stop the service.

### Extensions

PostGIS, pgvector, TimescaleDB etc.: `brew install postgis pgvector` (built against the Homebrew formula), or use images that bundle them (`pgvector/pgvector:pg17`, `timescale/timescaledb`, `postgis/postgis`). Postgres.app bundles PostGIS and pgvector.

## MySQL / MariaDB

`brew install mysql` (9.x) or `mysql@8.4` (LTS), `brew services start mysql`, `mysql_secure_installation`. MariaDB is `brew install mariadb`. In containers: `mysql:8.4` / `mariadb:11` — set `MYSQL_ROOT_PASSWORD`. Client-only: `brew install mysql-client`. **mycli** for a better shell.

## SQLite

Already on macOS (`/usr/bin/sqlite3`), but Apple's build is older and lacks some extensions; `brew install sqlite` installs a current version keg-only (`$(brew --prefix sqlite)/bin/sqlite3`). **litecli** (`uv tool install litecli`) for a friendlier shell; **DB Browser for SQLite** or **TablePlus** for a GUI; **Datasette** to explore a SQLite file in the browser. **DuckDB** (`brew install duckdb`) is SQLite's analytical sibling — the fastest way to query CSV/Parquet files from the shell, and it reads Postgres/MySQL too. For 90% of coursework and side projects SQLite (or Turso/libSQL) is the right database.

## Redis, Valkey & friends

`brew install redis` (Redis 8, back under an OSI licence) or `brew install valkey` (the Linux Foundation fork); `brew services start redis`; `redis-cli ping`. Container: `redis:8-alpine` / `valkey/valkey`. **RedisInsight** or **Another Redis Desktop Manager** for a GUI. **Dragonfly** and **KeyDB** are drop-in alternatives if a project uses them.

## MongoDB

MongoDB's server isn't in Homebrew core (licence): `brew tap --trust mongodb/brew && brew install mongodb-community`, `brew services start mongodb-community`; or the `mongo:8` container — the usual choice. **MongoDB Compass** (GUI) and `mongosh` (`brew install mongosh`).

## Everything else, briefly

| Need | Native | Container image |
|---|---|---|
| Elasticsearch / OpenSearch | `brew install opensearch` | `opensearchproject/opensearch`, `elasticsearch:9` (needs `-e discovery.type=single-node`, 1–2 GB RAM) |
| Kafka | `brew install kafka` (KRaft mode, no ZooKeeper) | `apache/kafka`, or **Redpanda** (`redpandadata/redpanda`) — lighter |
| RabbitMQ | `brew install rabbitmq` | `rabbitmq:4-management` |
| NATS | `brew install nats-server` | `nats` |
| ClickHouse | `brew install clickhouse` | `clickhouse/clickhouse-server` |
| Neo4j | `brew install neo4j` | `neo4j` |
| InfluxDB / Prometheus / Grafana | brew formulae | `prom/prometheus`, `grafana/grafana` |
| MinIO (S3) | `brew install minio` | `minio/minio` |
| Mailpit (catch dev email) | `brew install mailpit` | `axllent/mailpit` — point SMTP at `localhost:1025`, read at `:8025` |
| Supabase (Postgres + auth + storage + realtime) | — | `supabase start` (uses Docker) |
| Firebase emulators | `npm i -g firebase-tools` via mise | — |
| LocalStack (AWS) | `brew install localstack` | `localstack/localstack` |

All official images above have arm64 builds. Where a vendor image is amd64-only, see the multi-arch notes in Chapter 13.

## GUI database clients

| Client | Price | Notes |
|---|---|---|
| **TablePlus** | Free (2 tabs/2 connections limit) / $89 one-time / in Setapp | Native, fast, supports Postgres/MySQL/SQLite/Redis/Mongo/MSSQL/… The Mac default. |
| **DBeaver Community** | Free, OSS | Java, heavier, supports everything incl. big-data sources; ER diagrams. |
| **DataGrip** | JetBrains; free for students | Best SQL editor/intellisense; also inside IntelliJ Ultimate/PyCharm Pro. |
| **Postico 2** | Free tier / $60 | Postgres-only, lovely. |
| **Beekeeper Studio** | Free (Community) / paid | Electron, cross-platform, pleasant. |
| **pgAdmin 4** | Free | Postgres official; web UI; admin-focused. |
| **Sequel Ace** | Free, OSS | MySQL/MariaDB only; native; the successor to Sequel Pro. |
| **Azure Data Studio** / **SSMS** | — | Deprecated (ADS, Feb 2026) / Windows only — use the **MSSQL extension for VS Code** or DBeaver for SQL Server. |
| **Compass**, **RedisInsight** | Free | Vendor GUIs for Mongo and Redis. |
| **Drizzle Studio**, **Prisma Studio** | Free | ORM-aware browsers for JS/TS projects. |

## Local HTTPS and custom domains

Browsers treat `localhost` as a secure context, so plain `http://localhost:3000` works for most features (service workers, camera, WebCrypto). You need HTTPS locally when: testing OAuth callbacks that require `https://`, Secure cookies with `SameSite=None`, HTTP/2 or HTTP/3, or multiple subdomains (`app.myproject.test`, `api.myproject.test`).

- **mkcert** (`brew install mkcert nss && mkcert -install`) creates a local CA trusted by Safari/Chrome/Firefox, then `mkcert myproject.test "*.myproject.test" localhost 127.0.0.1 ::1` gives you cert files for your dev server or reverse proxy.
- **Caddy** (`brew install caddy`) as a local reverse proxy: a 3-line `Caddyfile` (`myproject.test { reverse_proxy localhost:3000 }`) with automatic local TLS via its internal CA (`caddy trust` once). **nginx** or **Traefik** if you prefer.
- **Custom domains**: `.test` is reserved for exactly this (never `.dev` — it's a real TLD with HSTS preloaded, so `http://foo.dev` breaks). Add entries to `/etc/hosts` (`sudo nvim /etc/hosts`; `127.0.0.1 myproject.test api.myproject.test`), or run `dnsmasq` (`brew install dnsmasq`) with `address=/.test/127.0.0.1` and a resolver file in `/etc/resolver/test` for wildcard resolution. **OrbStack** gives every container `name.orb.local` with HTTPS for free, which covers the common case.
- Tools that do all of this for you: **Laravel Herd** (PHP), **Laravel Valet**, **DDEV** (Docker-based, any stack, automatic `*.ddev.site` + HTTPS), **Lando**.

## Environment variables and secrets for local services

- Each project gets a `.env` (gitignored) with `DATABASE_URL`, `REDIS_URL`, etc., loaded by `mise` (`_.file = ".env"`), `direnv`, or the framework's dotenv loader. Commit `.env.example`.
- Local passwords can be trivial (`postgres`/`postgres`) — they're bound to `localhost` — but **never reuse a real password** for a local service; it ends up in a screenshot or a repo eventually.
- Bind services to `127.0.0.1`, not `0.0.0.0`, unless you need LAN access (mobile device testing); OrbStack/Docker publish on localhost by default, Homebrew Postgres listens on localhost by default.
- Check what's listening occasionally: `lsof -iTCP -sTCP:LISTEN -n -P | grep -v 127.0.0.1` shows anything exposed to the network.

## A sane local-dev workflow

1. `mise.toml` pins runtimes and loads `.env`; `mise run dev` starts the app.
2. `compose.yaml` runs *only* stateful services (db, cache, queue, mail catcher); `docker compose up -d` once per session, `down` when done.
3. The app runs natively for hot reload and the debugger; it talks to services on `localhost:<port>`.
4. Migrations and seeds are scripts (`mise run db:reset`), so a broken database is a 10-second fix, not a support ticket.
5. A `README` "Local setup" section is three commands. If it's longer, automate the rest.

## Data and disk hygiene

- Postgres/MySQL data under `/opt/homebrew/var` is in your Time Machine backup (fine — it's usually small); Docker named volumes live inside the VM image (excluded, see Chapter 17) — **dump anything you'd miss** (`pg_dump`, `mysqldump`) before `docker system prune --volumes`.
- Large datasets for coursework (CSV dumps, ML corpora): keep them outside the repo and outside iCloud Drive (`~/Developer/data`), and consider an external SSD; Spotlight-exclude the folder (Chapter 4).
- `brew services list` — stop what you're not using this term; every running service costs memory and battery.
