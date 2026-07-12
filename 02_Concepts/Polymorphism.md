---
date: 2026-07-12 12:37
tags:
  - type/concept
---
# Polymorphism

## 💡 TL;DR
- One interface, many implementations.
- Types of polymorphism:
	- Method Overloading (Compile-Time): Multiple signatures to the same method name.
	- Method Overriding (Run-Time): Overriding a method from its parent class and giving different implementations.

## 🛠️ Syntax / Code Example
```java
Payment payment;

// today
payment = new UpiPayment();

// tomorrow
payment = new CreditCardPayment();

// no matter which class is implemented, it runs
payment.pay();
```

## 🔗 Related Concepts

- 