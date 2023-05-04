import tkinter as tk
from tkinter import ttk
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

# Load the dataset
data = pd.read_csv('mumbai.csv')

# Create a linear regression model
X = data[['Address', 'area', 'Bedrooms', 'Bathrooms', 'Balcony', 'parking', 'Lift']]
y = data['price']

# Encode the categorical features
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X_encoded = ct.fit_transform(X)
Address_encoded = X_encoded[:, :len(ct.named_transformers_['encoder'].categories_[0])]
X_encoded = X_encoded[:, len(ct.named_transformers_['encoder'].categories_[0]):]

# Scale the numerical features
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_encoded = scaler.fit_transform(X_encoded)

# Merge the encoded Address feature with the scaled numerical features
X_final = pd.concat([pd.DataFrame(Address_encoded), pd.DataFrame(X_encoded)], axis=1)

# Set the feature importance weights
feature_importances = {'Address': 5, 'area': 2, 'Bedrooms': 1, 'Bathrooms': 0.5, 'Balcony': 0.5, 'parking': 0.5, 'Lift': 0.5}

# Create the linear regression model
model = LinearRegression()
model.coef_ = [feature_importances[feature] for feature in X.columns]

# Create the GUI
root = tk.Tk()
root.geometry('300x250')
root.title('House Price Predictor')

# Create the labels and input fields
area_label = ttk.Label(root, text='Square Feet:')
area_label.pack()
area_entry = ttk.Entry(root)
area_entry.pack()

Bedrooms_label = ttk.Label(root, text='Bedrooms:')
Bedrooms_label.pack()
Bedrooms_entry = ttk.Entry(root)
Bedrooms_entry.pack()

Bathrooms_label = ttk.Label(root, text='Bathrooms:')
Bathrooms_label.pack()
Bathrooms_entry = ttk.Entry(root)
Bathrooms_entry.pack()

Balcony_label = ttk.Label(root, text='Balcony:')
Balcony_label.pack()
Balcony_entry = ttk.Entry(root)
Balcony_entry.pack()

parking_label = ttk.Label(root, text='Parking:')
parking_label.pack()
parking_entry = ttk.Entry(root)
parking_entry.pack()

Lift_label = ttk.Label(root, text='Lift:')
Lift_label.pack()
Lift_entry = ttk.Entry(root)
Lift_entry.pack()

result_label = ttk.Label(root, text='')
result_label.pack()


# Define the predict function
def predict_price():
    area = float(area_entry.get())
    Bedrooms = int(Bedrooms_entry.get())
    Bathrooms = int(Bathrooms_entry.get())
    Balcony = int(Balcony_entry.get())
    parking = int(parking_entry.get())
    Lift = int(Lift_entry.get())

    address_index = list(ct.named_transformers_['encoder'].transformers_[0][1].categories_[0]).index(Address_var.get())
    Address_encoded = [0] * len(ct.named_transformers_['encoder'].categories_[0])
    Address_encoded[address_index] = 1

    X_test = [Address_encoded + [area, Bedrooms, Bathrooms, Balcony, parking, Lift]]
    X_test = scaler.transform(X_test)

    # Make the prediction
    prediction = model.predict(X_test)[0]

    # Update the result label
    result_label.configure(text='Predicted Price: ₹ {:.2f}'.format(prediction))
    predict_button = ttk.Button(root, text='Predict', command=predict_price)
    predict_button.pack()
    Address_label = ttk.Label(root, text='Address:')
    Address_label.pack()
    Address_var = tk.StringVar()
    Address_dropdown = ttk.Combobox(root, textvariable=Address_var, values=data['Address'].unique())
    Address_dropdown.pack()

    root.mainloop()