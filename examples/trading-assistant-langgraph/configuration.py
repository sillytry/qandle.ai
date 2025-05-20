from typing import ClassVar, Dict, Optional, Any
from pydantic import BaseModel
from langchain_core.runnables import RunnableConfig

class Configuration(BaseModel):
    """Configuration for the financial agent."""
    user_id: str = "default"
    
    @classmethod
    def from_runnable_config(cls, runnable_config: RunnableConfig) -> "Configuration":
        """Creates a Configuration from a RunnableConfig."""
        configurable = runnable_config.get("configurable", {})
        return cls(**configurable) 