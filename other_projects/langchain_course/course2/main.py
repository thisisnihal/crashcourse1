from dotenv import load_dotenv
import os
load_dotenv()

from langchain.agents import create_agent
# from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch
from langsmith import traceable

from schemas import AgentResponse

tools = [TavilySearch(api_key=os.getenv("TAVILY_API_KEY"))]

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.2, google_api_key=GOOGLE_API_KEY) 
# gemma3:270m    e7d36fb2c3b3    291 MB    22 hours ago
# gemma3:4b      a2af6cc3eb7f    3.3 GB    2 days ago
# llama3.1:8b    46e0c10c039e    4.9 GB    2 days ago


agent = create_agent(
    model=llm,
    tools=tools,
    response_format=AgentResponse,
)

@traceable
def main():
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details",
                }
            ]
        }
    )
    
    structured = result.get("structured_response", None)
    print(structured if structured is not None else result)


if __name__ == "__main__":
    main()