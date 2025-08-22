import pandas as pd

def preprocess(parsed_logs):
    df = pd.DataFrame(parsed_logs)
    df.fillna("unknown", inplace=True)
    return df
