---
date: 2026-05-17 09:16
tags:
  - type/concept
---
# Constraint

## 💡 TL;DR
- It is a database rule that is applied to a table/column to control what data is allowed.
- It helps maintain data integrity.
- Mostly used constraints are:
	- Primary Key
	- Foreign Key
	- Not Null
	- Unique
	- Check
	- Default
	- IDENTITY

## 🛠️ Syntax / Code Example
```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT
);

age INT CHECK (age >= 18);
```

## 🔗 Related Concepts
- [[Primary Key]]
- [[Foreign Key]]