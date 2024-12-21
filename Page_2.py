import tkinter as tk
from tkinter import ttk
import webbrowser

# Define the Task class


class Task:
    def __init__(self, name, link, state):
        self.name = name
        self.link = link
        self.state = state


# Sample task list
tasks = [
    Task("Task 1", "https://example.com/1", "AC"),
    Task("Task 2", "https://example.com/2", "WA"),
    Task("Task 3", "https://example.com/3", "NA"),

]


# Define functions
def save():
    print("Save button clicked!")


def refresh():
    print("Refresh button clicked!")


# Initialize main window
root = tk.Tk()
root.title("Page 2")
root.geometry("480x480")


# Configure the grid to make it responsive
root.columnconfigure(0, weight=1)  # First column expands
root.columnconfigure(1, weight=1)  # Second column expands
root.rowconfigure(0, weight=1)     # Row expands


# Buttons
save_button = tk.Button(root, text="Save", command=save, width=10)
save_button.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

refresh_button = tk.Button(root, text="Refresh", command=refresh, width=10)
refresh_button.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)


# Create the table header
header_labels = ["Problem", "State"]
for col_index, header in enumerate(header_labels):
    label = tk.Label(root, text=header, font=("Arial", 12, "bold"),
                     borderwidth=1, relief="solid", padx=10, pady=5)
    label.grid(row=1, column=col_index, sticky="nsew")


# Populate the table with data
for row_index, task in enumerate(tasks, start=1):
    # Name cell
    # name_label = tk.Label(root, text=task.name, borderwidth=1,
    #                       relief="solid", padx=10, pady=5)
    # name_label.grid(row=row_index+1, column=0, sticky="nsew")

    # Link cell
    link_label = tk.Label(root, text=task.name, fg="black", cursor="hand2",
                          borderwidth=1, relief="solid", padx=10, pady=5)
    link_label.grid(row=row_index+1, column=0, sticky="nsew")
    link_label.bind("<Button-1>", lambda e,
                    url=task.link: open_link(url))  # Link click handler

    # State cell
    state_color = "green" if task.state == "AC" else "red" if task.state == "WA" else "purple"
    state_label = tk.Label(root, text=task.state, bg=state_color,
                           borderwidth=1, relief="solid", padx=10, pady=5)
    state_label.grid(row=row_index+1, column=1, sticky="nsew")

# Configure grid weights for responsiveness
for col_index in range(len(header_labels)):
    root.columnconfigure(col_index, weight=1)
for row_index in range(len(tasks) + 2):
    root.rowconfigure(row_index, weight=1)


# Function to handle link clicks
def open_link(url):
    webbrowser.open(url)


# Run the application
root.mainloop()
