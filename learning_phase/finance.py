from agno.agent import Agent
from agno.models.groq import Groq

from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools

from agno.tools.yfinance import YFinanceTools

load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3-32b"),
        tools=[YFinanceTools(), DuckDuckGoTools()],
        markdown=True,
        description="You are an invesment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=["Use given tools whenever possible. Format your response using markdown and use tables to display data where possible."],
        add_datetime_to_context=True
    )

agent = build_agent()
agent.print_response("Share the NVDA stock price and analyst recommendations")