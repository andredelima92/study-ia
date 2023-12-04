import pandas as pd

# Criar DataFrames com base nos Datasets

## Carregar DataFrame de Clientes (Customers)
df_customers = pd.read_csv('./eda/churn_customers.csv')

## Mostrar 5 primeiros registros do DataFrame
fiveLines = 5
print(df_customers.head(fiveLines))

## Mostrar 5 ultimos registros do DataFrame
print(df_customers.tail(fiveLines))

## Mostrar estrutura / schema do DataFrame
print('\n')
print('Mostrar estrutura / schema do DataFrame')
print('\n')
print(df_customers.info())


df_services = pd.read_csv('./eda/churn_services.csv')

print(df_services.head(fiveLines))
print(df_services.tail(fiveLines))
print(df_services.info())

df_contracts = pd.read_csv('./eda/churn_contracts.csv')

print(df_contracts.head(fiveLines))
print(df_contracts.tail(fiveLines))
print(df_contracts.info())