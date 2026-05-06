from pathlib import Path
import pandas as pd


def export_keyword_counts_to_excel(results, output_file_path, sheet_name="keyword_counts"):
    output_file_path = Path(output_file_path)
    output_file_path.parent.mkdir(parents=True, exist_ok=True)

    dataframe = pd.DataFrame(results)
    dataframe.to_excel(output_file_path, index=False, sheet_name=sheet_name)
