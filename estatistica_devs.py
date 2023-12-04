import pandas as pd
print(pd.__version__)

dict_medidas = {
    'idade': [15, 18, 25, 25, 40, 55, 58, 60, 80],
    'altura': [160, 162, 165, 168, 172, 174, 174, 174, 176]
}


df_medidas = pd.DataFrame.from_dict(dict_medidas)

print(df_medidas)

# Média
print('Média')
print(df_medidas['idade'].mean())
print('\n')

# Mediana
print('Mediana')
print(df_medidas['idade'].median())
print('\n')

# Moda
print('Moda')
print(df_medidas['idade'].mode())
print('\n')

# Moda altura
print('Moda altura')
print(df_medidas['altura'].mode())
print('\n')

# Medidas de dispersão

# Variância
print('Variância ')
print(df_medidas.idade.var())
print('\n')

print('Variância em valores absolutos de acordo com os dados')
print(df_medidas.idade.std())
print('\n')


# Coeficiente de Variação em percentual (Idade)
print('Coeficiente de Variação - IDADE')
coeficienteIdade = df_medidas.idade.std() / df_medidas.idade.mean() * 100
print(coeficienteIdade)
print('\n')

print('Coeficiente de Variação - ALTURA')
coeficienteAltura = df_medidas.altura.std() / df_medidas.altura.mean() * 100
print(coeficienteAltura)
print('\n')


# Assimetria - Idade (Positiva pois a cauda direita é mais longa)
print('Assimetria - Idade')
assimetriaIdade = df_medidas.idade.skew()
print(assimetriaIdade)
print('\n')

# Assimetria - Altura (Negativa pois a cauda esquerda é mais longa)
print('Assimetria - Altura')
assimetriaAltura = df_medidas.altura.skew()
print(assimetriaAltura)
print('\n')

# Curtose - Idade (Leptocúrtica)
print('Curtose - Idade')
curtose = df_medidas.idade.kurtosis()
print(curtose)
print('\n')

# Curtose - Altura (Platicúrtica)
print('Curtose - Altura')
curtoseAltura = df_medidas.altura.kurtosis()
print(curtoseAltura)
print('\n')

# Obter medidas estatísticas
print('Medidas')
medidas = df_medidas.idade.describe()
print(medidas)
print('\n')


### Correlação de variáveis

# Correlação do DataFrame
print('Correlação de Pearson')
corrPearson = df_medidas.corr(method='pearson')
print(corrPearson)
print('\n')

# Correlação entre duas variaveis
print('Correlação entre duas variaveis')
corrVar = df_medidas.idade.corr(df_medidas.altura, method='pearson')
print(corrVar)
print('\n')