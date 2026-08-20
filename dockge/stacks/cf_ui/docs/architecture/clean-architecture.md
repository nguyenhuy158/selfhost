# Clean Architecture Overview

## Introduction

This project follows Clean Architecture principles to ensure maintainability, testability, and separation of concerns. Clean Architecture organizes code into concentric layers, each with specific responsibilities and dependencies.

## The Four Layers

### 1. Entities (Domain Layer)
- **Location**: `src/domain/entities/`
- **Purpose**: Core business objects and rules
- **Characteristics**:
  - Independent of any external frameworks or technologies
  - Pure Python classes with business logic
  - Contain domain validation and business invariants
  - No dependencies on outer layers

### 2. Use Cases (Application Layer)
- **Location**: `src/domain/use_cases/`
- **Purpose**: Application-specific business logic
- **Characteristics**:
  - Orchestrate entities and external interfaces
  - Define what the application does, not how
  - Contain application business rules
  - Depend only on entities and interfaces

### 3. Interface Adapters
- **Location**: `src/adapters/`
- **Purpose**: Convert data between external formats and internal formats
- **Sub-layers**:
  - **Web Adapters** (`src/adapters/web/`): HTTP controllers, presenters
  - **Data Adapters** (`src/adapters/data/`): External API clients, repositories
- **Characteristics**:
  - Convert external data to domain objects
  - Handle external interface protocols
  - Implement gateway interfaces defined by use cases

### 4. Frameworks & Drivers
- **Location**: `src/frameworks/`
- **Purpose**: External interfaces and frameworks
- **Characteristics**:
  - Database connections, web frameworks, external APIs
  - Implementation details that change frequently
  - No business logic

## Dependency Direction

The fundamental rule of Clean Architecture is that dependencies point inward:

```
Frameworks & Drivers → Interface Adapters → Use Cases → Entities
```

- Inner layers know nothing about outer layers
- Outer layers depend on inner layers through abstractions/interfaces
- Dependency injection is used to provide implementations at runtime

## Benefits

- **Testability**: Business logic can be tested independently of external dependencies
- **Maintainability**: Changes to external systems don't affect core business logic
- **Flexibility**: Easy to swap implementations (e.g., different databases, APIs)
- **Separation of Concerns**: Each layer has a single responsibility

## Data Flow

1. **Input**: External request enters through Framework layer (e.g., HTTP request)
2. **Controller**: Web adapter converts HTTP data to domain objects
3. **Use Case**: Application logic orchestrates business operations
4. **Entities**: Domain objects enforce business rules
5. **Gateway**: Data adapter calls external services
6. **Response**: Data flows back through layers with appropriate formatting

## Implementation in This Project

- **Entities**: Tunnel and IngressRule domain objects
- **Use Cases**: GetTunnelConfig, UpdateTunnelConfig, ManageIngressRules
- **Web Adapters**: FastAPI controllers and presenters
- **Data Adapters**: Cloudflare API gateway
- **Frameworks**: FastAPI, Requests, Pydantic

For detailed layer responsibilities, see [Layer Details](layers.md).
For data flow examples, see [Data Flow](data-flow.md).