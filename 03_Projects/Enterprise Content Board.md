---
date: 2026-05-16
tags:
  - type/project
  - status/active
---
# Enterprise Content Board

## Core Purpose
- A website where the people in an enterprise can create boards and add pins (images) into those boards for idea sharing.

## Tech Stack
- Frontend: Angular 15
- Backend: [[Spring Boot]] 4.0.6
- Database / DevOps: H2 (development & testing) / PostgreSQL (deployment), Docker
- Third-Party Integrations: Liquibase

## External Links
- Repository: https://github.com/mThanuj/enterprise-content-board

## Architecture & Decisions
- Use Liquibase for managing database via code.
- Use Redis and @Cacheable for heavily accessed endpoints.
- Use TestContainers for PostgreSQL testing.
- Spin up RabbitMQ for efficient image upload processing.