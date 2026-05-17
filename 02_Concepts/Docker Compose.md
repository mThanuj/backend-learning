---
date: 2026-05-17 17:08
tags:
  - type/concept
---
# Docker Compose

## 💡 TL;DR
- A tool to run multiple containers together.
- If we had to run multiple containers like:
	- postgres
	- redis
	- springboot-app etc.
	 then, we have to run multiple commands to achieve this.
- We also can configure network, storage, ports, envs and much more with compose files.
- Syntax:
	- services: These are the containers to run.
	- build: The location of the DockerFile of that particular container.
	- image: Use an existing image rather than our own DockerFile.
	- ports: The ports to use in the network.
		- Format: HOST:CONTAINER
	- environment: Environment Variables.

## 🛠️ Syntax / Code Example
```DockerCompose
services:
  app:
    build: .
    ports:
      - "8080:8080"
    environment:
      SPRING_DATASOURCE_URL: jdbc:postgresql://db:5432/mydb
      SPRING_DATASOURCE_USERNAME: postgres
      SPRING_DATASOURCE_PASSWORD: password
    depends_on:
      - db
  db:
    image: postgres
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
    ports:
      - "5432:5432"
```

## 🔗 Related Concepts
- [[Docker Container]]