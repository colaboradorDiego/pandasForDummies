import pandas as pd
import json

# DataFrame
titanic_df = pd.read_csv("data/titanic.csv")


with open('data/split_json', 'w') as f:
    result = titanic_df.to_json(orient="split")
    parsed = json.loads(result)
    f.write(json.dumps(parsed, indent=3))

with open('data/records_json', 'w') as f:
    result = titanic_df.to_json(orient="records")
    parsed = json.loads(result)
    f.write(json.dumps(parsed, indent=3))

with open('data/index_json', 'w') as f:
    result = titanic_df.to_json(orient="index")
    parsed = json.loads(result)
    f.write(json.dumps(parsed, indent=3))

with open('data/columns_json', 'w') as f:
    result = titanic_df.to_json(orient="columns")
    parsed = json.loads(result)
    f.write(json.dumps(parsed, indent=3))

with open('data/values_json', 'w') as f:
    result = titanic_df.to_json(orient="values")
    parsed = json.loads(result)
    f.write(json.dumps(parsed, indent=3))

with open('data/table_json', 'w') as f:
    result = titanic_df.to_json(orient="table")
    parsed = json.loads(result)
    f.write(json.dumps(parsed, indent=3))

