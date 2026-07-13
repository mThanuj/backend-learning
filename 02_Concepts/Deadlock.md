---
date: 2026-07-13 07:08
tags:
  - type/concept
---
# Deadlock

## 💡 TL;DR
- A deadlock occurs when two or more threads wait for each other indefinitely and none of them can proceed.

## 🛠️ Syntax / Code Example
```java
public class DeadlockExample {
	private static final Object LOCK1 = new Object();
	private static final Object LOCK2 = new Object();
	
	public static void main(String[] args) {
		Thread t1 = new Thread(() -> {
			synchronized(LOCK1) {
				System.out.println("Thread 1 aquired LOCK1");
				
				try {
					Thread.sleep(100);
				} catch (Exception e) {
					System.err.println(e.getMessage());
				}
				
				synchronized(LOCK2) {
					System.out.println("Thread 1 aquired LOCK2");
				}
			}
		});
		
		Thread t2 = new Thread(() -> {
			synchronized(LOCK2) {
				System.out.println("Thread 2 aquired LOCK2");
				
				try {
					Thread.sleep(100);
				} catch (Exception e) {
					System.err.println(e.getMessage());
				}
				
				synchronized(LOCK1) {
					System.out.println("Thread 2 aquired LOCK1");
				}
			}
		});
		
		t1.start();
		t2.start();
	}
}
```

## 🔗 Related Concepts

- 