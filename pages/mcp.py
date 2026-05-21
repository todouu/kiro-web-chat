"""MCP Page — Shows available MCP servers and their tools."""

import streamlit as st

from src.mcp_config import list_mcp_servers, get_servers_for_agent
from src.agents_config import list_agents

st.set_page_config(page_title="MCP — Kiro Web", page_icon="🔌", layout="wide")

st.markdown(
    """
<style>
    .stApp { background-color: #1a1a2e; }
    .mcp-card {
        background-color: #2d2d44;
        border-radius: 12px;
        padding: 20px;
        margin: 12px 0;
        border: 1px solid #3d3d5c;
    }
    .mcp-card:hover { border-color: #22c55e; }
    .tool-item {
        background-color: #1e1e36;
        border-radius: 8px;
        padding: 10px 14px;
        margin: 6px 0;
        border-left: 3px solid #6366f1;
    }
    .transport-badge {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 0.7rem;
        font-weight: 600;
        text-transform: uppercase;
    }
    .transport-stdio { background-color: #22c55e22; color: #22c55e; }
    .transport-http { background-color: #3b82f622; color: #3b82f6; }
</style>
""",
    unsafe_allow_html=True,
)

st.markdown("# 🔌 MCP Servers")
st.markdown(
    "Model Context Protocol (MCP) servers provide tools that agents use to interact with "
    "external systems — filesystems, APIs, databases, and more."
)
st.markdown("---")

# Filter
col_filter, _ = st.columns([1, 3])
with col_filter:
    agents = list_agents()
    agent_options = ["All"] + [a.name for a in agents]
    selected = st.selectbox("Filter by Agent", agent_options, label_visibility="collapsed")

# Get servers
if selected == "All":
    servers = list_mcp_servers()
else:
    agent_id = next(a.id for a in agents if a.name == selected)
    servers = get_servers_for_agent(agent_id)

if not servers:
    st.info("No MCP servers found for the selected filter.")
else:
    for server in servers:
        transport_class = "transport-stdio" if server.transport == "stdio" else "transport-http"

        # Agent usage badges
        agent_usage = ""
        if server.agents:
            agent_usage = " ".join([f"`{a}`" for a in server.agents])

        st.markdown(
            f"""
<div class="mcp-card">
    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
        <span style="font-size: 2rem;">{server.icon}</span>
        <div>
            <div style="font-weight: 600; font-size: 1.1rem; color: #e0e0e0;">{server.name}</div>
            <span class="transport-badge {transport_class}">{server.transport}</span>
        </div>
    </div>
    <div style="color: #9ca3af; margin-bottom: 12px;">{server.description}</div>
    <div style="font-size: 0.75rem; color: #6366f1; margin-bottom: 4px;">Used by: {agent_usage}</div>
    <div style="font-size: 0.75rem; color: #6b7280;">Command: <code>{server.command}</code></div>
</div>
""",
            unsafe_allow_html=True,
        )

        # Tools expander
        with st.expander(f"🔧 {len(server.tools)} tools available", expanded=False):
            for tool in server.tools:
                params_str = ", ".join(tool.parameters) if tool.parameters else "none"
                st.markdown(
                    f"""
<div class="tool-item">
    <div style="font-weight: 600; color: #e0e0e0; font-size: 0.9rem;">{tool.name}</div>
    <div style="color: #9ca3af; font-size: 0.8rem; margin-top: 2px;">{tool.description}</div>
    <div style="color: #6b7280; font-size: 0.75rem; margin-top: 4px;">Parameters: <code>{params_str}</code></div>
</div>
""",
                    unsafe_allow_html=True,
                )

# Summary
st.markdown("---")
total_tools = sum(len(s.tools) for s in servers)
st.caption(f"Showing {len(servers)} MCP servers with {total_tools} total tools")
