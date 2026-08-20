# Coding Standards

## Python Style Guide

This project follows PEP 8 Python style guidelines with the following specifics:

### Code Formatting
- Use Black formatter with 88 character line length
- Import organization: standard library, third-party, local modules
- One import per line
- Use type hints for all function parameters and return values

### Naming Conventions
- **Functions/Methods/Variables**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_SNAKE_CASE`
- **Modules**: `snake_case`
- **Packages**: `snake_case`

### Documentation
- Use Google-style docstrings for all classes and methods
- Include type hints in docstrings
- Document parameters, return values, and exceptions
- Write comprehensive docstrings for complex logic

### Code Structure
- Prefer dataclasses for simple data structures
- Use Pydantic models for API data validation
- Implement interfaces/protocols for dependency inversion
- Keep functions small and focused on single responsibility

## Architecture Guidelines

### Layer Separation
- Entities: No external dependencies
- Use Cases: Only depend on entities and interfaces
- Adapters: Implement interfaces, handle data conversion
- Frameworks: Only external system integrations

### Error Handling
- Use custom exceptions for domain errors
- Handle external errors in adapter layers
- Log errors with appropriate levels
- Return meaningful error messages to users

### Testing
- Unit tests for entities and use cases
- Integration tests for adapters
- Mock external dependencies
- Aim for 80%+ code coverage

### Dependency Injection
- Use constructor injection for dependencies
- Define interfaces in inner layers
- Implement interfaces in outer layers
- Avoid global state and singletons

## Git Workflow

### Branch Naming
- `feature/description`: New features
- `bugfix/description`: Bug fixes
- `refactor/description`: Code restructuring

### Commit Messages
- Use conventional commits: `type(scope): description`
- Types: `feat`, `fix`, `docs`, `refactor`, `test`
- Keep messages concise but descriptive

### Pull Requests
- Require code review for all changes
- Include tests for new functionality
- Update documentation as needed
- Squash merge to main branch

## File Organization

### Directory Structure
```
src/
├── domain/
│   ├── entities/          # Domain models
│   └── use_cases/         # Application logic
├── adapters/
│   ├── web/              # HTTP interfaces
│   └── data/             # External APIs
└── frameworks/           # External systems
```

### File Naming
- Use descriptive names that reflect purpose
- Group related functionality in modules
- Keep files focused and not too large
- Use `__init__.py` for package initialization