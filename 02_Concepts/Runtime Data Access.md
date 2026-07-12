---
date: 2026-07-12 08:49
tags:
  - type/concept
---
# Runtime Data Access

## 💡 TL;DR
- Heap:
	- Shared by all threads.
	- It stores all objects and arrays.
	- Since all threads access heap, we need synchronization.
	- Heap Generations:
		- Young Generation:
			- Eden: New objects are created in here.
			- Survivor 0
			- Survivor 1
			- ...
		- Old Generation
		- Objects that survive multiple garbage collections move upward in 'Survivor X' category.
		- Then after garbage collection, sent to Old Generation.
- Stack:
	- One per thread.
	- When a method is called, a 'Stack Frame' is created in the stack for it.
	- Stack Frame contains:
		- Local Variables
		- Method parameters
		- Return address
		- 
	- After the method returns, the 'Stack Frame' is removed.
- Metaspace:
	- Shared by all threads.
- PC Register:
	- One per thread.
- Native Method Stack:
	- One per thread.

## 🛠️ Syntax / Code Example
```java

```

## 🔗 Related Concepts

- [[JVM Architecture]]