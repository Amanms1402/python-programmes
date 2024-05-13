import tkinter as tk

# Function to retrieve the value from the Entry widget
def get_entry_value():
    value = entry.get()  # Retrieve the value from the Entry widget
    result_label.config(text="Entry value: " + value)  # Display the value in a label

# Create a Tkinter window
window = tk.Tk()
window.title("Entry Field Example")

# Create an Entry widget
entry = tk.Entry(window)
entry.pack()

# Create a button to trigger retrieval of the Entry value
retrieve_button = tk.Button(window, text="Get Entry Value", command=get_entry_value)
retrieve_button.pack()

# Create a label to display the result
result_label = tk.Label(window, text="")
result_label.pack()

# Run the Tkinter event loop
window.mainloop()
