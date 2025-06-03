import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()

search_tool = TavilySearchResults(max_results=2)

query = "What is the weather in Hyderabad"

search_results = search_tool.invoke(query)
# print(search_results)

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

tools = [search_tool]

memory = MemorySaver()
config = {"configurable": {"thread_id": "unique_thread_1"}}


agent = create_react_agent(model, tools, checkpointer=memory)

response = agent.invoke({'messages':[('user','Hi')]},config=config)
response['messages'][-1].pretty_print()

response = agent.invoke({'messages':[('user','What is the weather in Hyderabad')]},config=config)
response['messages'][-1].pretty_print()

response = agent.invoke({'messages':[('user','Who is the current Prime Minister of India')]},config=config)
response['messages'][-1].pretty_print()

# for res in response['messages']:
#     res.pretty_print()