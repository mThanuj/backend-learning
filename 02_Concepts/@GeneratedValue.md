---
date: 2026-05-17 09:33
tags:
  - type/concept
  - type/annotations
---
# @GeneratedValue

## 💡 TL;DR
- It tells the JPA how the primary key should be generated automatically.
- This takes a option strategy through which we can select the type of primary key we want and how we want the database to generate it automatically.

## 🛠️ Syntax / Code Example
```java
@Entity
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
}
```

## 🔗 Related Concepts
- [[GenerationType]]