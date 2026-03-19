---
description: Safe and downtime-free guide for modifying active database table structures.
---

# Zero-Downtime Migration Workflow

If requested to modify a database table with high live traffic (such as changing column types, renaming columns, or splitting tables), always use the **Expand → Migrate → Contract** pattern. Execute the following steps sequentially:

## 0. CONTEXT RETRIEVAL (JIT)
- [ ] Verify Binary Oratory compliance. IF unsure, use `grep_search` on `@agent_protocols.md`.
- [ ] Activate `@skill-db-expert` if dealing with deep Postgres/Supabase optimization.
- [ ] Ensure all local changes in `.agents` are finalized.

- [ ] **1. Phase 1 (Expand)**: 
   - Create a SQL/Prisma migration file that adds new columns/tables (must be nullable).
   - *Application*: Modify the application code so it always writes data to BOTH the OLD and NEW columns simultaneously.
   - Deploy Phase 1 to production.

- [ ] **2. Phase 2 (Migrate)**:
   - Create a background/worker script to *backfill* old data into the new columns. 
   - Ensure chunking is used to avoid locking the table for too long.
   - Verify that all old rows now have values in the new column.

- [ ] **3. Phase 3 (Contract)**:
   - *Application*: Modify the application's read/write logic so it now ONLY uses the NEW column.
   - Deploy this new read logic to production.
   - After stabilization, create the final SQL/Prisma migration to DROP the old column or change it to NOT NULL (if necessary).

**Golden Rule:** NEVER run `ALTER TABLE ... ADD COLUMN ... NOT NULL` without a default value on large tables. This will cause an instant table lock down.