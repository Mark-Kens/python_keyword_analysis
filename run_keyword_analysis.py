from pathlib import Path
from datetime import datetime
from src.settings import (
    CASE_SENSITIVE,
    WHOLE_WORD_ONLY,
    KEYWORD_WORKBOOK_PATH,
    KEYWORD_SHEET_NAME,
    KEYWORD_SERVICE_COLUMN,
    KEYWORD_PRIMARY_COLUMN,
    KEYWORD_ALT1_COLUMN,
    KEYWORD_ALT2_COLUMN,
    DOCUMENT_WORKSPACE_PATH,
    INPUT_DIRECTORY_NAME,
    CACHE_DIRECTORY_NAME,
    OUTPUT_DIRECTORY_NAME,
    OUTPUT_SHEET_NAME,
)

from src.utils.keyword_list_loader import load_service_keywords_from_excel
from src.utils.text_cache_manager import (
    cache_file_exists,
    read_cached_text,
    write_cached_text,
)
from src.extractors.pdf_text_extractor import extract_text_from_pdf
from src.extractors.docx_text_extractor import extract_text_from_docx
from src.counters.keyword_frequency_counter import count_service_keyword_frequencies
from src.exporters.excel_frequency_exporter import export_keyword_counts_to_excel


def get_single_input_file(input_directory_path):
    files = [path for path in Path(input_directory_path).iterdir() if path.is_file() and not path.name.startswith("~$")]

    if len(files) == 0:
        raise FileNotFoundError(f"No input file found in: {input_directory_path}")

    if len(files) > 1:
        raise ValueError(
            f"Expected exactly one input file in {input_directory_path}, found {len(files)}."
        )

    return files[0]


def build_cache_file_path(cache_directory_path, input_file_path):
    return Path(cache_directory_path) / f"{input_file_path.stem}_extracted-text.txt"


def build_output_file_path(output_directory_path, input_file_path):
    return Path(output_directory_path) / f"{input_file_path.stem}_keyword-frequency.xlsx"


def extract_text_by_file_type(input_file_path):
    suffix = input_file_path.suffix.lower()

    if suffix == ".pdf":
        return extract_text_from_pdf(input_file_path)

    if suffix == ".docx":
        return extract_text_from_docx(input_file_path)

    raise ValueError(f"Unsupported file type: {suffix}")


if __name__ == "__main__":
    workspace_path = Path(DOCUMENT_WORKSPACE_PATH)
    input_directory_path = workspace_path / INPUT_DIRECTORY_NAME
    cache_directory_path = workspace_path / CACHE_DIRECTORY_NAME
    output_directory_path = workspace_path / OUTPUT_DIRECTORY_NAME

    input_file_path = get_single_input_file(input_directory_path)
    cache_file_path = build_cache_file_path(cache_directory_path, input_file_path)
    output_file_path = build_output_file_path(output_directory_path, input_file_path)

    if cache_file_exists(cache_file_path):
        extracted_text = read_cached_text(cache_file_path)
        print(f"Loaded cached text: {cache_file_path}")
    else:
        extracted_text = extract_text_by_file_type(input_file_path)
        write_cached_text(cache_file_path, extracted_text)
        print(f"Extracted text and saved cache: {cache_file_path}")

    service_keyword_records = load_service_keywords_from_excel(
        workbook_path=KEYWORD_WORKBOOK_PATH,
        sheet_name=KEYWORD_SHEET_NAME,
        service_column=KEYWORD_SERVICE_COLUMN,
        primary_column=KEYWORD_PRIMARY_COLUMN,
        alt1_column=KEYWORD_ALT1_COLUMN,
        alt2_column=KEYWORD_ALT2_COLUMN,
    )

    results = count_service_keyword_frequencies(
        text=extracted_text,
        service_keyword_records=service_keyword_records,
        case_sensitive=CASE_SENSITIVE,
        whole_word_only=WHOLE_WORD_ONLY,
        
    )

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file_path = output_file_path.with_name(f"{output_file_path.stem}_{timestamp}{output_file_path.suffix}")

    export_keyword_counts_to_excel(
        results=results,
        output_file_path=output_file_path,
        sheet_name=OUTPUT_SHEET_NAME,
    )

    print(f"Keyword count export completed: {output_file_path}")
