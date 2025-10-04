import os
from dataclasses import dataclass
from typing import Optional

@dataclass
class PaymentProcessorConfig:
    """Configuration class for Payment-Processor"""
    
    # Database settings
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///app.db")
    database_pool_size: int = int(os.getenv("DATABASE_POOL_SIZE", "10"))
    
    # API settings
    api_host: str = os.getenv("API_HOST", "0.0.0.0")
    api_port: int = int(os.getenv("API_PORT", "8000"))
    api_debug: bool = os.getenv("API_DEBUG", "false").lower() == "true"
    
    # Business logic settings
    max_retries: int = int(os.getenv("MAX_RETRIES", "3"))
    timeout_seconds: int = int(os.getenv("TIMEOUT_SECONDS", "30"))
    
    @classmethod
    def from_env(cls) -> 'PaymentProcessorConfig':
        """Create config from environment variables"""
        return cls()

# Global config instance
config = PaymentProcessorConfig.from_env()
