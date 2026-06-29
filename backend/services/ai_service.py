import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_research(query: str):

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"""
        You are a professional business analyst.

        Analyze:

        {query}

        Provide:

        1. Market Analysis
        2. Opportunities
        3. Risks
        4. Recommendations
        """
    )

    return response.output_text