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
df['valor_total'] = df['quantidade'] * df['preço']
total_geral = df['valor_total'].sum().round(2)
print(f"\nValor Total de Todas as Vendas: R$ {total_geral:,.2f}")

# quantidade e valor de vendas por mês
df['mes_venda'] = pd.to_datetime(df['data']).dt.month
df['valor_total'] = df['quantidade'] * df['preço'] #criando a coluna valor total 
vendas_por_mes = df.groupby('mes_venda')[['quantidade', 'valor_total']].sum()#agrupa os dados por mês e soma as quantidade e valores
print("\nResumo de Vendas por Mês:")
print(vendas_por_mes)

#quantidade de vendas por dias da semana
df['dia_da_semana'] = pd.to_datetime(df['data']).dt.day_name()
vendas_por_dia = df.groupby('dia_da_semana')['quantidade'].sum() #agrupa os dados por dia da semana e soma as quantidades
ordem_dias = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] #para garantir a ordem
vendas_por_dia = vendas_por_dia.reindex(ordem_dias) #reordena ou reorganiza os dados de uma Series ou DataFrame com base em uma nova ordem de índices que você fornece.
print("\n Vendas por Dia da Semana:")
print(vendas_por_dia)

#categoria
def categorizar(produto):
    if 'Camisa' in produto or 'Camiseta' in produto or 'Calça' in produto or 'Jaqueta' in produto or 'Bermuda' in produto or 'Blusa' in produto or 'Saia' in produto or 'Meia' in produto or 'Moletom' in produto or 'Vestido' in produto or'Blazer' in produto:
        return 'Roupas'
    elif 'Tênis' in produto or 'Bota' in produto or 'Sapatilha' in produto or 'Salto' in produto or 'Sandália' in produto or 'Chinelo' in produto:
        return 'Calçados'
    else:
        return 'Outros'

#vendas por categoria
df['categoria'] = df['produto'].apply(categorizar)#.apply(categorizar) aplica a função categorizar() a cada valor da coluna produto
df['valor_total'] = df['quantidade'] * df['preço']
vendas_por_categoria = df.groupby('categoria')['quantidade'].sum().reset_index()
valor_total_por_categoria = df.groupby('categoria')['valor_total'].sum().reset_index()
print("\n Quantidade de vendas por categoria:")
print(vendas_por_categoria.to_string(index=False)) #.to_string() é um método do pandas que converte um DataFrame ou Series em uma string formatada, para exibição bonita no terminal ou logs. Quando você passa index=False, está dizendo para não mostrar a coluna de índices (os números que ficam na esquerda, tipo 0, 1, 2 etc)
print("\n Valor Total de Vendas por Categoria:")
print(valor_total_por_categoria.to_string(index=False))


#valor total de vendas por mês
df['mes_vendas'] = df['data'].dt.to_period('M').astype(str)  # cria coluna mês no formato 'YYYY-MM'
valor_total_vendas_por_mes = df.groupby('mes_vendas')['valor_total'].sum().reset_index()
valor_total_vendas_por_mes['valor_total'] = valor_total_vendas_por_mes['valor_total'].apply(lambda x: f"R$ {x:,.2f}") #def é um equivalente de lambda, que é uma função anônima em py. A função lambda formata o valor total para o formato monetário br
print("\n Valor total de vendas por mês:")
print(valor_total_vendas_por_mes.to_string(index=False))


df['categoria'] = df['produto'].apply(categorizar)
#df.head() Retorna as 5 primeiras linhas do DataFrame df.
#df.head(10) Mostra as 10 primeiras linhas