import pandas as pd

df = pd.read_csv("vendas.csv", encoding="utf-8")

#Tratamento de dados
#df.isnull().sum() remove valores nulos. o que não é o nosso caso
#df.dropna(inplace=True) remove linhas com valores nulos. o que não é o nosso caso

#remove duplicatas
df = df.drop_duplicates()

#conversão
df['data'] = pd.to_datetime(df['data']) #Quando você carrega um arquivo CSV (ou cria um DataFrame), o conteúdo de uma coluna com datas geralmente vem como string. Para realizar operações com datas o Pandas precisa que seja do tipo datetime.
#pd.to_datetime() converte uma coluna de strings para o tipo datetime
#.astype() converte uma coluna para um tipo específico, que será especificado entre parênteses
df['quantidade'] = df['quantidade'].astype(int)
df['preço'] = df['preço'].astype(float)

#Criando colunas
#valor total de vendas
df['valor_total_vendas'] = df['quantidade'] * df['preço']


# quantidade de vendas no mês da venda
df['mes_venda'] = pd.to_datetime(df['data']).dt.month

#quantidade de vendas por dias da semana
df['dia_da_semana'] = pd.to_datetime(df['data']).dt.day_name()

#categoria
def categorizar(produto):
    if 'Camisa' in produto or 'Camiseta' in produto or 'Calça' in produto or 'Jaqueta' in produto or 'Bermuda' in produto or 'Blusa' in produto or 'Saia' in produto or 'Meia' in produto or 'Moletom' in produto or 'Vestido' in produto or'Blazer' in produto:
        return 'Roupas'
    elif 'Tênis' in produto or 'Bota' in produto or 'Sapatilha' in produto or 'Salto' in produto or 'Sandália' in produto or 'Chinelo' in produto:
        return 'Calçados'
    else:
        return 'Outros'

#vendas por categoria
df['categoria'] = df['produto'].apply(categorizar)
vendas_por_categoria = df.groupby('categoria')['quantidade'].sum().reset_index()
print(vendas_por_categoria)

#valor total de vendas por categoria 
valor_total_por_categoria = df.groupby('categoria')['valor_total_vendas'].sum().reset_index()
print(valor_total_por_categoria)

#valor total de vendas por mês
df['mes_vendas'] = df['data'].dt.to_period('M').astype(str)  # cria coluna mês no formato 'YYYY-MM'
valor_total_vendas_por_mes = df.groupby('mes_vendas')['valor_total_vendas'].sum().reset_index()
print(valor_total_vendas_por_mes)


print("\n🧾 Valor total por venda:")
print(df[['produto', 'quantidade', 'preço', 'valor_total_vendas']].to_string(index=False, formatters={
    'preço': 'R$ {:,.2f}'.format,
    'valor_total_vendas': 'R$ {:,.2f}'.format
}))

print("\n📅 Mês da venda:")
print(df[['data', 'mes_venda']].to_string(index=False))

print("\n📆 Dia da semana da venda:")
print(df[['data', 'dia_da_semana']].to_string(index=False))

# 🏷️ Vendas por categoria
print("\n📦 Quantidade de vendas por categoria:")
print(vendas_por_categoria.to_string(index=False))

# 💰 Valor total de vendas por categoria
valor_total_por_categoria['valor_total_vendas'] = valor_total_por_categoria['valor_total_vendas'].apply(lambda x: f"R$ {x:,.2f}")
print("\n💰 Valor total de vendas por categoria:")
print(valor_total_por_categoria.to_string(index=False))

# 📅 Valor total de vendas por mês
valor_total_vendas_por_mes['valor_total_vendas'] = valor_total_vendas_por_mes['valor_total_vendas'].apply(lambda x: f"R$ {x:,.2f}")
print("\n📆 Valor total de vendas por mês:")
print(valor_total_vendas_por_mes.to_string(index=False))


df['categoria'] = df['produto'].apply(categorizar)
#df.head() Retorna as 5 primeiras linhas do DataFrame df.
#df.head(10) Mostra as 10 primeiras linhas