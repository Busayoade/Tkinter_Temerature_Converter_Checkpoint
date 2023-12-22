#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk

def convert_temp():
    try:
        fahrenheit = float(entry.get())
        celsius = (fahrenheit - 32) * 5.0/9.0
        result_label.config(text=f"{fahrenheit}°F = {celsius:.2f}°C")
    except ValueError:
        result_label.config(text="Please enter a valid number")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create input label and entry field for Fahrenheit temperature
input_label = tk.Label(root, text="Enter Fahrenheit temperature:")
input_label.pack()

entry = tk.Entry(root)
entry.pack()

# Create a button to trigger the conversion
convert_button = tk.Button(root, text="Convert", command=convert_temp)
convert_button.pack()

# Create label to display the converted temperature
result_label = tk.Label(root, text="", font=('Arial', 14, 'bold'))
result_label.pack()

# Run the main Tkinter loop
root.mainloop()


# In[ ]:




