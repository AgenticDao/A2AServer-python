# Crypto A2A Server Python

## Overview

Crypto A2A Server Python is a reference implementation of the Agent-to-Agent (A2A) protocol server in Python. It enables communication between AI agents through a standardized JSON-RPC based API, supporting both synchronous and streaming responses for blockchain and crypto-related applications.

## Features

- Full implementation of the Crypto A2A protocol specification
- In-memory task management system
- Support for Server-Sent Events (SSE) for real-time streaming updates
- Push notification capabilities with JWT-based authentication
- Thread-safe design for concurrent request handling
- Extensible architecture with abstract interfaces for custom implementations

## Roadmap

Upcoming features and integrations planned for development:

- **Solana Blockchain Integration**: Implementation of on-chain verification logic and Market contract validation (In Progress)

## Installation

### Requirements

- Python 3.13+
- uv

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/AgenticDao/A2AServer-python
   cd A2AServer-python
   ```

2. Running Tests:
    ```bash
    uv run --dev pytest -v -s tests/test_a2a_spec.py
    ```

## Usage

### Basic Server Setup

```python
from crypto_a2a.client import A2AClient
from crypto_a2a.server.apps import A2AStarletteApplication
from crypto_a2a.types import AgentCard, AgentProvider, AgentCapabilities, AgentSkill, AgentAuthentication

# Configure your agent card
agent_card = AgentCard(
    name="My Agent",
    description="A sample agent",
    url="https://example.com/agent",
    provider=AgentProvider(organization="Example Corp"),
    version="1.0.0",
    capabilities=AgentCapabilities(
        streaming=True,
        pushNotifications=True,
        stateTransitionHistory=True
    ),
    authentication=AgentAuthentication(schemes=["none"]),
    skills=[
        AgentSkill(
            id="example-skill",
            name="Example Skill",
            description="An example skill"
        )
    ]
)

# Create the Starlette application with your agent configuration
app = A2AStarletteApplication(agent_card=agent_card)

# The app can now be run with any ASGI server like Uvicorn
# import uvicorn
# uvicorn.run(app, host="0.0.0.0", port=5000)
```

## API Endpoints

- `POST /` - Main endpoint for Crypto A2A JSON-RPC requests
- `GET /.well-known/agent.json` - Endpoint for retrieving the agent capability card

## Architecture

The server is built on the following components:

- **A2AStarletteApplication**: Main server class that handles HTTP requests and routes them to the appropriate handlers
- **RequestHandlers**: Components for handling different types of A2A requests
- **TaskManagement**: System for managing, tracking, and updating agent tasks
- **Push Notifications**: Authentication and delivery system for external notifications

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

## Acknowledgments

- Based on the Crypto A2A protocol specification
- Built with Starlette framework
