"""
noteripper: An AI-based note system

This is the main entry point for the noteripper application.
It demonstrates basic setup for OpenAI and Azure OpenAI integration.
"""

import os
from dotenv import load_dotenv
from .openai_client import OpenAIClient, AzureOpenAIClient


def load_config():
    """Load configuration from environment variables."""
    load_dotenv()
    
    config = {
        'openai_api_key': os.getenv('OPENAI_API_KEY'),
        'openai_model': os.getenv('OPENAI_MODEL', 'gpt-4o'),
        'azure_openai_api_key': os.getenv('AZURE_OPENAI_API_KEY'),
        'azure_openai_endpoint': os.getenv('AZURE_OPENAI_ENDPOINT'),
        'azure_openai_api_version': os.getenv('AZURE_OPENAI_API_VERSION', '2024-02-01'),
        'azure_openai_deployment': os.getenv('AZURE_OPENAI_DEPLOYMENT_NAME'),
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'log_level': os.getenv('LOG_LEVEL', 'INFO'),
    }
    
    return config


def create_openai_client(config):
    """Create OpenAI client based on configuration."""
    if config['azure_openai_api_key'] and config['azure_openai_endpoint']:
        print("Using Azure OpenAI...")
        return AzureOpenAIClient(
            api_key=config['azure_openai_api_key'],
            endpoint=config['azure_openai_endpoint'],
            api_version=config['azure_openai_api_version']
        )
    elif config['openai_api_key']:
        print("Using OpenAI...")
        return OpenAIClient(api_key=config['openai_api_key'])
    else:
        print("No API keys configured. Please set up your .env file based on .env.example")
        return None


def test_client(client, config):
    """Test the AI client with a simple request."""
    if not client:
        return False
    
    try:
        test_messages = [
            {"role": "user", "content": "Say hello and confirm you're working correctly."}
        ]
        
        if isinstance(client, AzureOpenAIClient):
            response = client.chat_completion(
                deployment_name=config['azure_openai_deployment'],
                messages=test_messages,
                max_tokens=50
            )
        else:
            response = client.chat_completion(
                model=config['openai_model'],
                messages=test_messages,
                max_tokens=50
            )
        
        print(f"✅ AI Response: {response['choices'][0]['message']['content']}")
        return True
    except Exception as e:
        print(f"❌ Error testing AI client: {e}")
        return False


def main():
    """Main function demonstrating the AI note system setup."""
    print("Welcome to noteripper - An AI-based note system!")
    print("=" * 50)
    
    # Load configuration
    config = load_config()
    print(f"Environment: {config['environment']}")
    print(f"Log Level: {config['log_level']}")
    
    # Create AI client
    client = create_openai_client(config)
    
    if client:
        print("✅ AI client successfully initialized!")
        print("🔧 Configuration loaded from environment variables")
        
        # Test the client if API keys are provided
        if config.get('openai_api_key') or (config.get('azure_openai_api_key') and config.get('azure_openai_deployment')):
            print("🧪 Testing AI client...")
            if test_client(client, config):
                print("📝 Ready to process notes with AI assistance")
            else:
                print("⚠️  AI client initialized but test failed - check your API configuration")
        else:
            print("📝 Ready to process notes with AI assistance (add API keys to test)")
    else:
        print("❌ Failed to initialize AI client")
        print("💡 Please copy .env.example to .env and configure your API keys")
    
    print("\nNext steps:")
    print("1. Copy .env.example to .env")
    print("2. Add your OpenAI or Azure OpenAI API keys")
    print("3. Start building your AI-powered note system!")


if __name__ == "__main__":
    main()