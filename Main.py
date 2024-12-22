from tkinter import *
from tkinter import messagebox
# open the new window start
from tkinter import filedialog


from connection import write_cft_to_sql


from Info_Tap import create_info_tap
from TasksPage import create_tasks_page

root = Tk()
# InfoTapRoot.deiconify()
# InfoTapRoot.withdraw()
# # close the info tap window

# InfoTapRoot.withdraw()
# InfoTapRoot.destroy()
# open the new window start


def open_info_tap():
    root.destroy()
    create_info_tap().mainloop()

# open the new window end

# abous us funcrion start


def about_us_info():
    about_us_lb.pack(pady=10)
# abous us funcrion end

# load function start


def load_tap():
    try:
        filename = filedialog.askopenfilename(
            filetypes=[("Codeforces Trainer Files", "*.cft")])

        if filename:
            # copy the content to db.cft
            with open(filename, "r") as file:
                with open("db.cft", "w") as db:
                    db.write(file.read())
        write_cft_to_sql()  # add the content of the chosen file to the sqllite3
        root.destroy()
        create_tasks_page().mainloop()
    except Exception as e:
        print(e)
        messagebox.showinfo("Error", "Cannot load file")
# load function end


# Main GUI start
root.title("Codeforces Trainer")
root.geometry("500x450")
root.minsize(500, 450)
root.configure(bg="#ededed")
root.option_add("*Font", ("Arial", 12))
# Main GUI end

# logo start

image = PhotoImage(file="logo.png")
Label(root, text="", bg="#ededed", image=image).pack(pady=10)

# logo end

# new and load button start
buttons_frame = Frame(root, bg="#ededed")
buttons_frame.pack(pady=40)
# new button start
new_button = Button(buttons_frame, text="New", width=5, height=1, relief="solid",
                    borderwidth=1, bg="#bdbdbd", command=open_info_tap, padx=20, pady=10)
new_button.grid(row=0, column=1, padx=50)
# new button end

# load button start
load_button = Button(buttons_frame, text="Load", width=5, height=1, relief="solid",
                     borderwidth=1, bg="#bdbdbd", command=load_tap, padx=20, pady=10)
load_button.grid(row=0, column=2, padx=50)
# load button end

# new and load button end

# about us button start
about_button = Button(root, text="About Us", width=10, height=1, relief="solid",
                      borderwidth=1, bg="#bdbdbd", command=about_us_info, padx=20, pady=10)
about_button.pack(pady=0)
# about us button start

# footer text start
names = "Developed by : \n John Shawky Habil \n Youssef Ragab El Azab \n Hamza Mohamed Hassanain \n David Ashraf Farid \n Mohamed Nasser Abd El Azem"
about_us_lb = Label(root, text=names, bg="#ededed")
# footer text end

root.mainloop()


# when the root is closed the info tap window is closed too
