<div align=center>
  
# Previsor estelar

<img src="deploy_star_app.gif"/>
</div>

---
Este é um aplicativo web que utiliza aprendizado de máquina para prever o tipo de uma estrela com base em suas características. O modelo de aprendizado de máquina foi treinado usando dados astrofísicos, incluindo a Lei de Stefan-Boltzmann, Lei de deslocamento de Wienn, relação de magnitude absoluta, e paralaxe para calcular a temperatura, luminosidade, raio, magnitude absoluta, cor e classe espectral de uma estrela.

- 🌌  [app previsor estelar](https://previsor-estelar.streamlit.app/)

## Propósito
O conjunto de dados e este aplicativo foram desenvolvidos com o objetivo de analisar e classificar estrelas, identificando padrões em seus dados. As características das estrelas são representadas em gráficos Hertzsprung-Russell e Diagrama HR-Diagram para fornecer uma visão visual da distribuição das estrelas no espaço celeste.

## Como Usar
- Filtros: Utilize a barra lateral para ajustar as características da estrela que você deseja classificar, incluindo temperatura, luminosidade, raio, magnitude absoluta, cor e classe espectral.

- Previsão: Clique no botão "Prever" para obter uma previsão do tipo da estrela com base nas características fornecidas.

- Resultados: O aplicativo exibirá o resultado da previsão, indicando se a estrela é uma Anã Marrom, Anã Vermelha, Anã Branca, Estrela da Sequência Principal, Super Gigante ou Hiper Gigante.

## Visualizações Adicionais
O aplicativo inclui imagens e informações adicionais para cada tipo de estrela previsto, proporcionando uma experiência educativa sobre diferentes classes estelares.

## Observação
O conjunto de dados é construído com base em equações astrofísicas, incluindo a Lei de Stefan-Boltzmann, Lei de deslocamento de Wienn, relação de magnitude absoluta e paralaxe.

<div align=center>
  
# Previsão do Tipo de Estrela com machine learning
<img src="https://olhardigital.com.br/wp-content/uploads/2020/03/20200302074536-scaled.jpg"/>
</div>

---
Este repositório contém um modelo de aprendizado de máquina para prever o tipo de uma estrela com base em suas características. O conjunto de dados usado para treinar e testar o modelo está disponível no arquivo 6 class csv.csv.

## Sumário
- Introdução
- Visão Geral do Conjunto de Dados
- Pré-processamento de Dados
- Treinamento do Modelo
- Avaliação do Modelo
- Visualização
- Uso
- Dependências
- Autor
## Introdução
Compreender as características e tipos de estrelas é crucial no campo da astronomia. Este projeto tem como objetivo prever o tipo de uma estrela com base em recursos como temperatura, luminosidade, raio, cor da estrela e classe espectral. Os modelos de previsão utilizados são Decision Tree Classifier, Logistic Regression e Gaussian Naive Bayes.

## Visão Geral do Conjunto de Dados
O conjunto de dados consiste em várias características que descrevem estrelas, incluindo temperatura, luminosidade, raio, cor da estrela, classe espectral e a variável alvo 'Star type'. O conjunto de dados é carregado a partir do arquivo 6 class csv.csv.

```python
import pandas as pd

data = pd.read_csv('/content/6 class csv.csv')
```
## Pré-processamento de Dados
O conjunto de dados passa por etapas de pré-processamento, incluindo o tratamento de valores ausentes, exploração de tipos de dados e visualização de correlações entre recursos.

```python
data.isnull().sum() # Verificando valores ausentes
data.dtypes # Verificando os tipos de dados
```
As colunas 'Star color' e 'Spectral Class' são agrupadas para lidar com desequilíbrios, e a codificação one-hot é aplicada. Por fim, os tipos de dados são ajustados, convertendo variáveis categóricas para inteiros.

```python
def agrupar(df, coluna, nova_coluna, limite):
    tab_text = df[coluna].value_counts()
    lista_aux = []
    for x in tab_text.index:
        if tab_text[x] < limite:
            lista_aux.append(x)
    for y in lista_aux:
        df.loc[df[coluna]==y, coluna] = nova_coluna
    return df

data['Star color'].value_counts()
agrupar(data, 'Star color', 'Other', 20)
data['Star color'].value_counts()

data['Spectral Class'].value_counts()

colunas = ['Star color', 'Spectral Class'] # Fazendo one hot encode da coluna Label

data['Star color'] = data['Star color'].astype(np.int32, copy=False)
data['Spectral Class'] = data['Spectral Class'].astype(np.int32, copy=False)
```
## Treinamento do Modelo
Três modelos de aprendizado de máquina são treinados nos dados pré-processados: Decision Tree Classifier, Logistic Regression e Gaussian Naive Bayes.

```python
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

y = data['Star type']
x = data.drop('Star type', axis=1)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

dtc = DecisionTreeClassifier(random_state=42)
dtc.fit(x_train, y_train)

lr = LogisticRegression(random_state=42)
lr.fit(x_train, y_train)

gnb = GaussianNB()
gnb.fit(x_train, y_train)
```
## Avaliação do Modelo
A acurácia de cada modelo é avaliada usando o conjunto de teste. As pontuações de precisão são impressas, fornecendo insights sobre a eficácia de cada modelo na previsão dos tipos de estrelas.

```python
from sklearn.metrics import accuracy_score

y_preds_dtc = dtc.predict(x_test)
y_preds_lr = lr.predict(x_test)
y_preds_gnb = gnb.predict(x_test)

print(f"A acurácia do modelo de árvore de decisão é de: {accuracy_score(y_test, y_preds_dtc) * 100}%")
print(f"A acurácia do modelo de regressão logística é de: {accuracy_score(y_test, y_preds_lr) * 100}%")
print(f"A acurácia do modelo de regressão logística é de: {accuracy_score(y_test, y_preds_gnb) * 100}%")
```
## Visualização
Um gráfico de dispersão é gerado para visualizar a comparação entre os tipos de estrelas reais e previstos.

```python
plt.figure(figsize=(8, 6))
plt.scatter(range(len(y_test)), y_test, label="Valores Reais", marker='o')
plt.scatter(range(len(y_preds_dtc)), y_preds_dtc, label="Previsões", marker='x')
plt.xlabel("Dados")
plt.ylabel("Tipo de estrela")
plt.title("Comparação entre Valores Reais e Previsões")
plt.legend()
plt.show()
```

## Dependências
O projeto requer as seguintes bibliotecas Python:

```python
# requirements.txt
pandas==1.3.3
numpy==1.21.2
matplotlib==3.4.3
seaborn==0.11.2
scikit-learn==0.24.2
joblib==1.1.0
```
Instale as dependências usando o arquivo requirements.txt fornecido.

## Autor
Este projeto foi criado por Miguel Araújo Julio. Para dúvidas ou contribuições, entre em contato com julioaraujo.guel@gmail.com.
