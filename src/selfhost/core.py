from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Tool:
    name: str
    description: str
    url: str
    command: str

@dataclass
class ToolResult:
    tools: List[Tool]
    success: bool
    message: str = ""
