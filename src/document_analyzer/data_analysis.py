import sys

from utils.model_loader import ModelLoader
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException

from model.models import Metadate
from prompt.prompt_library import prompt


class DocumentAnalyzer:
    """
    Analyzes documents using a pre-trained model.
    Automatically logs all actions and supports session-based organization.
    """

    def __init__(self):
        self.log = CustomLogger().get_logger(__name__)
        try:
            self.loader = ModelLoader()
            self.llm = self.loader.load_llm()
            # Structured Output
            self.structured_llm = self.llm.with_structured_output(Metadate)
            self.prompt = prompt
            self.log.info("DocumentAnalyzer initialized successfully.")

        except Exception as e:
            self.log.error(f"Error initializing DocumentAnalyzer: {e}")
            raise DocumentPortalException(e, sys)

    def analyze_document(self, document_text: str) -> dict:
        """
        Analyze a document's text and extract structured metadata.
        """

        try:
            chain = self.prompt | self.structured_llm
            self.log.info("Metadata analysis chain initialized.")
            response = chain.invoke(
                {
                    "document_text": document_text
                }
            )

            self.log.info("Metadata extraction successful.")
            # Return dictionary
            return response.model_dump()

        except Exception as e:
            self.log.error(f"Metadata analysis failed: {e}")
            raise DocumentPortalException(e, sys)