import pandas as pd
from fastapi import HTTPException


def get_dataframe(path: str) -> pd.DataFrame:
    try:
        if path.endswith('.csv'):
            df = pd.read_csv(path)
        elif path.endswith('.xlsx'):
            df = pd.read_excel(path)
    except Exception as e: 
        #TODO: Logging needs to be implemented
        print(f"HTTPException 500 raised: {e}")
        raise HTTPException(500, "Internal Server Error")
    return df

def get_synopsis(path: str):
    
    df = get_dataframe(path)

    synopsis = {"columns": []}

    for column in df.columns:
        
        header = df[column].name

        type = get_data_type(df[column].dtype)

        sample = get_sample(df[column].values.tolist())

        column_dict = {
            "header": header,
            "type": type,
            "Sample": sample
        }
        synopsis["columns"].append(column_dict)

    return synopsis

def get_data_type(df_dtype: str) -> str:
    if df_dtype == "int64" or df_dtype == "float64":
        type = "Number"
    elif df_dtype == "datetime64":
        # TODO: CSV Dates to be parsed as date data type, currently identified as "Text"
        type = "Date"
    else:
        type = "Text"
    return type

def get_sample(column_values: list) -> list:
    # remove duplicate values
    unique_col_values = list(dict.fromkeys(column_values))

    # remove nan - assuming we are not wanting null values
    unique_col_values = [val for val in unique_col_values if not(pd.isnull(val)) == True]

    if len(unique_col_values) < 5:
        return unique_col_values
    else:
        return unique_col_values[0:5]