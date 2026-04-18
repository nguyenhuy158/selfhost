import httpx
import asyncio
from typing import List
from ..core import Tool, ToolResult

class GitHubProvider:
    def __init__(self, username: str = "nguyenhuy158"):
        self.username = username
        self.base_url = f"https://api.github.com/users/{username}/repos"

    def fetch_tools(self) -> ToolResult:
        try:
            return asyncio.run(self._fetch_all())
        except Exception as e:
            return ToolResult(tools=[], success=False, message=str(e))

    async def _fetch_all(self) -> ToolResult:
        async with httpx.AsyncClient() as client:
            headers = {"User-Agent": "selfhost-cli"}
            response = await client.get(self.base_url, headers=headers, params={"type": "public", "sort": "updated"})
            response.raise_for_status()
            
            repos = response.json()
            tasks = []
            
            for repo in repos:
                topics = repo.get("topics", [])
                is_python = repo.get("language") == "Python" or "python" in topics
                has_description = bool(repo.get("description"))
                is_not_fork = not repo.get("fork")

                if is_python and has_description and is_not_fork:
                    tasks.append(self._process_repo(client, repo))
            
            tools = await asyncio.gather(*tasks)
            return ToolResult(tools=list(tools), success=True)

    async def _process_repo(self, client: httpx.AsyncClient, repo: dict) -> Tool:
        name = repo["name"]
        tags_url = repo["tags_url"]
        headers = {"User-Agent": "selfhost-cli"}
        
        version = "n/a"
        try:
            tags_res = await client.get(tags_url, headers=headers)
            if tags_res.status_code == 200:
                tags = tags_res.json()
                if tags:
                    version = tags[0]["name"].lstrip("v")
        except:
            pass

        return Tool(
            name=name,
            description=repo["description"],
            url=repo["html_url"],
            command=name,
            install_cmd=f"uvx {name}",
            version=version
        )
