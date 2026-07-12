---
date: 2026-07-12 12:30
tags:
  - type/concept
---
# Encapsulation

## 💡 TL;DR
- Encapsulation is the process of wrapping data and methods into a single unit while restricting direct access to the internal state using access modifiers.
- For example:
	- In a real spring boot project, UserService does not expose the repository directly, but uses its methods to modify the data.

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