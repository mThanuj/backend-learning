---
date: 2026-05-16 10:28
tags:
  - type/concept
---
# Liquibase

## 💡 TL;DR
- Liquibase is a database version control tool.
- We define DB changes in changelogs (XML, JSON, YAML or SQL).
- Liquibase tracks which changes are already ran using these tables:
	- DATABASECHANGELOG
	- DATABASECHANGELOGLOCK
- Each change is written in a changeset with:
	- id
	- author
	- changes
- Main purpose:
	- Keep DB schema consistent across all environments (dev / test / prod).
	- Avoid manual SQL execution.
	- Make DB changes trackable.

## 🛠️ Syntax / Code Example
```xml
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog
    xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:ext="http://www.liquibase.org/xml/ns/dbchangelog-ext"
    xmlns:pro="http://www.liquibase.org/xml/ns/pro"
    xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-latest.xsd
                        http://www.liquibase.org/xml/ns/dbchangelog-ext http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-ext.xsd
                        http://www.liquibase.org/xml/ns/pro http://www.liquibase.org/xml/ns/pro/liquibase-pro-latest.xsd">
    <changeSet id="1" author="thanuj">
        <createTable tableName="users">
            <column name="id" type="INT" autoIncrement="true">
                <constraints primaryKey="true" nullable="false"/>
            </column>
            <column name="username" type="VARCHAR(50)">
                <constraints nullable="false" unique="true"/>
            </column>
            <column name="password" type="VARCHAR(255)">
                <constraints nullable="false"/>
            </column>
        </createTable>
        <createIndex
            tableName="users"
            indexName="idx_users_username">
            <column name="username"/>
        </createIndex>
    </changeSet>
</databaseChangeLog>
```

```properties
spring.liquibase.change-log=location-of-the-file
```

## 🔗 Related Concepts
- 