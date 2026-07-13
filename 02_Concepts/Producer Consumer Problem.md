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
			System.out.println("Buffer full -> Producer waiting...");
			wait();
		}
		
		queue.add(value);
		System.out.println("Produced: " + value);
		
		notifyAll();
	}
	
	public synchronized int consume() throws Exception {
		while(queue.isEmpty()) {
			System.out.println("Buffer empty -> Consumer waiting...");
			wait();
		}
		
		int value = queue.remove();
		System.out.println("Consumed: " + value);
		
		notifyAll();
	}
}

class Producer extends Thread {
	priva
}
```

## 🔗 Related Concepts

- 