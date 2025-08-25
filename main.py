import json
import pandas as pd


def main():
    ndjson_file_path = "input/polyfet-logs.ndjson"
    output_excel_file = "output/polyfet-logs.xlsx"

    # Read the NDJSON file
    with open(ndjson_file_path, "r") as ndjson_file:
        data = [json.loads(line) for line in ndjson_file]

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Write to Excel
    df.to_excel(output_excel_file, index=False)

    print(f"Successfully converted NDJSON to Excel: {output_excel_file}")


if __name__ == "__main__":
    main()
