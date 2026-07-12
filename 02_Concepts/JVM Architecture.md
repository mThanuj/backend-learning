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
		- Interpreter
		- JIT Compiler
		- Garbage Collector

## 🛠️ Syntax / Code Example
```java

```

## 🔗 Related Concepts

- [[JVM]]