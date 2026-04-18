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
                # Rule: Must be a Python project OR have 'python' topic, not a fork, and have a description
                topics = repo.get("topics", [])
                is_python = repo.get("language") == "Python" or "python" in topics
                has_description = bool(repo.get("description"))
                is_not_fork = not repo.get("fork")

                if is_python and has_description and is_not_fork:
                    tools.append(Tool(
                        name=repo["name"],
                        description=repo["description"],
                        url=repo["html_url"],
                        command=repo["name"]
                    ))
            
            return ToolResult(tools=tools, success=True)
        except Exception as e:
            return ToolResult(tools=[], success=False, message=str(e))
