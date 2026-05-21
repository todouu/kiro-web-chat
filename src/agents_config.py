"""Pre-configured agent definitions.

Each agent has a name, description, icon, and the prompt/system context
that will be used when communicating via ACP.

Users select which agent to use from the sidebar list.
"""

from dataclasses import dataclass, field


@dataclass
class AgentConfig:
    """Configuration for a pre-defined agent."""

    id: str
    name: str
    description: str
    icon: str
    system_prompt: str  # Sent as context when creating the ACP session
    skills: list[str] = field(default_factory=list)
    mcp_servers: list[str] = field(default_factory=list)


# Pre-configured agents - add/modify as needed
AGENTS: dict[str, AgentConfig] = {
    "auto": AgentConfig(
        id="auto",
        name="Auto",
        description="Balanced agent that automatically selects the best approach for each task. Good for general development work.",
        icon="🤖",
        system_prompt="You are a helpful AI coding assistant.",
        skills=["code_generation", "refactoring", "debugging", "testing"],
        mcp_servers=["filesystem", "github"],
    ),
    "code-review": AgentConfig(
        id="code-review",
        name="Code Review",
        description="Reviews code for bugs, security issues, and best practices. Provides actionable feedback.",
        icon="🔍",
        system_prompt="You are an expert code reviewer. Focus on identifying bugs, security vulnerabilities, performance issues, and suggest improvements following best practices.",
        skills=["code_review", "security_analysis", "performance_review"],
        mcp_servers=["filesystem", "github"],
    ),
    "architect": AgentConfig(
        id="architect",
        name="Architect",
        description="Designs system architecture, creates technical specs, and plans implementation strategies.",
        icon="🏗️",
        system_prompt="You are a software architect. Help design scalable, maintainable systems. Create technical specifications, architecture diagrams (in mermaid), and implementation plans.",
        skills=["system_design", "spec_generation", "architecture_review"],
        mcp_servers=["filesystem"],
    ),
    "debugger": AgentConfig(
        id="debugger",
        name="Debugger",
        description="Specializes in finding and fixing bugs. Analyzes stack traces, reproduces issues, and suggests fixes.",
        icon="🐛",
        system_prompt="You are an expert debugger. Analyze error messages, stack traces, and code to identify root causes. Suggest minimal, targeted fixes.",
        skills=["debugging", "log_analysis", "error_tracing"],
        mcp_servers=["filesystem", "shell"],
    ),
    "test-writer": AgentConfig(
        id="test-writer",
        name="Test Writer",
        description="Generates comprehensive tests — unit, integration, and e2e. Focuses on edge cases and coverage.",
        icon="🧪",
        system_prompt="You are a testing expert. Write comprehensive tests including unit tests, integration tests, and edge cases. Aim for high coverage and clear test descriptions.",
        skills=["test_generation", "coverage_analysis", "mocking"],
        mcp_servers=["filesystem", "shell"],
    ),
    "docs-writer": AgentConfig(
        id="docs-writer",
        name="Docs Writer",
        description="Creates and maintains documentation — READMEs, API docs, inline comments, and technical guides.",
        icon="📝",
        system_prompt="You are a technical documentation expert. Write clear, concise documentation including READMEs, API references, guides, and inline code comments.",
        skills=["documentation", "api_docs", "readme_generation"],
        mcp_servers=["filesystem"],
    ),
    "devops": AgentConfig(
        id="devops",
        name="DevOps",
        description="Handles CI/CD, Docker, Kubernetes, infrastructure-as-code, and deployment configurations.",
        icon="⚙️",
        system_prompt="You are a DevOps expert. Help with CI/CD pipelines, Docker configurations, Kubernetes manifests, Terraform, and deployment strategies.",
        skills=["ci_cd", "docker", "kubernetes", "terraform", "monitoring"],
        mcp_servers=["filesystem", "shell", "docker"],
    ),
}


def get_agent(agent_id: str) -> AgentConfig | None:
    """Get agent configuration by ID."""
    return AGENTS.get(agent_id)


def list_agents() -> list[AgentConfig]:
    """List all available agents."""
    return list(AGENTS.values())
