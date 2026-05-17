---
date: 2026-05-17 09:38
tags:
  - type/concept
---
# GenerationType

## 💡 TL;DR
- There are basically 4 generation types. They are:
	- IDENTITY: Database auto-increments ids. 1,2,3...
	- SEQUENCE: Similar to IDENTITY but better performance in PostgreSQL/Oracle etc.
	- AUTO: Hibernate decides automatically.
	- UUID: Generated UUIDs. Useful for APIs and distributed systems.

## 🛠️ Syntax / Code Example
```java
@GeneratedValue(strategy = GenerationType.IDENTITY)

// OR

@GeneratedValue(strategy = GenerationType.SEQUENCE)

// OR

@GeneratedValue(strategy = GenerationType.AUTO)

// OR

@GeneratedValue(strategy = GenerationType.UUID)
```

## 🔗 Related Concepts
- 