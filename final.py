import tkinter as tk
from tkinter import ttk
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv('mumbai.csv')

# Create a linear regression model
model = LinearRegression()
X = data[['area', 'Bedrooms', 'Bathrooms', 'Balcony', 'parking', 'Lift']]
y = data['price']
model.fit(X, y)

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

    Address = Address_var.get()

    # Find the average price of houses in the selected Address
    filtered_data = data[data['Address'] == Address]
    avg_price = filtered_data['price'].mean()

    # Make the prediction using the linear regression model
    prediction = model.predict([[area, Bedrooms, Bathrooms, Balcony, parking, Lift]])[0]

    # Display the result
    if prediction > avg_price:
        result_label.config(
            text=f'The predicted price is {round(prediction, 2)}, which is higher than the average price in {Address} ({round(avg_price , 2)}).')
    else:
        result_label.config(
            text=f'The predicted price is {round(prediction , 2)}, which is lower than the average price in {Address} ({round(avg_price , 2)}).')


# Create the Address dropdown
Address = list(set(data['Address']))
Address_var = tk.StringVar(value=Address[0])
Address_dropdown = ttk.OptionMenu(root, Address_var, *Address)
Address_dropdown.pack()

# Create the predict button
predict_button = ttk.Button(root, text='Predict', command=predict_price)
predict_button.pack()

root.mainloop()
