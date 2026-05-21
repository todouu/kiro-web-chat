"""Skills Page — Shows all available Kiro agent skills."""

import streamlit as st

from src.skills_config import get_skills_by_category, get_skills_for_agent
from src.agents_config import list_agents

st.set_page_config(page_title="Skills — Kiro Web", page_icon="⚡", layout="wide")

st.markdown(
    """
<style>
    .stApp { background-color: #1a1a2e; }
    .skill-card {
        background-color: #2d2d44;
        border-radius: 12px;
        padding: 16px;
        margin: 8px 0;
        border: 1px solid #3d3d5c;
    }
    .skill-card:hover { border-color: #6366f1; }
    .category-header {
        color: #a5b4fc;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-top: 1.5rem;
    }
</style>
""",
    unsafe_allow_html=True,
)

st.markdown("# ⚡ Skills")
st.markdown("Skills are capabilities available to Kiro agents. Each agent has access to a specific set of skills based on its role.")
st.markdown("---")

# Filter by agent
col_filter, _ = st.columns([1, 3])
with col_filter:
    agents = list_agents()
    agent_options = ["All"] + [a.name for a in agents]
    selected = st.selectbox("Filter by Agent", agent_options, label_visibility="collapsed")

# Get skills
if selected == "All":
    skills_by_cat = get_skills_by_category()
else:
    agent_id = next(a.id for a in agents if a.name == selected)
    agent_skills = get_skills_for_agent(agent_id)
    skills_by_cat = {}
    for s in agent_skills:
        if s.category not in skills_by_cat:
            skills_by_cat[s.category] = []
        skills_by_cat[s.category].append(s)

# Render skills by category
if not skills_by_cat:
    st.info("No skills found for the selected filter.")
else:
    for category, skills in sorted(skills_by_cat.items()):
        st.markdown(f"<p class='category-header'>{category}</p>", unsafe_allow_html=True)

        cols = st.columns(3)
        for i, skill in enumerate(skills):
            with cols[i % 3]:
                # Agent badges
                agent_badges = " ".join(
                    [f"`{aid}`" for aid in skill.agents]
                )
                st.markdown(
                    f"""
<div class="skill-card">
    <div style="font-size: 1.5rem; margin-bottom: 4px;">{skill.icon}</div>
    <div style="font-weight: 600; color: #e0e0e0; margin-bottom: 4px;">{skill.name}</div>
    <div style="color: #9ca3af; font-size: 0.85rem; margin-bottom: 8px;">{skill.description}</div>
    <div style="font-size: 0.75rem; color: #6366f1;">Agents: {agent_badges}</div>
</div>
""",
                    unsafe_allow_html=True,
                )

# Summary stats
st.markdown("---")
total_skills = sum(len(s) for s in skills_by_cat.values())
total_categories = len(skills_by_cat)
st.caption(f"Showing {total_skills} skills across {total_categories} categories")
