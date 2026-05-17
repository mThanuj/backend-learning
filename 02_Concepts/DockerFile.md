---
date: 2026-05-17 17:07
tags:
  - type/concept
---
# DockerFile

## 💡 TL;DR
- These are the instructions given to docker on how to build an image.
- Example:
	- Start from java.
	- Copy app.
	- Run app.
- Syntax:
	- FROM: Start from an image that already has this software installed.
		- ubuntu
		- node
		- python
		- openjdk
		- postgres etc.
	- WORKDIR: Sets a working directory inside the container.
	- COPY: Copies files from your computer into the container.
		- COPY src dst
	- EXPOSE: Expose this port(s) to the outside of the container.
	- RUN: Execute this image while building the image.
	- CMD: Default command to run once the container starts.

## 🛠️ Syntax / Code Example
```DockerFile
FROM openjdk:21

WORKDIR /app

COPY target/myapp.jar app.jar

EXPOSE 8080

CMD ["java", "-jar", "app.jar"]
```

	Go to the directory we have the DockerFile in and run this command:  
```bash
docker build -t my-app .
```

## 🔗 Related Concepts
- [[Docker Image]]