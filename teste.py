import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Configuração do tema do seaborn
sns.set_theme()

# Carregando os dados
dados = pd.read_csv(r"C:\Users\ronal\Documents\Analise dados dataset animes 2024 POWER BI\Top_Anime_data.csv")

# Verifica as colunas do dataset
print(dados.columns)

# Seleciona apenas colunas numéricas para a matriz de correlação
dados_numericos = dados.select_dtypes(include=['number'])

# Cria a matriz de correlação
correlacao = dados_numericos.corr()

# Criando o heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlacao, annot=True, fmt=".2f", cmap="YlGnBu", linewidths=0.5)

# Adiciona título
plt.title('Heatmap de Correlação entre Variáveis Numéricas', fontsize=14)

# Exibe o gráfico
plt.show()
