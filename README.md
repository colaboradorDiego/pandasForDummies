# pandasForDummies
Learning pandas con python

# Crear DataFrame

La [forma](https://www.geeksforgeeks.org/different-ways-to-create-pandas-dataframe/) mas simple de crear

```
data = []
index = []
columns = []
pandas.DataFrame(data, index, columns)
```

https://www.alpharithms.com/python-financial-data-491110/
https://towardsdatascience.com/how-to-store-financial-market-data-for-backtesting-84b95fc016fc
https://stackoverflow.com/questions/41010937/python-filter-list-of-dictionaries-based-on-multiple-keys

[Pandas](https://pandas.pydata.org/)

### Titanic sample data

This tutorial uses the Titanic data set, stored as CSV. The data consists of the following data columns:

| Dato | Detalle |
| ---- | ------- |
| PassengerId | Id of every passenger |
| Survived | This feature have value 0 (not survived) and 1 (survived) |
| Pclass | There are 3 classes: Class 1, Class 2 and Class 3 |
| Name | Name of passenger |
| Sex | Gender of passenger |
| Age | Age of passenger |
| SibSp | Indication that passenger have siblings (hemanos) and spouse (conyugue) |
| Parch | Whether a passenger is alone or have family |
| Ticket | Ticket number of passenger |
| Fare | Indicating the fare (tarifa) |
| Cabin | The cabin of passenger |
| Embarked | The embarked category |


### How do I read and write tabular data?

Pandas supports the integration with many file formats or data sources out of the box (csv, excel, sql, json, parquet,…). Importing data from each of these data sources is provided by function with the prefix read_. Similarly, the to_ methods are used to store data.

Asi leemos los datos del csv y creamos un *DataFrame*, aquie el [Tutorial completo](https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html#min-tut-02-read-write)

`titanic = pd.read_csv("data/titanic.csv")`

- First & Last 5 rows will be shown by default: `titanic`
- First 8 rows: `titanic.head(8)`
- Last 10 rows: `titanic.tail(10)`

Titanic dtypes attribute `titanic.dtypes`

Titanic technical summary:  `titanic.info()`

Tambien podemos exportar el [DataFrame.to_excel](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html?highlight=dataframe%20to_excel#pandas.DataFrame.to_excel) asi como el [DataFrame.to_json](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_json.html?highlight=dataframe%20to_json#pandas.DataFrame.to_json)

```
titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)

titanic.to_json("titanic.xlsx", sheet_name="passengers", index=False)
```


### Working with real tima data

[NEVER grow a DataFrame!](https://stackoverflow.com/questions/13784192/creating-an-empty-pandas-dataframe-then-filling-it/56746204#56746204)


### Binance stock md

[cliente binance](https://github.com/Uruzmag15/ticker_stream)


[payload symbol@bookTicker](https://binance-docs.github.io/apidocs/futures/en/#all-market-tickers-streams)

```
{
  "e":"bookTicker",         // event type
  "u":400900217,            // order book updateId
  "E": 1568014460893,       // event time
  "T": 1568014460891,       // transaction time
  "s":"BNBUSDT",            // symbol
  "b":"25.35190000",        // best bid price
  "B":"31.21000000",        // best bid qty
  "a":"25.36520000",        // best ask price
  "A":"40.66000000"         // best ask qty
}
```

