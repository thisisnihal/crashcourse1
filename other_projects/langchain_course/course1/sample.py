import logging
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langsmith import traceable
import google.generativeai as genai

# Logging config
logging.basicConfig(
    filename="sample.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

TRACE_LEVEL = 5
logging.addLevelName(TRACE_LEVEL, "TRACE")


def trace(self, message, *args, **kwargs):
    if self.isEnabledFor(TRACE_LEVEL):
        self._log(TRACE_LEVEL, message, args, **kwargs)


logging.Logger.trace = trace

logging.getLogger().setLevel(TRACE_LEVEL)
logging.getLogger("langchain").setLevel(TRACE_LEVEL)
logging.getLogger("langchain_google_genai").setLevel(TRACE_LEVEL)

# Load .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


genai.configure(api_key=GEMINI_API_KEY, transport="rest")

SUMMARY_TEMPLATE = """
You are a professional book assistant.
Given a passage from a book, do the following:
1. Write a short, clear summary (3-5 sentences)
2. List two interesting or lesser-known facts about it

Passage:
{text}
"""

summary_prompt = PromptTemplate(input_variables=["text"], template=SUMMARY_TEMPLATE)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=GEMINI_API_KEY,
    temperature=0.7,
    max_retries=3,
)


@traceable
def main():
    user_text = input("\nEnter a passage to summarize:\n> ").strip()
    try:
        chain = summary_prompt | llm
        response = chain.invoke({"text": user_text})
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        logger.exception("Error in chain.invoke()")
        return

    print("\nSummary & Facts:\n")
    print(response.content)
    logger.info("Model response: %s", response.content)


if __name__ == "__main__":
    main()
