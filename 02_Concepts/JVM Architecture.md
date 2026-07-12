---
date: 2026-07-12 08:40
tags:
  - type/concept
---
# JVM Architecture

## 💡 TL;DR
- Major components of JVM:
	- Class Loader:
		- Loads the \*.class files into memory.
	- Bytecode Verifier:
		- Checks whether the bytecode is valid.
		- Verifies things like:
			- Stack corruption.
			- Invalid memory access.
			- Illegal instructions.
			- Bytecode format.
	- Runtime Data Access:
		- Heap
		- Stack
		- Metaspace
		- PC Register
		- Native Method Stack
	- Execution Engine:
		- Interpreter:
			- Reads bytecode.
			- One instruction at a time.
		- JIT Compiler
			- Instead of interpreting repeatedly, observes patterns.
			- If a method is called 'N' times, it doesnt interpret again and again, but converts it into machine code and reuses it.
		- Garbage Collector

## 🛠️ Syntax / Code Example
```java

```

## 🔗 Related Concepts

- [[Runtime Data Access]]