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


#divide o dataset em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#cria e configura o random forest
model = RandomForestClassifier(n_estimators=100, random_state=42)

#treina o modelo
model.fit(X_train, y_train)

#faz previsões
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print(f"\nAcurácia geral: {accuracy:.4f}")

#gera a matriz de confusão
conf_matrix = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 6))

#cria o gráfico
sns.heatmap(
    conf_matrix,
    annot=True,            
    fmt='d',              
    cmap="Pinks",         
    xticklabels=["PCOS Não", "PCOS Sim"],  
    yticklabels=["PCOS Não", "PCOS Sim"]   
)

plt.title("Matriz de Confusão")
plt.xlabel("Previsões")
plt.ylabel("Valores Reais")

plt.show()

#pega a importância dos dados
importances = model.feature_importances_
feature_names = X.columns

#cria um dataframe
feat_importances = pd.DataFrame({
    'Feature': feature_names,
    'Importance': importances
})

#ordena as features
feat_importances = feat_importances.sort_values(by='Importance', ascending=False)

plt.figure(figsize=(10, 6))

#cria o gráfico
sns.barplot(x='Importance', y='Feature', data=feat_importances, palette='viridis')

plt.title('Importância das Features')
plt.xlabel('Importância')
plt.ylabel('Features')

plt.show()
