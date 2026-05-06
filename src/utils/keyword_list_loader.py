import pandas as pd


def load_service_keywords_from_excel(
    workbook_path,
    sheet_name,
    service_column,
    primary_column,
    alt1_column,
    alt2_column,
):
    dataframe = pd.read_excel(workbook_path, sheet_name=sheet_name)

    required_columns = [
        service_column,
        primary_column,
        alt1_column,
        alt2_column,
    ]

    missing_columns = [column for column in required_columns if column not in dataframe.columns]
    if missing_columns:
        raise ValueError(
            f"Missing required columns in sheet '{sheet_name}': {missing_columns}. "
            f"Available columns: {list(dataframe.columns)}"
        )

    records = []

    for _, row in dataframe.iterrows():
        service = row[service_column]
        primary_keyword = row[primary_column]
        alt_keyword_1 = row[alt1_column]
        alt_keyword_2 = row[alt2_column]

        service = "" if pd.isna(service) else str(service).strip()
        primary_keyword = "" if pd.isna(primary_keyword) else str(primary_keyword).strip()
        alt_keyword_1 = "" if pd.isna(alt_keyword_1) else str(alt_keyword_1).strip()
        alt_keyword_2 = "" if pd.isna(alt_keyword_2) else str(alt_keyword_2).strip()

        if service == "":
            continue

        records.append(
            {
                "Service": service,
                "PrimaryKeyword": primary_keyword,
                "AltKeyword1": alt_keyword_1,
                "AltKeyword2": alt_keyword_2,
            }
        )

    return records
