from agno.agent import Agent
from agno.models.groq import Groq

from dotenv import load_dotenv
from agno.team import Team

load_dotenv()


eng_agent = Agent(name="English agent",role="You answer questions in english")
chi_agent = Agent(name="Chinese agent",role="You answer questions in chinese")
hindi_agent = Agent(name="Hindi agent",role="You answer questions in hindi")

team = Team(
    name="Answer and Translation Team",
    members=[eng_agent, chi_agent, hindi_agent],
    model=Groq(id="qwen/qwen3-32b"),
    markdown=True,
    show_members_responses=True,
    instructions=""" All member agents must respond to answer the query in their specific language.
                    Do not route just one agent.
                    Output the response of all agents

                 """
)





team.print_response("What is the capital of India ?")
    