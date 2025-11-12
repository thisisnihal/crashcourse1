import os

import certifi
from dotenv import load_dotenv
# from google import genai
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langsmith import traceable

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# client = genai.Client(api_key=GEMINI_API_KEY)


SUMMARY_TEMPLATE = """
You are a professional book assistant.
Given a passage from a book, do the following:
1. Write a short, clear summary (3-5 sentences)
2. List two interesting or lesser-known facts about it

Passage:
{text}
"""

summary_prompt_template = PromptTemplate(
    input_variables=["text"], template=SUMMARY_TEMPLATE
)

# llm_gemini = ChatGoogleGenerativeAI(
#     model="gemini-2.0-flash", google_api_key=GEMINI_API_KEY, max_retries=2
# )
llm_ollama = ChatOllama(model="gemma3:270m", temperature=0.2)


user_input = open("user_input.txt", "r").read()
chain = summary_prompt_template | llm_ollama

# @traceable
def main():

    print("Hello")


    response = chain.invoke(input={"text": user_input})

    print(response.content)


if __name__ == "__main__":
    main()
