from agents.report import run_report_agent
from agents.sales import run_sales_agent
from agents.research import run_research_agent
from agents.analysis import run_analysis_agent
from tools.web_research import fetch_multiple_pages


sample_input = {
    "product_name": "Cloud Data Platform",
    "company_url": "https://www.example.com",
    "product_category": "Cloud Data",
    "competitors": "Snowflake, Databricks",
    "value_proposition": "Helps organizations centralize and analyze data in the cloud.",
    "target_customer": "Chief Data Officer"
}

# Collect website sources
source_urls = [
    sample_input["company_url"]
]

# Read all webpages
web_results = fetch_multiple_pages(source_urls)

# Combine webpage content
web_content = "\n\n".join(
    item["content"] for item in web_results
)

# Combine source URLs
source_urls_text = "\n".join(
    item["url"] for item in web_results
)

print("\n===== WEBSITE CONTENT =====")
print(web_content[:1000])

print("\n===== SOURCE URLS =====")
print(source_urls_text)

# Step 1: Sales Agent
sales_result = run_sales_agent(sample_input)

print("===== SALES AGENT =====")
print(sales_result)


# Step 2: Research Agent
research_result = run_research_agent(
    sales_result,
    web_content,
    source_urls_text
)
    
    

print("\n===== RESEARCH AGENT =====")
print(research_result)


# Step 3: Analysis Agent
analysis_result = run_analysis_agent(research_result)

print("\n===== ANALYSIS AGENT =====")
print(analysis_result)

# Step 4: Report Agent
report_result = run_report_agent(
    analysis_result,
    source_urls_text
)
print("\n===== FINAL SALES REPORT =====")
print(report_result)