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

class ProducerConsumerProblem {
	Queue<Integer> queue = new LinkedList<>();
	int capacity = 0;
	
	public void produce(int value) throws Exception {
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