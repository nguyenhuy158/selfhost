# Cloudflare Tunnels Manager Documentation

## Overview

The Cloudflare Tunnels Manager is a web application built with FastAPI that provides a user-friendly interface for managing Cloudflare tunnel configurations and zones. It allows users to view tunnel status, connections, and configurations, as well as update ingress rules for routing traffic through Cloudflare tunnels. Additionally, it provides comprehensive zone management capabilities for handling Cloudflare domains.

## Architecture

This project follows Clean Architecture principles, organizing code into four distinct layers:

- **Entities**: Core domain business logic and rules
- **Use Cases**: Application-specific business operations
- **Interface Adapters**: Controllers, presenters, and gateways
- **Frameworks & Drivers**: External frameworks and APIs

For detailed information, see [Clean Architecture Overview](architecture/clean-architecture.md).

## Getting Started

### Local Development Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables (see `.env.example`)
4. Run the application: `uvicorn main:app --reload`

For detailed setup instructions, see [Local Development Setup](deployment/setup.md).

## Development

- [Coding Standards](development/coding-standards.md)
- [Testing Strategy](development/testing.md)
- [Debugging Guide](development/debugging.md)

## Domain Concepts

- [Tunnel Management](domain/tunnel-management.md)
- [Zone Management](domain/zone-management.md)
- [DNS Management](domain/dns-management.md)
- [Ingress Rules](domain/ingress-rules.md)

## Deployment

- [Production Deployment](deployment/production.md)
