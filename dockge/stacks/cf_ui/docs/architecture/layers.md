# Layer Responsibilities

## Entities Layer

### Purpose
The Entities layer contains the core business logic and domain rules that are independent of any external systems or frameworks.

### Responsibilities
- Define domain objects and their relationships
- Implement business rules and validation
- Enforce domain invariants
- Provide pure business logic without side effects

### Examples in This Project
- `Tunnel`: Represents a Cloudflare tunnel with its configuration
- `IngressRule`: Defines routing rules with business validation
- Domain exceptions for business rule violations

### Guidelines
- No external dependencies (no imports from outer layers)
- Pure functions where possible
- Comprehensive unit tests
- Rich domain models with behavior

## Use Cases Layer

### Purpose
The Use Cases layer contains application-specific business logic that orchestrates domain entities and external interfaces.

### Responsibilities
- Implement application workflows
- Coordinate between entities and external services
- Define input/output contracts
- Handle application-level error scenarios

### Examples in This Project
- `GetTunnelConfig`: Retrieve and validate tunnel configuration
- `UpdateTunnelConfig`: Apply configuration changes with business rules
- `ManageIngressRules`: Handle ingress rule CRUD operations

### Guidelines
- Define interfaces for external dependencies (ports)
- No knowledge of external implementation details
- Testable with mocked gateways
- Clear separation of concerns

## Interface Adapters Layer

### Purpose
The Interface Adapters layer converts data between external formats and internal domain formats.

### Web Adapters
- **Controllers**: Handle HTTP requests, validate input, call use cases
- **Presenters**: Format domain responses for HTTP transport

### Data Adapters
- **Gateways**: Implement external API communication
- **Repositories**: Handle data persistence (if applicable)

### Examples in This Project
- FastAPI route handlers as controllers
- JSON response formatters as presenters
- Cloudflare API client as gateway

### Guidelines
- Thin layer focused on data transformation
- Implement interfaces defined by use cases
- Handle external system errors gracefully
- Easy to test with integration tests

## Frameworks & Drivers Layer

### Purpose
The Frameworks layer contains external system integrations and implementation details.

### Responsibilities
- HTTP server setup (FastAPI)
- External API clients (Requests)
- Configuration management
- Logging frameworks
- Database connections (if added later)

### Examples in This Project
- FastAPI application setup
- Requests HTTP client configuration
- Environment variable handling

### Guidelines
- No business logic
- Easy to replace or mock
- Configuration-driven
- Error handling for external systems