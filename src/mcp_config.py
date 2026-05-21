"""MCP (Model Context Protocol) server configuration.

Defines the MCP servers available to agents, including their tools and capabilities.
"""

from dataclasses import dataclass, field


@dataclass
class MCPTool:
    """A tool provided by an MCP server."""

    name: str
    description: str
    parameters: list[str] = field(default_factory=list)


@dataclass
class MCPServer:
    """An MCP server configuration."""

    id: str
    name: str
    description: str
    icon: str
    transport: str  # "stdio" or "http"
    command: str  # The command to start the server
    tools: list[MCPTool] = field(default_factory=list)
    status: str = "available"  # "available", "connected", "error"
    agents: list[str] = field(default_factory=list)  # Which agents use this server


# Pre-configured MCP servers
MCP_SERVERS: dict[str, MCPServer] = {
    "filesystem": MCPServer(
        id="filesystem",
        name="Filesystem",
        description="Read, write, and manage files in the workspace. Provides tools for file operations, directory listing, and content search.",
        icon="📁",
        transport="stdio",
        command="mcp-server-filesystem",
        tools=[
            MCPTool(
                name="read_file",
                description="Read the contents of a file",
                parameters=["path"],
            ),
            MCPTool(
                name="write_file",
                description="Write content to a file (create or overwrite)",
                parameters=["path", "content"],
            ),
            MCPTool(
                name="list_directory",
                description="List files and directories at a given path",
                parameters=["path"],
            ),
            MCPTool(
                name="search_files",
                description="Search for files matching a pattern",
                parameters=["pattern", "path"],
            ),
            MCPTool(
                name="get_file_info",
                description="Get metadata about a file (size, modified date, etc.)",
                parameters=["path"],
            ),
        ],
        agents=["auto", "code-review", "architect", "debugger", "test-writer", "docs-writer", "devops"],
    ),
    "github": MCPServer(
        id="github",
        name="GitHub",
        description="Interact with GitHub repositories — create PRs, manage issues, review code, and access repo metadata.",
        icon="🐙",
        transport="stdio",
        command="mcp-server-github",
        tools=[
            MCPTool(
                name="create_pull_request",
                description="Create a new pull request",
                parameters=["title", "body", "head", "base"],
            ),
            MCPTool(
                name="list_issues",
                description="List issues in a repository",
                parameters=["state", "labels"],
            ),
            MCPTool(
                name="create_issue",
                description="Create a new issue",
                parameters=["title", "body", "labels"],
            ),
            MCPTool(
                name="get_file_contents",
                description="Get file contents from a repository",
                parameters=["path", "ref"],
            ),
            MCPTool(
                name="push_files",
                description="Push file changes to a branch",
                parameters=["branch", "files", "message"],
            ),
        ],
        agents=["auto", "code-review"],
    ),
    "shell": MCPServer(
        id="shell",
        name="Shell",
        description="Execute shell commands in the workspace. Run builds, tests, linters, and other CLI tools.",
        icon="🖥️",
        transport="stdio",
        command="mcp-server-shell",
        tools=[
            MCPTool(
                name="execute_command",
                description="Execute a shell command and return output",
                parameters=["command", "cwd", "timeout"],
            ),
            MCPTool(
                name="background_process",
                description="Start a long-running process in the background",
                parameters=["command", "cwd"],
            ),
            MCPTool(
                name="kill_process",
                description="Kill a running background process",
                parameters=["pid"],
            ),
        ],
        agents=["debugger", "test-writer", "devops"],
    ),
    "docker": MCPServer(
        id="docker",
        name="Docker",
        description="Manage Docker containers, images, and compose stacks. Build, run, and inspect containers.",
        icon="🐳",
        transport="stdio",
        command="mcp-server-docker",
        tools=[
            MCPTool(
                name="build_image",
                description="Build a Docker image from a Dockerfile",
                parameters=["dockerfile", "tag", "context"],
            ),
            MCPTool(
                name="run_container",
                description="Run a Docker container",
                parameters=["image", "ports", "volumes", "env"],
            ),
            MCPTool(
                name="list_containers",
                description="List running containers",
                parameters=["all"],
            ),
            MCPTool(
                name="container_logs",
                description="Get logs from a container",
                parameters=["container_id", "tail"],
            ),
            MCPTool(
                name="compose_up",
                description="Start services defined in docker-compose.yml",
                parameters=["file", "services"],
            ),
        ],
        agents=["devops"],
    ),
    "web-search": MCPServer(
        id="web-search",
        name="Web Search",
        description="Search the web for documentation, solutions, and current information about libraries and APIs.",
        icon="🔍",
        transport="stdio",
        command="mcp-server-web-search",
        tools=[
            MCPTool(
                name="search",
                description="Search the web for information",
                parameters=["query"],
            ),
            MCPTool(
                name="fetch_page",
                description="Fetch and extract content from a URL",
                parameters=["url"],
            ),
        ],
        agents=["auto", "architect"],
    ),
    "postgres": MCPServer(
        id="postgres",
        name="PostgreSQL",
        description="Connect to PostgreSQL databases. Run queries, inspect schemas, and manage migrations.",
        icon="🐘",
        transport="stdio",
        command="mcp-server-postgres",
        tools=[
            MCPTool(
                name="query",
                description="Execute a SQL query",
                parameters=["sql", "params"],
            ),
            MCPTool(
                name="list_tables",
                description="List all tables in the database",
                parameters=[],
            ),
            MCPTool(
                name="describe_table",
                description="Get table schema (columns, types, constraints)",
                parameters=["table_name"],
            ),
        ],
        agents=[],
    ),
}


def list_mcp_servers() -> list[MCPServer]:
    """List all available MCP servers."""
    return list(MCP_SERVERS.values())


def get_mcp_server(server_id: str) -> MCPServer | None:
    """Get an MCP server by ID."""
    return MCP_SERVERS.get(server_id)


def get_servers_for_agent(agent_id: str) -> list[MCPServer]:
    """Get all MCP servers available to a specific agent."""
    return [s for s in MCP_SERVERS.values() if agent_id in s.agents]
