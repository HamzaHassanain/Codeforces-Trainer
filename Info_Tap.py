from tkinter import *
from tkinter import messagebox, ttk
import requests

from TasksPage import create_tasks_page
# Check Function start


# Check Function end

# Generate Button Function start


def on_generate():
    #   messagebox.showinfo("Generate", "This will lead to another page.")
    # Generate Button Function end
    create_tasks_page().mainloop()


def create_info_tap():

    def check_handle():
        handle = handle_entry.get()
        url = f"https://codeforces.com/api/user.info?handles={handle}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                result = response.json()
                if "status" in result and result["status"] == "OK":
                    status_label.config(text="Handle is valid", fg="green")
                    generate_button.config(state="normal")
                else:
                    status_label.config(
                        text="The Handle is not valid", fg="red")
                    generate_button.config(state="disabled")
            else:
                status_label.config(text="The Handle is not valid", fg="red")
                generate_button.config(state="disabled")
        except Exception as e:
            status_label.config(text="Error: Cannot validate handle", fg="red")
            generate_button.config(state="disabled")

    # Main GUI start
    InfoTapRoot = Tk()
    InfoTapRoot.title("Check & Generate")
    InfoTapRoot.geometry("400x300")
    InfoTapRoot.minsize(400, 300)
    InfoTapRoot.configure(bg="#ededed")
    InfoTapRoot.option_add("*Font", ("Arial", 12))
    # Main GUI end

    # Style Spinners start
    style = ttk.Style()
    style.configure("TSpinbox", relief="solid", borderwidth=1)
    # Style Spinners end

    # Handle Input start
    Label(InfoTapRoot, text="Enter Codeforces Handle:", bg="#ededed").pack(pady=5)
    handle_entry = Entry(InfoTapRoot, font=("Arial", 12), width=30,
                         relief="solid", borderwidth=1)
    handle_entry.pack(pady=5)
    # Handle Input end

    # Status Label start
    status_label = Label(InfoTapRoot, text="", fg="red", bg="#ededed")
    status_label.pack(pady=5)
    # Status Label end

    # Check Button start
    check_button = Button(InfoTapRoot, text="Check", bg="#bdbdbd", borderwidth=1,
                          relief="solid", command=check_handle)
    check_button.pack(pady=5)
    # Check Button end

    # Spinners start
    Label(InfoTapRoot, text="Choose Rating Range and Number of Problems:",
          bg="#ededed").pack(pady=5)
    rating_frame = Frame(InfoTapRoot, bg="#ededed")
    rating_frame.pack(pady=5)

    # Rating From Spinner start
    Label(rating_frame, text="From:", bg="#ededed").grid(
        row=0, column=0, padx=5)
    rating_from_spinner = ttk.Spinbox(
        rating_frame, from_=800, to=3500, increment=100, width=5, style="TSpinbox")
    rating_from_spinner.set(1000)
    rating_from_spinner.grid(row=0, column=1, padx=5)
    # Rating From Spinner end

    # Rating To Spinner start
    Label(rating_frame, text="To:", bg="#ededed").grid(row=0, column=2, padx=5)
    rating_to_spinner = ttk.Spinbox(
        rating_frame, from_=800, to=3500, increment=100, width=5, style="TSpinbox")
    rating_to_spinner.set(1500)
    rating_to_spinner.grid(row=0, column=3, padx=5)
    # Rating To Spinner end

    # Number of Problems Spinner start
    Label(rating_frame, text="Problems:", bg="#ededed").grid(
        row=0, column=4, padx=5)
    problems_spinner = ttk.Spinbox(
        rating_frame, from_=5, to=10, increment=1, width=2, style="TSpinbox")
    problems_spinner.set(10)
    problems_spinner.grid(row=0, column=5, padx=5)
    # Number of Problems Spinner end
    # Spinners end

    # Generate Button start
    generate_button = Button(InfoTapRoot, text="Generate", command=on_generate, state="disabled",
                             bg="#bdbdbd", borderwidth=1, relief="solid")
    generate_button.pack(pady=20)
    # Generate Button end

    return InfoTapRoot
    # InfoTapRoot.mainloop()
    # create_gui function end
