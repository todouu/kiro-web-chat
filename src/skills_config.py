"""Skills configuration for Kiro agents.

Skills represent capabilities that agents can use.
This module defines the available skills and their metadata.
"""

from dataclasses import dataclass, field


@dataclass
class Skill:
    """A capability that an agent can use."""

    id: str
    name: str
    description: str
    icon: str
    category: str
    agents: list[str] = field(default_factory=list)  # Which agents have this skill


# All available skills
SKILLS: dict[str, Skill] = {
    "code_generation": Skill(
        id="code_generation",
        name="Code Generation",
        description="Generate code from natural language descriptions. Supports multiple languages and frameworks.",
        icon="💻",
        category="Development",
        agents=["auto"],
    ),
    "refactoring": Skill(
        id="refactoring",
        name="Refactoring",
        description="Improve code structure without changing behavior. Extract functions, rename variables, simplify logic.",
        icon="♻️",
        category="Development",
        agents=["auto"],
    ),
    "debugging": Skill(
        id="debugging",
        name="Debugging",
        description="Identify and fix bugs by analyzing code, error messages, and stack traces.",
        icon="🐛",
        category="Development",
        agents=["auto", "debugger"],
    ),
    "testing": Skill(
        id="testing",
        name="Testing",
        description="Generate and improve test suites. Unit tests, integration tests, and coverage analysis.",
        icon="🧪",
        category="Quality",
        agents=["auto", "test-writer"],
    ),
    "code_review": Skill(
        id="code_review",
        name="Code Review",
        description="Review code for bugs, security issues, performance problems, and adherence to best practices.",
        icon="🔍",
        category="Quality",
        agents=["code-review"],
    ),
    "security_analysis": Skill(
        id="security_analysis",
        name="Security Analysis",
        description="Identify security vulnerabilities, suggest fixes, and enforce secure coding practices.",
        icon="🔒",
        category="Security",
        agents=["code-review"],
    ),
    "performance_review": Skill(
        id="performance_review",
        name="Performance Review",
        description="Identify performance bottlenecks and suggest optimizations.",
        icon="⚡",
        category="Quality",
        agents=["code-review"],
    ),
    "system_design": Skill(
        id="system_design",
        name="System Design",
        description="Design scalable system architectures with clear component boundaries and data flows.",
        icon="🏗️",
        category="Architecture",
        agents=["architect"],
    ),
    "spec_generation": Skill(
        id="spec_generation",
        name="Spec Generation",
        description="Create technical specifications and requirement documents from high-level descriptions.",
        icon="📋",
        category="Architecture",
        agents=["architect"],
    ),
    "architecture_review": Skill(
        id="architecture_review",
        name="Architecture Review",
        description="Review existing architectures for scalability, maintainability, and potential issues.",
        icon="🏛️",
        category="Architecture",
        agents=["architect"],
    ),
    "log_analysis": Skill(
        id="log_analysis",
        name="Log Analysis",
        description="Parse and analyze application logs to identify patterns, errors, and anomalies.",
        icon="📊",
        category="Operations",
        agents=["debugger"],
    ),
    "error_tracing": Skill(
        id="error_tracing",
        name="Error Tracing",
        description="Trace errors through the call stack to identify root causes in complex systems.",
        icon="🔗",
        category="Operations",
        agents=["debugger"],
    ),
    "test_generation": Skill(
        id="test_generation",
        name="Test Generation",
        description="Auto-generate test cases including edge cases, boundary conditions, and error scenarios.",
        icon="🎯",
        category="Quality",
        agents=["test-writer"],
    ),
    "coverage_analysis": Skill(
        id="coverage_analysis",
        name="Coverage Analysis",
        description="Analyze test coverage and suggest tests for uncovered code paths.",
        icon="📈",
        category="Quality",
        agents=["test-writer"],
    ),
    "mocking": Skill(
        id="mocking",
        name="Mocking",
        description="Create test mocks, stubs, and fixtures for isolating units under test.",
        icon="🎭",
        category="Quality",
        agents=["test-writer"],
    ),
    "documentation": Skill(
        id="documentation",
        name="Documentation",
        description="Write and maintain project documentation, including inline comments and guides.",
        icon="📖",
        category="Documentation",
        agents=["docs-writer"],
    ),
    "api_docs": Skill(
        id="api_docs",
        name="API Documentation",
        description="Generate API reference documentation from code, including endpoint descriptions and examples.",
        icon="🌐",
        category="Documentation",
        agents=["docs-writer"],
    ),
    "readme_generation": Skill(
        id="readme_generation",
        name="README Generation",
        description="Create comprehensive README files with setup instructions, examples, and badges.",
        icon="📄",
        category="Documentation",
        agents=["docs-writer"],
    ),
    "ci_cd": Skill(
        id="ci_cd",
        name="CI/CD Pipelines",
        description="Create and optimize continuous integration and deployment pipelines.",
        icon="🔄",
        category="DevOps",
        agents=["devops"],
    ),
    "docker": Skill(
        id="docker",
        name="Docker",
        description="Create Dockerfiles, docker-compose configurations, and container optimization.",
        icon="🐳",
        category="DevOps",
        agents=["devops"],
    ),
    "kubernetes": Skill(
        id="kubernetes",
        name="Kubernetes",
        description="Generate K8s manifests, Helm charts, and cluster configuration.",
        icon="☸️",
        category="DevOps",
        agents=["devops"],
    ),
    "terraform": Skill(
        id="terraform",
        name="Terraform",
        description="Write infrastructure-as-code with Terraform for cloud resource provisioning.",
        icon="🏔️",
        category="DevOps",
        agents=["devops"],
    ),
    "monitoring": Skill(
        id="monitoring",
        name="Monitoring",
        description="Set up observability with metrics, alerts, dashboards, and logging pipelines.",
        icon="📡",
        category="DevOps",
        agents=["devops"],
    ),
}


def list_skills() -> list[Skill]:
    """List all available skills."""
    return list(SKILLS.values())


def get_skills_by_category() -> dict[str, list[Skill]]:
    """Group skills by category."""
    categories: dict[str, list[Skill]] = {}
    for skill in SKILLS.values():
        if skill.category not in categories:
            categories[skill.category] = []
        categories[skill.category].append(skill)
    return categories


def get_skills_for_agent(agent_id: str) -> list[Skill]:
    """Get all skills available to a specific agent."""
    return [s for s in SKILLS.values() if agent_id in s.agents]
