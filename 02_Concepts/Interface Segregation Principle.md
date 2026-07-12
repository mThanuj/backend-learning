---
date: 2026-07-12 12:52
tags:
  - type/concept
---
# Interface Segregation Principle

## 💡 TL;DR
- Don't force classes to implement methods they don't need.
- For example:
	- If I had a parent class 'Worker' which has methods (work, eat, sleep).
	- I cannot use this class to extend into a 'Robot' class as they dont 'eat' or 'sleep'.
	- So, we can create Sleepable, Workable, Eatable classes and use only what is needed.

## 🛠️ Syntax / Code Example
```java

```

## 🔗 Related Concepts

- 