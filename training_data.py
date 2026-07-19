import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


# 1. Load the dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target   # species stays numeric: 0, 1, 2

# 2. Split into X (features) and Y (target) — Y stays numeric
X = df.drop('species', axis=1)
Y = df['species']

# 3. Train/test split (random_state added for reproducible results)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

print(X_train.shape)
print(X_test.shape)

# 4. Train the model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, Y_train)

# 5. Evaluate
prediction = model.predict(X_test)
accuracy = accuracy_score(Y_test, prediction)
print(accuracy)

print(confusion_matrix(Y_test, prediction))


# 6. Predict on new data (reusable function to avoid repeating code)
def predict_species(input_data):
    input_df = pd.DataFrame([input_data], columns=X.columns)  # keeps feature names, kills the warning
    prediction1 = model.predict(input_df)
    print(type(prediction1[0]), prediction1[0])

    if prediction1[0] == 0:
        print("setosa")
    elif prediction1[0] == 1:
        print("versicolor")
    else:
        print("virginica")


predict_species((5.0, 3.6, 1.4, 0.2))   # example measurements
predict_species((6.0, 2.7, 4.2, 1.3))