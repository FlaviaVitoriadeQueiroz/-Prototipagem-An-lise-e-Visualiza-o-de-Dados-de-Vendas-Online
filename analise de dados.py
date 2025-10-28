import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Lendo o CSV
df = pd.read_csv("B:\\VScode\\Python\\projeto loja online\\vendas.csv", encoding="utf-8")

# Criando o gráfico quantidade de vendas por produto
sns.barplot(data=df, x='quantidade', y='produto')
plt.title("Quantidade de Vendas por Produto")
plt.xlabel("Quantidade")
plt.ylabel("Produto")

plt.show()

# Criando o gráfico valor por produto durante os ultimos 6 meses
sns.barplot(data=df, x='preço', y='produto')
plt.title("Valor por Produto")
plt.xlabel("Preço")
plt.ylabel("Produto")

plt.show()


# Criar a coluna de categoria manualmente (exemplo)
def definir_categoria(produto):
    if produto in ['Calça', 'Camisa', 'Camiseta', 'Blusa', 'Jaqueta', 'Saia', 'Bermuda', 'Moletom', 'Blazer', 'Vestido']:
        return 'roupas'
    elif produto in ['Tênis', 'Bota', 'Salto', 'Sapatilha', 'Chinelo', 'Sandália']:
        return 'calçados'
    elif produto in ['Meia', 'Boné']:
        return 'acessórios'
    else:
        return 'outros'

df['categoria'] = df['produto'].apply(definir_categoria)

#valor dos produtos por categoria
sns.barplot(data=df, x='preço', y='categoria')
plt.title("Valor por Categoria")
plt.xlabel("Preço")
plt.ylabel("Categoria")

plt.show()





