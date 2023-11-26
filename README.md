<div align=center>
  
# Predict Star Web App

<img src="deploy_star_app.gif"/>
</div>

---
This is a web application that uses machine learning to predict the type of a star based on its characteristics.  The machine learning model was trained using astrophysical data including the Stefan-Boltzmann Law, Wienn displacement law, absolute magnitude ratio, and parallax to calculate the temperature, luminosity, radius, absolute magnitude, color, and spectral class of a star.

- 🌌  [star prediction app](https://previsor-estelar.streamlit.app/)

## Purpose
The dataset and this application were developed with the aim of analyzing and classifying stars, identifying patterns in their data.  Star characteristics are represented in Hertzsprung-Russell Charts and HR-Diagram to provide a visual view of the distribution of stars in celestial space.

## Usage
- Filters: Use the sidebar to adjust the characteristics of the star you want to classify, including temperature, luminosity, radius, absolute magnitude, color and spectral class.

 - Forecast: Click the "Predict" button to get a prediction of the star type based on the characteristics provided.

 - Results: The application will display the result of the prediction, indicating whether the star is a Brown Dwarf, Red Dwarf, White Dwarf, Main Sequence Star, Super Giant or Hyper Giant.

 ## Additional Views
 The app includes additional images and information for each predicted star type, providing an educational experience about different stellar classes.

 ## Observation
 The dataset is constructed based on astrophysical equations, including the Stefan-Boltzmann Law, Wienn displacement law, absolute magnitude relationship, and parallax.

<div align=center>
  
# Star Type Prediction with machine learning
<img src="https://olhardigital.com.br/wp-content/uploads/2020/03/20200302074536-scaled.jpg"/>
</div>

---
This repository contains a machine learning model to predict the type of a star based on its characteristics.  The dataset used to train and test the model is available in the 6 class csv.csv file.

 ## Summary
 - Introduction
 - Dataset Overview
 - Data Preprocessing
 - Model Training
 - Model Assessment
 - Visualization
 - Usage
 - Dependencies
 - Author
 ## Introduction
 Understanding the characteristics and types of stars is crucial in the field of astronomy.  This project aims to predict the type of a star based on features such as temperature, luminosity, radius, star color and spectral class.  The prediction models used are Decision Tree Classifier, Logistic Regression and Gaussian Naive Bayes.

 ## Dataset Overview
 The dataset consists of several features that describe stars, including temperature, luminosity, radius, star color, spectral class, and the target variable 'Star type'.  The dataset is loaded from the 6 class csv.csv file.

 ```python
 import pandas as pd

 data = pd.read_csv('/content/6 class csv.csv')
 ```
 ## Data Preprocessing
 The dataset goes through pre-processing steps, including handling missing values, exploring data types, and visualizing correlations between features.

 ```python
 data.isnull().sum() # Checking for missing values
 data.dtypes # Checking data types
 ```
 The 'Star color' and 'Spectral Class' columns are grouped to deal with imbalances, and one-hot coding is applied.  Finally, data types are adjusted by converting categorical variables to integers.

 ```python
 def group(df, column, new_column, limit):
     tab_text = df[column].value_counts()
     aux_list = []
     for x in tab_text.index:
         if tab_text[x] < limit:
             list_aux.append(x)
     for y in list_aux:
         df.loc[df[column]==y, column] = new_column
     return df

 data['Star color'].value_counts()
 group(date, 'Star color', 'Other', 20)
 data['Star color'].value_counts()

 data['Spectral Class'].value_counts()

 columns = ['Star color', 'Spectral Class'] # Making one hot encode the Label column

 data['Star color'] = data['Star color'].astype(np.int32, copy=False)
 data['Spectral Class'] = data['Spectral Class'].astype(np.int32, copy=False)
 ```
 ## Model Training
 Three machine learning models are trained on the preprocessed data: Decision Tree Classifier, Logistic Regression, and Gaussian Naive Bayes.

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
 ## Model Evaluation
 The accuracy of each model is evaluated using the test set.  Accuracy scores are printed, providing insights into how effective each model is in predicting star types.

 ```python
 from sklearn.metrics import accuracy_score

 y_preds_dtc = dtc.predict(x_test)
 y_preds_lr = lr.predict(x_test)
 y_preds_gnb = gnb.predict(x_test)

 print(f"The accuracy of the decision tree model is: {accuracy_score(y_test, y_preds_dtc) * 100}%")
 print(f"The accuracy of the logistic regression model is: {accuracy_score(y_test, y_preds_lr) * 100}%")
 print(f"The accuracy of the logistic regression model is: {accuracy_score(y_test, y_preds_gnb) * 100}%")
 ```
 ## Preview
 A scatterplot is generated to visualize the comparison between actual and predicted star types.

 ```python
 plt.figure(figsize=(8, 6))
 plt.scatter(range(len(y_test)), y_test, label="Real Values", marker='o')
 plt.scatter(range(len(y_preds_dtc)), y_preds_dtc, label="Predictions", marker='x')
 plt.xlabel("Data")
 plt.ylabel("Star type")
 plt.title("Comparison between Actual Values and Forecasts")
 plt.legend()
 plt.show()
 ```

 ## Dependencies
 The project requires the following Python libraries:

 ```python
 # requirements.txt
 pandas==1.3.3
 numpy==1.21.2
 matplotlib==3.4.3
 seaborn==0.11.2
 scikit-learn==0.24.2
 joblib==1.1.0
 ```
 Install dependencies using the provided requirements.txt file.

 ## Author
 This project was created by Miguel Araújo Julio.  For questions or contributions, please contact julioaraujo.guel@gmail.com.