import io
from pathlib import Path
from src.document_compare.data_ingestion import DocumentIngestion
from src.document_compare.document_comparator import DocumentComparatorLLM


class FakeUpload:
    """
    Wraps a local file so it behaves like a Streamlit-style uploaded file
    (has .name and .getbuffer()), for testing without a UI.
    """
    def __init__(self, file_path: Path):
        self.name = file_path.name
        self._buffer = file_path.read_bytes()

    def getbuffer(self):
        return self._buffer


def test_compare_documents():
    ref_path = Path(r"E:\Project\Document-Portal\data\document_compare\2005.14165v4.pdf")
    act_path = Path(r"E:\Project\Document-Portal\data\document_compare\NIPS-2017-attention-is-all-you-need-Paper.pdf")

    ref_upload = FakeUpload(ref_path)
    act_upload = FakeUpload(act_path)

    ingestion = DocumentIngestion(base_dir="data/document_compare")
    ingestion.save_uploaded_files(ref_upload, act_upload)

    combined_text = ingestion.combine_documents()

    print("\nCombined Text Preview (First 1000 chars):\n")
    print(combined_text[:1000])

    llm_comparator = DocumentComparatorLLM()
    comparison_df = llm_comparator.compare_documents(combined_text)

    print("\n=== COMPARISON RESULT ===")
    print(comparison_df.head())


if __name__ == "__main__":
    test_compare_documents()