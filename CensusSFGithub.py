#local de download da planilha
# https://data.sfgov.org/City-Management-and-Ethics/Employee-Compensation/88g8-5mnd/about_data


#habilitando pandas
import pandas as pd

# importando arquivo
Compensation = "localdoarquivo.csv"
df = pd.read_csv(Compensation)

# Ajustando para exibir todas as colunas
pd.set_option('display.max_columns', None)

#visualizando somente as primeiras linhas agora com todas as colunas
df.head()

#visualizando o tipo do arquivo
type(df)

#Visualizando quantas linhas e colunas
df.shape

#Verificando todas os nomes de colunas do conjunto
df.columns

#filtrar colunas desejadas
colunas_desejadas = ['Organization Group Code', 'Job Family Code', 'Job Code', 'Year Type',
       'Year', 'Organization Group', 'Department', 'Union Code', 'Job', 'Employee Name', 
       'Salaries', 'Overtime', 'Other Salaries', 'Total Salary', 'Retirement', 'Health and Dental',
       'Other Benefits', 'Total Benefits', 'Total Compensation']


#cria a planilha com as colunas filtradas       
df_filtrado = df[colunas_desejadas]

#tratando missing values
missing_departments = df_filtrado[df_filtrado['Department'].isna()]
print(missing_departments)

#confirmando os departments dos Police Officer e Sheriff que são os missings
police_sheriff_dpt = df_filtrado[df_filtrado['Job'].isin(['Police Officer 2', "Sheriff's Cadet"])]

# Exibir as primeiras 5 linhas do DataFrame filtrado, mostrando as colunas de interesse
print(police_sheriff_dpt[['Job', 'Department']].head(5))
print(police_sheriff_dpt[['Job', 'Department']].tail(5))

#Substituindo missing numbers
df_filtrado.loc[896129, 'Department'] = 'Sheriff'
df_filtrado.loc[956127, 'Department'] = 'POL Police'

#Visualizando correção
print(df_filtrado.loc[[896129,956127], ['Job','Department']])


# Salvar o DataFrame modificado em um arquivo csv
df_filtrado.to_csv('Employee_Compensation_Final.csv', index=False)







