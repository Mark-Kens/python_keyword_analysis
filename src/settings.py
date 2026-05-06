from pathlib import Path

# -----------------------------
# Matching behavior
# -----------------------------
CASE_SENSITIVE = False
WHOLE_WORD_ONLY = True
# EXACT_PHRASE_MATCH = True

# -----------------------------
# Keyword input file settings
# -----------------------------
KEYWORD_WORKBOOK_PATH = Path("keywords/aws_keywords.xlsx")
KEYWORD_SHEET_NAME = "keywords"

KEYWORD_SERVICE_COLUMN = "Service"
KEYWORD_PRIMARY_COLUMN = "PrimaryKeyword"
KEYWORD_ALT1_COLUMN = "AltKeyword1"
KEYWORD_ALT2_COLUMN = "AltKeyword2"

# -----------------------------
# Active workspace document
# -----------------------------
DOCUMENT_WORKSPACE_PATH = Path("workspace/source_1/source_1_set-01")
INPUT_DIRECTORY_NAME = "input"
CACHE_DIRECTORY_NAME = "cache"
OUTPUT_DIRECTORY_NAME = "output"

# -----------------------------
# Output settings
# -----------------------------
OUTPUT_SHEET_NAME = "keyword_counts"
OUTPUT_COLUMNS = [
    "Service",
    "PrimaryKeyword",
    "PrimaryKeywordCount",
    "AltKeyword1",
    "AltKeyword1Count",
    "AltKeyword2",
    "AltKeyword2Count",
    "TotalCount",
]
