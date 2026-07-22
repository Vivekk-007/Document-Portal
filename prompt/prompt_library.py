from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# ==========================================================
# Document Analysis Prompt
# ==========================================================

document_analysis_prompt = ChatPromptTemplate.from_template("""
You are an expert document analysis assistant.

Analyze the following document and extract:

- Title
- Authors
- Summary
- Keywords
- Technologies
- Main Topics
- Publication Year (if available)

Return the information according to the required schema.

Document:
{document_text}
""")

# ==========================================================
# Document Comparison Prompt
# ==========================================================

document_comparison_prompt = ChatPromptTemplate.from_template("""
You are an expert document comparison assistant.

Compare the following two documents.

Tasks:
1. Compare both documents page by page.
2. Identify all differences.
3. Mention the page number for each difference.
4. If a page has no differences, write "NO CHANGE".
5. Keep the output structured and easy to read.

Documents:

{combined_docs}

Return your answer using this format:

{format_instruction}
""")

# ==========================================================
# Contextualize Question Prompt
# ==========================================================

contextualize_question_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
Given the chat history and the latest user question,
rewrite the latest question so it can be understood
without the chat history.

Instructions:
- Do NOT answer the question.
- Preserve the original meaning.
- If the question is already standalone,
  return it unchanged.
- Return ONLY the rewritten question.
            """,
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
    ]
)

# ==========================================================
# Context QA Prompt
# ==========================================================

context_qa_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an intelligent document question-answering assistant.

Answer ONLY using the provided context.

Instructions:
- Use only the retrieved context.
- If the answer is not found, say:
  "I don't know based on the provided document."
- Do not hallucinate.
- Keep answers accurate and concise.
- Use bullet points whenever appropriate.

Retrieved Context:

{context}
            """,
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
    ]
)

# ==========================================================
# Registry
# ==========================================================

PROMPT_REGISTRY = {
    "document_analysis": document_analysis_prompt,
    "document_comparison": document_comparison_prompt,
    "contextualize_question": contextualize_question_prompt,
    "context_qa": context_qa_prompt,
}