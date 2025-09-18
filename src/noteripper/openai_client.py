"""
OpenAI client implementation using requests
Compatible with Python 3.14+
"""

import json
import os
import requests
from typing import Dict, Any, Optional


class OpenAIClient:
    """Simple OpenAI API client using requests."""
    
    def __init__(self, api_key: str, base_url: str = "https://api.openai.com/v1"):
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
    
    def chat_completion(self, model: str, messages: list, **kwargs) -> Dict[str, Any]:
        """Create a chat completion."""
        url = f"{self.base_url}/chat/completions"
        data = {
            'model': model,
            'messages': messages,
            **kwargs
        }
        
        response = requests.post(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()


class AzureOpenAIClient:
    """Simple Azure OpenAI API client using requests."""
    
    def __init__(self, api_key: str, endpoint: str, api_version: str = "2024-02-01"):
        self.api_key = api_key
        self.endpoint = endpoint.rstrip('/')
        self.api_version = api_version
        self.headers = {
            'api-key': api_key,
            'Content-Type': 'application/json'
        }
    
    def chat_completion(self, deployment_name: str, messages: list, **kwargs) -> Dict[str, Any]:
        """Create a chat completion using Azure OpenAI."""
        url = f"{self.endpoint}/openai/deployments/{deployment_name}/chat/completions"
        params = {'api-version': self.api_version}
        data = {
            'messages': messages,
            **kwargs
        }
        
        response = requests.post(url, headers=self.headers, params=params, json=data)
        response.raise_for_status()
        return response.json()