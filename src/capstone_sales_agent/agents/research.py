
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

        Your job is to analyze publicly available company
        information for a sales representative.

        You MUST base your findings only on:
        1. The supplied Sales Agent information
        2. The supplied web content
        3. The supplied source URLs

        Do not invent facts.
        Do not assume information that is not supported by
        the supplied web content.

        If information cannot be verified from the supplied
        sources, clearly state:
        "Not verified from the provided sources."

        Do not make the final sales recommendation.
        """
    ),
    (
        "human",
        """
        SALES AGENT INFORMATION:

        {sales_information}


        PUBLIC WEB CONTENT:

        {web_content}


        SOURCE URLS:

        {source_url}


        Using ONLY the information above, research and summarize:

        1. Company Strategy
        - Relevant company initiatives
        - Business priorities
        - Public strategy statements

        2. Technology Strategy
        - Technology platforms
        - Cloud or data initiatives
        - Technology-stack indicators

        3. Competitor Mentions
        - Identify mentions of competitors supplied by the Sales Agent
        - Explain the context of those mentions
        - Do not claim a competitor relationship unless supported by the sources

        4. Leadership Information
        - Relevant executives or leaders
        - Public statements related to the sales opportunity
        - Clearly identify information that cannot be verified

        5. Products and Services
        - Relevant products
        - Services
        - Strategic initiatives

        6. Recent Company News
        - Relevant announcements
        - Press releases
        - Strategic developments contained in the provided web content

        7. Technology and Hiring Indicators
        - Job-posting information if present
        - Technology skills or platforms mentioned
        - Other indicators of company technology direction

        8. Potential Sales Relevance
        - Explain how the verified research may relate to the product being sold
        - Clearly separate verified facts from interpretation

        9. Sources Used
        - List the supplied source URLs
        - Do not create or invent additional URLs

        IMPORTANT:
        Every factual statement must be based on the supplied web content.
        If there is insufficient evidence, say so explicitly.
        """
    )
])

research_chain = (
    research_prompt
    | model
    | StrOutputParser()
)


def run_research_agent(sales_information, web_content, source_url):
    return research_chain.invoke({
        "sales_information": sales_information,
        "web_content": web_content,
        "source_url": source_url
    })

