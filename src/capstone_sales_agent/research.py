from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

research_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are a Company Research Agent.

        Your responsibility is to determine what information
        should be researched about a prospective customer.

        Focus only on information relevant to the sales opportunity.

        Do not make the final sales recommendation.
        Do not invent facts.
        """
    ),
    (
        "human",
        """
        Here is the output from the Sales Agent:

        {sales_information}

        Based on this information, identify research areas for:

        1. Company Strategy
        2. Technology Strategy
        3. Competitor Mentions
        4. Leadership
        5. Relevant Products or Services
        6. Recent Company News
        7. Job Postings or Technology Indicators
        8. Potential Sales Opportunity

        Clearly explain what should be researched in each area.
        """
    )
])

research_chain = research_prompt | model | StrOutputParser()


def run_research_agent(sales_information):
    return research_chain.invoke({
        "sales_information": sales_informations
    })