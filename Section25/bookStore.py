from tkinter import *
import backBookStore

def view_command():
    list1.delete(0,END)
    for row in backBookStore.view():
        list1.insert(END,row)
        
def search_command():
    list1.delete(0,END)
    for row in backBookStore.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)
        
def insert_command():
    list1.delete(0,END)
    backBookStore.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)

        e1.insert(END, selected_tuple[1])
        e2.insert(END,selected_tuple[2])
        e3.insert(END,selected_tuple[3])
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

def delete_command():
    backBookStore.delete(selected_tuple[0])
     
def update_command():
    backBookStore.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


# Create an empty Tkinter window
window=Tk()
window.wm_title("Book Store")
# Create a Label widget with "Kg" as label
l1=Label(window,text="Title")
l1.grid(row=0,column=0) # The Label is placed in position 0, 0 in the window
# Create a Label widget with "Kg" as label
l2=Label(window,text="Author")
l2.grid(row=0,column=2) # The Label is placed in position 0, 0 in the window
# Create a Label widget with "Kg" as label
l3=Label(window,text="Year")
l3.grid(row=1,column=0) # The Label is placed in position 0, 0 in the window
# Create a Label widget with "Kg" as label
l4=Label(window,text="ISBN")
l4.grid(row=1,column=2) # The Label is placed in position 0, 0 in the window


title_text=StringVar()  # Create a special StringVar object
e1=Entry(window,textvariable=title_text)  # Create an Entry box for users to enter the value
e1.grid(row=0,column=1)

author_text=StringVar()  # Create a special StringVar object
e2=Entry(window,textvariable=author_text)  # Create an Entry box for users to enter the value
e2.grid(row=0,column=3)

year_text=StringVar()  # Create a special StringVar object
e3=Entry(window,textvariable=year_text)  # Create an Entry box for users to enter the value
e3.grid(row=1,column=1)

isbn_text=StringVar()  # Create a special StringVar object
e4=Entry(window,textvariable=isbn_text)  # Create an Entry box for users to enter the value
e4.grid(row=1,column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row= 2, rowspan = 6, column=0, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window, text="View all", width=12, command=view_command)
b2=Button(window, text="Search", width=12, command=search_command)
b3=Button(window, text="Add", width=12, command=insert_command)
b4=Button(window, text="Update", width=12, command=update_command)
b5=Button(window, text="Delete", width=12, command=delete_command)
b6=Button(window, text="Close", width=12, command=window.destroy)

b1.grid(row=2,column=3)
b2.grid(row=3,column=3)
b3.grid(row=4,column=3)
b4.grid(row=5,column=3)
b5.grid(row=6,column=3)
b6.grid(row=7,column=3)




# def from_kg():
#     # Get user value from input box and multiply by 1000 to get kilograms
#     gram=float(e2_value.get())*1000
 
#     # Get user value from input box and multiply by 2.20462 to get pounds
#     pound=float(e2_value.get())*2.20462
 
#     # Get user value from input box and multiply by 35.274 to get ounces
#     ounce=float(e2_value.get())*35.274
 
#     # Empty the Text boxes if they had text from the previous use and fill them again
#     t1.delete("1.0", END)  # Deletes the content of the Text box from start to END
#     t1.insert(END,gram)  # Fill in the text box with the value of gram variable
#     t2.delete("1.0", END)
#     t2.insert(END,pound)
#     t3.delete("1.0", END)
#     t3.insert(END,ounce)
 

 
# # This makes sure to keep the main window open
window.mainloop()