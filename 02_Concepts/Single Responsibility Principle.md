---
date: 2026-07-12 12:42
tags:
  - type/concept
---
# Single Responsibility Principle

## 💡 TL;DR
- A class should have only one reason to change.
- For example:
	- In a springboot application we have:
		- Controller
		- Service
		- Repository
	- where, each layer has a single responsibility.

## 🛠️ Syntax / Code Example
```java
// ❌ Bad
class UserService {
    saveUser();
    sendEmail();
    generatePDF();
}

// ✅ Good
UserService      -> User logic
EmailService     -> Emails
PdfService       -> PDF generation
```

## 🔗 Related Concepts

- 