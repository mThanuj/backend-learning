---
date: 2026-07-12 12:54
tags:
  - type/concept
---
# Dependency Inversion Principle

## 💡 TL;DR
- Depend on abstractions, not concrete implementations.

## 🛠️ Syntax / Code Example
```java
❌
class UserService {

    MySqlRepository repo = new MySqlRepository();

}

✅
interface UserRepository

// and then make MySqlRepository or MongoRepository to be extended with UserRepository.
```

## 🔗 Related Concepts

- 