from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext

#Данная функция добавляет пользователя в список
def execute():
    name = nameEntry.get()
    surname = surnameEntry.get()
    age = ageBox.get()
    resultBox.insert(END, name + " " + surname + " " + age)
    refresh()

#Данная функция обновляет все поля ввода
def refresh():
    nameEntry.delete(0,END)
    nameEntry.insert(0,"")

    surnameEntry.delete(0,END)
    surnameEntry.insert(0,"")

    ageBox.current(0)

#данная функция очищает список пользователей
def clearList():
    resultBox.delete(0, END)


#создание окна и виджетов
window = Tk()
window.title("Application for adding users")

nameLabel = Label(window, text = "NAME:",  font="Calibri 14")
nameLabel.grid(row=0, column = 0, padx=20, pady=20)

surnameLabel = Label(window, text = "SURNAME:",  font="Calibri 14")
surnameLabel.grid(row=1, column = 0, padx=20, pady=20)

ageLabel = Label(window, text = "AGE:", font="Calibri 14")
ageLabel.grid(row=2, column = 0, padx=20, pady=20)

nameEntry = Entry(window, fg = 'black', width = 17,  font="Calibri 14")
nameEntry.grid(row=0, column = 1, padx=20, pady=20)

surnameEntry = Entry(window, fg = 'black', width = 17,  font="Calibri 14")
surnameEntry.grid(row=1, column = 1, padx=20, pady=20)

ages = ["Choose age"]
for i in range(1, 100):
    ages.append(i)

ageBox = Combobox(window, values = ages, width = 15, font="Calibri 14")
ageBox['state'] = 'readonly'
ageBox.current(0)
ageBox.grid(row=2, padx=20, pady=20, column = 1)

resultBox = Listbox(window, width = 35, height = 10, font="14")
resultBox.grid(row=4, column = 0, columnspan=2, padx=20, pady=20)

button = Button(window, width = 20, text = "ADD USER", command = execute, font="Calibri 12", bg="green", fg = "white")
button.grid(row=3, column = 0, padx=20, pady=20)

clearButton = Button(window, width = 20, text = "CLEAR LIST", command = clearList, font="Calibri 12", bg="red", fg = "white")
clearButton.grid(row=3, column = 1, padx=20, pady=20)

window.mainloop()