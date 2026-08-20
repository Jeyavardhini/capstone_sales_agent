
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

        Your job is to identify what information should be
        researched about a prospective customer.

        Focus only on information relevant to the sales opportunity.

        Do not invent facts.
        Do not make the final recommendation.
        """
    ),
    (
        "human",
        """
        Sales Agent information:

        {sales_information}

        Identify research areas for:

        1. Company Strategy
        2. Technology Strategy
        3. Competitor Mentions
        4. Leadership
        5. Relevant Products or Services
        6. Recent Company News
        7. Job Postings or Technology Indicators
        8. Potential Sales Opportunity
        """
    )
])

research_chain = research_prompt | model | StrOutputParser()


def run_research_agent(sales_information, web_content, source_url):
    {source_url}
    return research_chain.invoke({
        "sales_information": sales_information,
        "web_content": web_content,
        "source_url": source_url
    })