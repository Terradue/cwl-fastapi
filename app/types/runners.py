from typing import Any
from pydantic import BaseModel
from app.core.config import Configuration

class Runner(BaseModel):
    name: str
    module: str
    
class RunnerFactory():
    """Runner factory
    
    Factory for loading all available runners in the app.
    
    """
    
    def get_runners(self) -> list[Runner]:
        cfg = Configuration.load()
        return [Runner.parse_obj(r) for r in cfg.runners]