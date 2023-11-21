import pandas as pd
import json

# DataFrame
#data_df = pd.read_csv("data/titanic.csv")
data_df = pd.read_json("data/tasa.json", orient='index')


with open('data/out/split_json', 'w') as f:
    result = data_df.to_json(orient="split")
    parsed = json.loads(result)
    f.write(json.dumps(parsed, indent=3))

with open('data/out/records_json', 'w') as f:
    result = data_df.to_json(orient="records")
    parsed = json.loads(result)
    f.write(json.dumps(parsed, indent=3))

with open('data/out/index_json', 'w') as f:
    result = data_df.to_json(orient="index")
    parsed = json.loads(result)
    f.write(json.dumps(parsed, indent=3))

with open('data/out/columns_json', 'w') as f:
    result = data_df.to_json(orient="columns")
    parsed = json.loads(result)
    f.write(json.dumps(parsed, indent=3))

with open('data/out/values_json', 'w') as f:
    result = data_df.to_json(orient="values")
    parsed = json.loads(result)
    f.write(json.dumps(parsed, indent=3))

with open('data/out/table_json', 'w') as f:
    result = data_df.to_json(orient="table")
    parsed = json.loads(result)
    f.write(json.dumps(parsed, indent=3))

