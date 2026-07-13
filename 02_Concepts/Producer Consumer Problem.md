---
date: 2026-07-13 06:24
tags:
  - type/concept
---
# Producer Consumer Problem

## 💡 TL;DR
- 

## 🛠️ Syntax / Code Example
```java
import java.util.*;

class Buffer {
	private final Queue<Integer> queue;
	private final int capacity;
	
	Buffer(int capacity) {
		this.queue = new LinkedList<>();
		this.capacity = capacity;
	}
	
	public synchronized void produce(int value) throws Exception {
		while(queue.size() == capacity) {
			wait();
		}
		
		queue.add(value);
		notifyAll();
	}
	
	public int consume() throws Exception {
		while(queue.isEmpty()) {
			wait();
		}
		
		queue.pop();
		notifyAll();
	}
}
```

## 🔗 Related Concepts

- 