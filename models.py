from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime
import re

@dataclass
class PaymentProcessorModel:
    """Base model for Payment-Processor"""
    
    id: Optional[int] = None
    created_at: datetime = None
    updated_at: datetime = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.updated_at is None:
            self.updated_at = datetime.now()
    
    def validate(self) -> List[str]:
        """Validate model data and return list of errors"""
        errors = []
        
        # Add specific validation logic here
        if hasattr(self, 'name') and not self.name:
            errors.append("Name is required")
        
        return errors
    
    def to_dict(self) -> dict:
        """Convert model to dictionary"""
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

class ValidationError(Exception):
    """Custom validation error"""
    pass
