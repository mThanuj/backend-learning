---
date: 2026-07-12 12:32
tags:
  - type/concept
---
# Abstraction

## 💡 TL;DR
- Abstraction exposes only essential behavior while hiding implementation details.
- You only know to use the method, but not how its internally implemented.
- For Example:
	- You know how to drive a car, but we dont need to know how the fuel injection works.
	- Another example is, in Spring Boot, whenever we want to save a entity using a repository we do Repository.save(entity), but we dont care or know how hibernate is generatin

## 🛠️ Syntax / Code Example
```java
interface Payment {

    void pay();

}

class CreditCardPayment implements Payment {
	...
}

class UpiPayment implements Payment {
	...
}

payment.pay(); // user doesnt need to know how payment is done, he only uses it
```

## 🔗 Related Concepts

- 