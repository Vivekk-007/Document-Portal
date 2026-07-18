from langchain_core.prompts import ChatPromptTemplate

# Prompt for document analysis
document_analysis_prompt = ChatPromptTemplate.from_template("""
You are an expert document analysis assistant.

Read the following document carefully and extract:

- Title
- Authors
- Summary
- Keywords
- Technologies
- Main Topics
- Publication Year (if available)

Return the information according to the schema provided by the system.

Document:
{document_text}
""")

# Prompt for document comparison
document_comparison_prompt = ChatPromptTemplate.from_template("""
You will be provided with content from two PDFs. Your tasks are as follows:

1. Compare the content in two PDFs
2. Identify the difference in PDF and note down the page number 
3. The output you provide must be page wise comparison content 
4. If any page do not have any change, mention as 'NO CHANGE' 

Input documents:

{combined_docs}

Your response should follow this format:

{format_instruction}
""")

PROMPT_REGISTRY = {
    "document_analysis": document_analysis_prompt,
    "document_comparison": document_comparison_prompt,   # fixed typo: was "document_comparision"
}