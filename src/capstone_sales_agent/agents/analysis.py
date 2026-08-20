
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

analysis_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are a Sales Analysis Agent.

        Your job is to analyze research about a prospective
        company and identify useful information for a sales representative.

        Do not invent facts.
        Clearly separate facts from assumptions.
        """
    ),
    (
        "human",
        """
        Research information:

        {research_information}

        Analyze the information and return:

        1. Company Strategy
        2. Technology Strategy
        3. Competitor Activity
        4. Leadership Information
        5. Business Needs
        6. Potential Sales Opportunities
        7. Risks or Missing Information
        """
    )
])

analysis_chain = analysis_prompt | model | StrOutputParser()


def run_analysis_agent(research_information):
    return analysis_chain.invoke({
        "research_information": research_information
    })