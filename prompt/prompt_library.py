from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("""
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