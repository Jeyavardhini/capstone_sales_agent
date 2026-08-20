
import streamlit as st

from agents.sales import run_sales_agent
from agents.research import run_research_agent
from agents.analysis import run_analysis_agent
from agents.report import run_report_agent
from tools.web_research import fetch_multiple_pages


st.set_page_config(
    page_title="AI Sales Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Sales Assistant")
st.write("Generate a sales account brief using a multi-agent AI workflow.")


product_name = st.text_input("Product Name")

company_url = st.text_input("Company URL")

product_category = st.text_input("Product Category")

competitors = st.text_input("Competitors")

value_proposition = st.text_area("Value Proposition")

target_customer = st.text_input("Target Customer")
additional_urls = st.text_area(
    "Additional Research URLs",
    placeholder="Enter one URL per line"
)

uploaded_file = st.file_uploader(
    "Upload Product Overview (Optional)",
    type=["txt", "pdf", "docx"]
)
product_document_text = ""

if uploaded_file is not None:
    if uploaded_file.type == "text/plain":
        product_document_text = uploaded_file.read().decode("utf-8")



if st.button("Generate Sales Brief"):

    if not product_name:
        st.error("Please enter a product name.")

    elif not company_url:
        st.error("Please enter a company URL.")

    else:
        user_input = {
            "product_name": product_name,
            "company_url": company_url,
            "product_category": product_category,
            "competitors": competitors,
            "value_proposition": value_proposition,
            "target_customer": target_customer,
            "product_document": product_document_text
        }

        # Build list of research URLs
        source_urls = [company_url]

        if additional_urls.strip():
            extra_urls = [
                url.strip()
                for url in additional_urls.splitlines()
                if url.strip()
            ]

            source_urls.extend(extra_urls)

        with st.spinner(
            "Researching company and generating sales brief..."
        ):
            web_results = fetch_multiple_pages(source_urls)

            web_content = "\n\n".join(
                item["content"] for item in web_results
            )

            source_urls_text = "\n".join(
                item["url"] for item in web_results
            )

            sales_result = run_sales_agent(user_input)

            research_result = run_research_agent(
                sales_result,
                web_content,
                source_urls_text
            )

            analysis_result = run_analysis_agent(
                research_result
            )

            report_result = run_report_agent(
                analysis_result,
                source_urls_text
            )

        st.success("Sales brief generated!")
        st.markdown(report_result)   


          
           

   