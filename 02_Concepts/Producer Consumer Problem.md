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
        this.queue = new LinkedList<Integer>();
        this.capacity = capacity;
    }
    
    public synchronized void produce(int value) throws Exception {
        while(queue.size() == capacity) {
            System.err.println("Buffer full -> Producer waiting...");
            wait();
        }
        
        queue.add(value);
        System.out.print("Produced: " + value + " | ");
        System.out.println(this.queue);
        
        notifyAll();
    }
    
    public synchronized void consume() throws Exception {
        while(queue.isEmpty()) {
            System.err.println("Buffer empty -> Consumer waiting...");
            wait();
        }
        
        int value = queue.remove();
        System.out.print("Consumed: " + value + " | ");
        System.out.println(this.queue);
        
        notifyAll();
    }
}

class Producer extends Thread {
    private final Buffer buffer;
    
    Producer(Buffer buffer) {
        this.buffer = buffer;
    }
    
    @Override
    public void run() {
        int value = 1;
        
        try {
            while(true) {
                buffer.produce(value++);
                Thread.sleep(100);
            }
        } catch(Exception e) {
            System.err.println(e.getMessage());
        }
    }
}

class Consumer extends Thread {
    private final Buffer buffer;
    
    Consumer(Buffer buffer) {
        this.buffer = buffer;
    }
    
    @Override
    public void run() {
        try {
            while(true) {
                buffer.consume();
                Thread.sleep(300);
            }
        } catch(Exception e) {
            System.err.println(e.getMessage());
        }
    }
}

public class ProducerConsumer {
    public static void main(String[] args) {
        Buffer buffer = new Buffer(5);
        
        Producer producer = new Producer(buffer);
        Consumer consumer = new Consumer(buffer);
        
        producer.start();
        consumer.start();
    }
}
```

## 🔗 Related Concepts

- 