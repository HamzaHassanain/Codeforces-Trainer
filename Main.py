from tkinter import *
from tkinter import messagebox
# open the new window start
def open_info_tap():
    messagebox.showinfo("Info", "This will lead to another page.")
# open the new window end

# abous us funcrion start
def about_us_info():
    about_us_lb.pack(pady=10)
# abous us funcrion end

# load function start
def load_tap():
    messagebox.showinfo("Load", "This will lead to another page.")
#load function end

# Main GUI start
root = Tk()
root.title("Main")
root.geometry("500x450")
root.minsize(500, 450)
root.configure(bg="#ededed")
root.option_add("*Font", ("Arial", 12))
# Main GUI end

#logo start
image = PhotoImage(file="logo.png")
Label(root, text= "",bg="#ededed", image=image).pack(pady=10)
#logo end

# new and load button start
buttons_frame = Frame(root, bg="#ededed")
buttons_frame.pack(pady=40)
#new button start
new_button = Button(buttons_frame, text="New", width=5, height=1 ,relief="solid",
                    borderwidth=1, bg="#bdbdbd", command=open_info_tap)
new_button.grid(row=0, column=1, padx=50)
# new button end

# load button start
load_button = Button(buttons_frame, text="Load", width=5, height=1, relief="solid",
                    borderwidth=1, bg="#bdbdbd", command=load_tap)
load_button.grid(row=0, column=2, padx=50)
#load button end

# new and load button end

# about us button start
about_button = Button(root, text="About Us", width=10, height=1, relief="solid",
                    borderwidth=1, bg="#bdbdbd", command=about_us_info)
about_button.pack(pady=0)
# about us button start

# footer text start
names = "Developed by : \n John Shawky Habil \n Youssef Ragab El Azab \n Hamza Mohamed Hassanain \n David Ashraf Farid \n Mohamed Nasser Abd El Azem"
about_us_lb = Label(root, text=names, bg="#ededed")
# footer text end

root.mainloop()