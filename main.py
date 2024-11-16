from tkinter import *
import backend


def clear_list():
    list1.delete(0, END)


def fill_list(books):
    for book in books:
        list1.insert(END, book)


window = Tk()

window.title("<* Erfan Khodakarami Book Store *>")
window.geometry('400x300')
window.resizable(width=False, height=False)
window.configure(bg='gray')
# window.iconbitmap('index_mge_icon.ico')

# ===================  label  ==================
l1 = Label(window, text="Title:", bg="darkgray", font=("Cour New", 10, 'bold'))
l1.grid(row=0, column=0, pady=5)

l2 = Label(window, text="Author:", bg="darkgray")
l2.grid(row=0, column=3)

l3 = Label(window, text="Year:", bg="darkgray")
l3.grid(row=1, column=0)

l4 = Label(window, text="  ISBN  :", bg="darkgray")
l4.grid(row=1, column=3)
# ===================  Entry  ==================

title_text = StringVar()
e1 = Entry(window, textvariable=title_text, bg="lightgray")
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text, bg="lightgray")
e2.grid(row=0, column=4)

year_text = IntVar()
e3 = Entry(window, textvariable=year_text, bg="lightgray")
e3.grid(row=1, column=1)

isbn_text = IntVar()
e4 = Entry(window, textvariable=isbn_text, bg="lightgray")
e4.grid(row=1, column=4)

list1 = Listbox(window, width=38, height=15, bg="lightsteelblue")
list1.grid(row=2, column=0, rowspan=10, columnspan=3, pady=5)

sb1 = Scrollbar(window, bg="lightsteelblue")
sb1.grid(row=2, column=3, rowspan=10)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


# sb1.config(command=list1.yview)


def get_selected_row(even):
    global selected_book

    if len(list1.curselection()) > 0:
        index = list1.curselection()[0]
        selected_book = list1.get(index)
        # title
        e1.delete(0, END)
        e1.insert(END, selected_book[1])
        # author
        e2.delete(0, END)
        e2.insert(END, selected_book[2])
        # year
        e3.delete(0, END)
        e3.insert(END, selected_book[3])
        # isbn
        e4.delete(0, END)
        e4.insert(END, selected_book[4])


list1.bind("<<ListboxSelect>>", get_selected_row)


def view_command():
    clear_list()
    books = backend.view()
    for book in books:
        list1.insert(END, book)



b1 = Button(window, text="View All", width=12, bd=6, bg='lightgray', command=lambda: view_command())
b1.grid(row=2, column=4)


def search_command():
    clear_list()
    books = backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    fill_list(books)


b2 = Button(window, text="Search Entry", bd=6, width=12, bg='lightgray', command=search_command)
b2.grid(row=3, column=4)


def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()


b3 = Button(window, text="Add Entry", bd=6, width=12, bg='lightgray', command=add_command)
b3.grid(row=4, column=4)


def update_command():
    backend.update(selected_book[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()


b4 = Button(window, text="Update Selected", bd=6, width=12, bg='lightgray', command=update_command)
b4.grid(row=5, column=4)


def delete_command():
    backend.delete(selected_book[0])
    view_command()


b5 = Button(window, text="Delete Selected", bd=6, width=12, bg='lightgray', command=delete_command)
b5.grid(row=6, column=4)

b6 = Button(window, text="Close", bd=6, width=12, bg='lightgray', command=window.destroy)
b6.grid(row=7, column=4)

window.mainloop()
