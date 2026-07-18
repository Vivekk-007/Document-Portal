import sys
from dotenv import load_dotenv
import pandas as pd
from langchain_core.output_parsers import JsonOutputParser
from langchain_classic.output_parsers import OutputFixingParser
from utils.model_loader import ModelLoader
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from prompt.prompt_library import PROMPT_REGISTRY
from model.models import SummaryResponse, PromptType

log = CustomLogger().get_logger(__name__)


class DocumentComparatorLLM:
    def __init__(self):
        load_dotenv()
        self.log = log  # bind module logger onto the instance
        self.loader = ModelLoader()
        self.llm = self.loader.load_llm()
        self.parser = JsonOutputParser(pydantic_object=SummaryResponse)
        self.fixing_parser = OutputFixingParser.from_llm(parser=self.parser, llm=self.llm)
        self.prompt = PROMPT_REGISTRY[PromptType.DOCUMENT_COMPARISON.value]
        self.chain = self.prompt | self.llm | self.fixing_parser
        self.log.info("DocumentComparatorLLM initialized")

    def compare_documents(self, combined_docs: str) -> pd.DataFrame:
        """
        Compares two documents and returns a structured comparison.
        """
        try:
            inputs = {
                "combined_docs": combined_docs,
                "format_instruction": self.parser.get_format_instructions()
            }
            self.log.info("Starting document comparison")
            response = self.chain.invoke(inputs)
            self.log.info("Document comparison completed")
            return self._format_response(response)

        except Exception as e:
            self.log.error(f"Error in compare_documents: {e}")
            raise DocumentPortalException("An error occurred while comparing documents.", sys)

    def _format_response(self, response_parsed: list[dict]) -> pd.DataFrame:  # type: ignore
        """
        Formats the response from the LLM into a structured format.
        """
        try:
            df = pd.DataFrame(response_parsed)
            self.log.info("Response formatted into DataFrame", rows=len(df))
            return df
        except Exception as e:
            self.log.error(f"Error formatting response into DataFrame: {e}")
            raise DocumentPortalException("Error formatting response", sys)