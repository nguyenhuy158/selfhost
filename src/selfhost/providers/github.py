import httpx
from typing import List
from ..core import Tool, ToolResult

class GitHubProvider:
    def __init__(self, username: str = "nguyenhuy158"):
        self.username = username
        self.base_url = f"https://api.github.com/users/{username}/repos"

    def fetch_tools(self) -> ToolResult:
        try:
            # Added User-Agent as required by GitHub API
            headers = {"User-Agent": "selfhost-cli"}
            response = httpx.get(self.base_url, headers=headers, params={"type": "public", "sort": "updated"})
            response.raise_for_status()
            
            repos = response.json()
            tools = []
            
            for repo in repos:
                # We consider a "tool" as a public repo that is not a fork (optional) 
                # and has a description.
                if not repo.get("fork") and repo.get("description"):
                    tools.append(Tool(
                        name=repo["name"],
                        description=repo["description"],
                        url=repo["html_url"],
                        command=repo["name"] # Default command is the repo name
                    ))
            
            return ToolResult(tools=tools, success=True)
        except Exception as e:
            return ToolResult(tools=[], success=False, message=str(e))
