import tkinter as tk
import webbrowser
from Task import Task
# Define the Task class
from tkinter import filedialog
from loader import load_tasks, loaded, solved, not_solved, get_status, read_handle, write_tasks, write_handle
from tkinter import messagebox


def create_tasks_page():

    # Define functions
    tasks = load_tasks()

    def save():
        # open file viwer to save the file db.cft to another cft file
        # creatre a file dialog to save the file
        filename = filedialog.asksaveasfilename(
            filetypes=[("Codeforces Trainer Files", "*.cft")])
        try:

            if filename:

                if not filename.endswith(".cft"):
                    filename += ".cft"
                with open("db.cft", "r") as file:
                    with open(filename, "w") as db:
                        db.write(file.read())
            messagebox.showinfo("File Saved", "File saved successfully")

        except Exception as e:
            print(e)
            messagebox.showinfo("Error", "Cannot save file")

    def refresh():
        global loaded, solved, not_solved

        try:

            tasks = load_tasks()
            handle = read_handle()
            # print("refreshed", tasks)

            didRef = True
            for task in tasks:
                task.state = get_status(
                    task.contestId, task.index, handle, didRef)
                didRef = False
            print("refreshed")
            for task in tasks:
                print(task.name, task.link, task.state)
            write_tasks(tasks)
            write_handle(handle)

            # clear old data from the table

            Page2Root.destroy()

            create_tasks_page().mainloop()
        except Exception as e:
            print(e)
            messagebox.showinfo("Error", "Cannot refresh")
    # Initialize main window
    Page2Root = tk.Tk()
    Page2Root.title("Codeforces Trainer | Tasks")
    Page2Root.geometry("480x480")
    Page2Root.configure(bg="#ededed")
    Page2Root.option_add("*Font", ("Arial", 12))
    Page2Root.minsize(200, 200)
    # Configure the grid to make it responsive
    Page2Root.columnconfigure(0, weight=1)  # First column expands
    Page2Root.columnconfigure(1, weight=1)  # Second column expands
    Page2Root.rowconfigure(0, weight=1)     # Row expands

    # Buttons
    save_button = tk.Button(Page2Root, text="Save", command=save,
                            width=10, relief="solid", bd=1, bg="#bdbdbd")
    save_button.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    refresh_button = tk.Button(
        Page2Root, text="Refresh", command=refresh, width=10, relief="solid", bd=1, bg="#bdbdbd")
    refresh_button.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    # Create the table header
    header_labels = ["Problem", "State"]
    for col_index, header in enumerate(header_labels):
        label = tk.Label(Page2Root, text=header, font=("Arial", 12, "bold"),
                         borderwidth=1, relief="solid", padx=10, pady=5)
        label.grid(row=1, column=col_index, sticky="nsew")

    # Populate the table with data
    for row_index, task in enumerate(tasks, start=1):
        # Name cell
        # name_label = tk.Label(Page2Root, text=task.name, borderwidth=1,
        #                       relief="solid", padx=10, pady=5)
        # name_label.grid(row=row_index+1, column=0, sticky="nsew")

        # Link cell
        link_label = tk.Label(Page2Root, text=task.name, fg="black", cursor="hand2",
                              borderwidth=1, relief="solid", padx=10, pady=5)
        link_label.grid(row=row_index+1, column=0, sticky="nsew")
        link_label.bind("<Button-1>", lambda e,
                        url=task.link: open_link(url))  # Link click handler

        # State cell
        state_color = "#31bf21" if task.state == "AC" else "#d42424" if task.state == "WA" else "#888a89"
        state_label = tk.Label(Page2Root, text=task.state, bg=state_color,
                               borderwidth=1, relief="solid", padx=10, pady=5)
        state_label.grid(row=row_index+1, column=1, sticky="nsew")

    # Configure grid weights for responsiveness
    for col_index in range(len(header_labels)):
        Page2Root.columnconfigure(col_index, weight=1)
    for row_index in range(len(tasks) + 2):
        Page2Root.rowconfigure(row_index, weight=1)

    # Function to handle link clicks

    def open_link(url):
        webbrowser.open(url)

    # Run the application
    return Page2Root
