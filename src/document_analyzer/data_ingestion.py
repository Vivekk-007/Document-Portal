import os
import fitz
import uuid
from datetime import datetime
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException


class DocumentHandler:
    """
    A handler for managing document-related operations.
    """
    def __init__(self):
        self.logger = CustomLogger().get_logger(__name__)

    def save_pdf(self, file_path: str) -> str:
        """
        Extract text from a PDF file using PyMuPDF (fitz).
        """
        try:
            self.logger.info(f"Extracting text from PDF: {file_path}")
            doc = fitz.open(file_path)
            text = ""
            for page in doc:
                text += page.get_text()
            doc.close()
            return text
        except Exception as e:
            self.logger.error(f"Error extracting text from PDF: {e}")
            raise DocumentPortalException("Failed to extract text from PDF", e)
        
    def read_pdf(self, file_path: str) -> str:
        """
        Read a PDF file and return its text content.
        """
        try:
            self.logger.info(f"Reading PDF: {file_path}")
            return self.save_pdf(file_path)
        except Exception as e:
            self.logger.error(f"Error reading PDF: {e}")
            raise DocumentPortalException("Failed to read PDF", e)