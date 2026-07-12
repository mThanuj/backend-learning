---
date: 2026-07-12 12:30
tags:
  - type/concept
---
# Encapsulation

## 💡 TL;DR
- Used to bundle data and methods together.
- Also to hide internal implementation.

## 🛠️ Syntax / Code Example
```java
class BankAccount {
    private double balance;

    public void deposit(double amount) {
        balance += amount;
    }

    public double getBalance() {
        return balance;
    }
}
```

## 🔗 Related Concepts

- 