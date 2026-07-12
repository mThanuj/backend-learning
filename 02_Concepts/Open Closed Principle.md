---
date: 2026-07-12 12:46
tags:
  - type/concept
---
# Open Closed Principle

## 💡 TL;DR
- Open for extension, closed for modification.
- If we want to add any features, we are able to just extend it and do it. 
- We donot need to modify the existing features everytime.

## 🛠️ Syntax / Code Example
```java
interface Payment {
    pay();
}

class CreditCardPayment implements Payment {
	...
}

class UpiPayment implements Payment {
	...
}
```

## 🔗 Related Concepts

- 