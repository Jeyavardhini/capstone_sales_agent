
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

report_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are a Sales Account Brief Agent.

        Your job is to create a concise, professional one-page
        sales brief from the analysis provided.

        Do not invent facts.
        Clearly label missing or unverified information.
        Keep the report focused on the sales use case.
        """
    ),
    (
        "human",
        """
        Sales Analysis:

        {analysis_information}

        Source URL:
        {source_url}

        Create the final sales brief using these sections:

        # Sales Account Brief

        ## Company Strategy

        ## Technology Strategy

        ## Competitor Mentions

        ## Leadership Information

        ## Business Needs

        ## Sales Opportunity

        ## Recommended Next Steps

        ## Sources / Verification Needed

        Include the provided source URL in the Sources section.
    Do not invent additional source URLs.
    """
    )
])

report_chain = report_prompt | model | StrOutputParser()


def run_report_agent(analysis_information, source_url):
    return report_chain.invoke({
        "analysis_information": analysis_information,
        "source_url": source_url
    })