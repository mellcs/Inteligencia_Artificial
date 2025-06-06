import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

#carrega o dataset
dataset = pd.read_csv("pcos_dataset.csv")

print("Colunas do Dataset:")
print(dataset.columns.tolist())

print("\nDados faltantes por coluna:")
print(dataset.isnull().sum())

#separa a variável alvo (y) das outras variáveis (x) 
X = dataset.drop(columns=["Diagnostico_PCOS"])
y = dataset["Diagnostico_PCOS"]

#gráfico de barras de distribuição das classes
plt.figure(figsize=(5, 5))
sns.countplot(x=y, palette='pastel')
plt.title("Distribuição das Classes (PCOS)")
plt.xlabel("Diagnóstico PCOS")
plt.ylabel("Contagem")
plt.xticks([0,1], ["PCOS Não", "PCOS Sim"])
plt.show()

#gráfico de correlação entre variáveis
plt.figure(figsize=(10, 8))
correlation = dataset.corr()  #calcula a matriz
sns.heatmap(correlation, cmap='coolwarm', annot=False)  #cria mapa
plt.title("Mapa de Calor das Correlações")
plt.show()

#seleciona 3 primeiras features
top_features = X.columns[:3]

#cria um histograma para cada uma
for feature in top_features:
    plt.figure(figsize=(6, 4))
    sns.histplot(data=dataset, x=feature, hue="Diagnostico_PCOS", multiple="stack", palette="pastel")
    plt.title(f"Distribuição de {feature} por Diagnóstico PCOS")
    plt.xlabel(feature)
    plt.ylabel("Frequência")
    plt.show()

#divide os dados de treino e os dados de teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#treina o modelo random forest, pega os dados de treino
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

#faz as previsões
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"\nAcurácia geral: {accuracy:.4f}")

conf_matrix = confusion_matrix(y_test, y_pred)

#cria o gráfico de matriz de confusão
plt.figure(figsize=(6, 6))
sns.heatmap(
    conf_matrix,
    annot=True,
    fmt='d',
    cmap="RdPu",
    xticklabels=["PCOS Não", "PCOS Sim"],
    yticklabels=["PCOS Não", "PCOS Sim"]
)
plt.title("Matriz de Confusão")
plt.xlabel("Previsões")
plt.ylabel("Valores Reais")
plt.show()

#importância das features
importances = model.feature_importances_ 
feature_names = X.columns

feat_importances = pd.DataFrame({
    'Feature': feature_names,
    'Importance': importances
})

#ordena as features por importância, cria o gráfico de barras
feat_importances = feat_importances.sort_values(by='Importance', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=feat_importances, palette='magma')
plt.title('Importância das Features')
plt.xlabel('Importância')
plt.ylabel('Features')
plt.show()
