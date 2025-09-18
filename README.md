# noteripper

An AI-based note system built with Python 3.14+ and uv package management.

## Features

- 🐍 **Python 3.14+ Ready**: Built with the latest Python features
- ⚡ **Fast Package Management**: Uses uv for ultra-fast dependency resolution
- 🤖 **AI Integration**: Supports both OpenAI and Azure OpenAI APIs
- 🔧 **Easy Configuration**: Environment-based configuration with .env files
- 📦 **Modern Project Structure**: Follows Python packaging best practices

## Quick Start

### Prerequisites

- Python 3.14+
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd noteripper
```

2. Set up the project with uv:
```bash
uv sync
```

3. Configure your API keys:
```bash
cp .env.example .env
# Edit .env with your OpenAI or Azure OpenAI credentials
```

4. Run the application:
```bash
uv run noteripper
# or
uv run python main.py
```

## Configuration

Copy `.env.example` to `.env` and configure your API keys:

### OpenAI Configuration
```env
OPENAI_API_KEY=sk-your-openai-api-key-here
OPENAI_MODEL=gpt-4o
```

### Azure OpenAI Configuration
```env
AZURE_OPENAI_API_KEY=your-azure-openai-api-key-here
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-02-01
AZURE_OPENAI_DEPLOYMENT_NAME=your-deployment-name
```

## Development

### Project Structure
```
noteripper/
├── src/
│   └── noteripper/
│       ├── __init__.py
│       ├── main.py
│       └── openai_client.py
├── .env.example
├── main.py
├── pyproject.toml
└── README.md
```

### Running in Development
```bash
# Install in development mode
uv sync

# Run the application
uv run noteripper

# Run directly with Python
uv run python main.py
```

### Dependencies

- **requests**: HTTP client for API calls
- **python-dotenv**: Environment variable management

## Python 3.14 Compatibility

This project is designed for Python 3.14+ and uses a custom OpenAI client implementation using `requests` to ensure compatibility. When the official `openai` package fully supports Python 3.14, we can easily switch to it.

## License

MIT License - see LICENSE file for details.
