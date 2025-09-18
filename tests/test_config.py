"""
Test configuration validation for noteripper
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from noteripper.main import load_config, create_openai_client


def test_config_loading():
    """Test that configuration loads without errors."""
    config = load_config()
    
    # Check that all expected keys are present
    expected_keys = [
        'openai_api_key', 'openai_model', 'azure_openai_api_key',
        'azure_openai_endpoint', 'azure_openai_api_version',
        'azure_openai_deployment', 'environment', 'log_level'
    ]
    
    for key in expected_keys:
        assert key in config, f"Missing config key: {key}"
    
    print("✅ Configuration loading test passed")


def test_client_creation():
    """Test that client creation works with empty config."""
    config = {
        'openai_api_key': None,
        'azure_openai_api_key': None,
        'azure_openai_endpoint': None,
    }
    
    client = create_openai_client(config)
    assert client is None, "Client should be None when no API keys are provided"
    
    print("✅ Client creation test passed")


def test_api_key_detection():
    """Test that API key detection works correctly."""
    # Test OpenAI config
    config = {
        'openai_api_key': 'test-key',
        'azure_openai_api_key': None,
        'azure_openai_endpoint': None,
    }
    
    client = create_openai_client(config)
    assert client is not None, "Client should be created with OpenAI key"
    
    # Test Azure OpenAI config
    config = {
        'openai_api_key': None,
        'azure_openai_api_key': 'test-key',
        'azure_openai_endpoint': 'https://test.openai.azure.com',
        'azure_openai_api_version': '2024-02-01'
    }
    
    client = create_openai_client(config)
    assert client is not None, "Client should be created with Azure OpenAI key"
    
    print("✅ API key detection test passed")


if __name__ == "__main__":
    print("Running noteripper configuration tests...")
    test_config_loading()
    test_client_creation()
    test_api_key_detection()
    print("🎉 All tests passed!")