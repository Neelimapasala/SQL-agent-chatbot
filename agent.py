"""
agent.py — LangChain SQL Agent powered by Groq + SQLite
"""
import os
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_groq import ChatGroq

# ── Paste your Groq API key here ──────────────────────────────
os.environ["GROQ_API_KEY"] = "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"
# ──────────────────────────────────────────────────────────────


def build_agent(db_path: str = "company.db", model: str = "llama-3.1-8b-instant"):
    db = SQLDatabase.from_uri(f"sqlite:///{db_path}")

    llm = ChatGroq(
        model=model,
        temperature=0.0,
    )

    agent_executor = create_sql_agent(
        llm=llm,
        db=db,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=10,
    )

    return agent_executor


def run_query(agent, question: str) -> str:
    try:
        result = agent.invoke({"input": question})
        return result.get("output", "No response generated.")
    except Exception as e:
        return f"Error: {str(e)}"