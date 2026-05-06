# python_keyword_analysis

Python project for extracting text from source documents and counting keyword frequencies, with export to Excel.

## Project Structure

```text
python_keyword_analysis/
├── keywords/
│   └── aws_keywords.xlsx
├── src/
│   ├── counters/
│   │   └── keyword_frequency_counter.py
│   ├── exporters/
│   │   └── excel_frequency_exporter.py
│   ├── extractors/
│   │   ├── docx_text_extractor.py
│   │   └── pdf_text_extractor.py
│   ├── utils/
│   │   ├── keyword_list_loader.py
│   │   └── text_cache_manager.py
│   └── settings.py
├── workspace/
│   └── source_1/
│       └── source_1_set-01/
│           ├── cache/
│           │   └── .gitkeep
│           ├── input/
│           │   └── .gitkeep
│           └── output/
│               └── .gitkeep
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── run_keyword_analysis.py
```

## Notes

- `aws_keywords.xlsx` is intentionally present as a 6-row template.
- The `workspace/` directories include `.gitkeep` files so the folder structure is preserved in Git.
- Input, cache, and output folders are included as empty placeholders for runtime use.

## Purpose

This project is designed to:

- extract text from supported source documents
- load keyword definitions from an Excel workbook
- count keyword frequencies
- export results to Excel

## Main Components

- `run_keyword_analysis.py` — main entry point
- `src/extractors/` — document text extraction logic
- `src/utils/` — utility helpers for keyword loading and text caching
- `src/counters/` — keyword counting logic
- `src/exporters/` — Excel export logic
- `keywords/` — keyword workbook location
- `workspace/` — runtime working area for input, cache, and output

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the project

```bash
python run_keyword_analysis.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
