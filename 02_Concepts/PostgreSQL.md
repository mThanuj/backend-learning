---
date: 2026-05-17 16:43
tags:
  - type/concept
---
# PostgreSQL

## 💡 TL;DR
- It is a advanced version of MySQL with complex SQL schemas, analytics, data integrity and many more.

## 🛠️ Syntax / Code Example
```bash
docker run --name postgres-db \
-e POSTGRES_USER=root \
-e POSTGRES_PASSWORD=root \
-e POSTGRES_DB=db_name \
-p 5432:5432 \
-v postgres_data:/var/lib/postgresql/data \
-d postgres
```

## 🔗 Related Concepts
- 