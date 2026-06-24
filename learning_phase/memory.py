from agno.agent import Agent
from agno.models.groq import Groq

from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint

load_dotenv()


db = SqliteDb(db_file="agno.db")
db.clear_memories()


def build_agent():
    return Agent(
        db=db,
        model=Groq(id="qwen/qwen3-32b"),
        markdown=True,
        instructions="You are a helpful and expert travel agent.",
        add_history_to_context=True,
        enable_agentic_memory=True
    )

agent = build_agent()


agent.print_response("What is the capital of Australia ?")
agent.print_response("What is the best time to visit it?")


    