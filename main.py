from tkinter import *
from tkinter import messagebox
import backend

def button_click():
    general_num = 0
    spl_str = (str_num.get()).split()
    i = 0
    while i < len(spl_str):
        next_num = backend.search_number(spl_str[i])
        if general_num == 0 or len(str(backend.search_number(spl_str[i-1]))) > len(str(next_num)):
            general_num += next_num
        else:
            prev_num = backend.search_number(spl_str[i-1])
            print(f"{prev_num} and {next_num}")
            if len(str(prev_num)) == len(str(next_num)):
                messagebox.showerror("Error", "Ввод чисел одной разрядности")
            elif len(str(prev_num)) < len(str(next_num)):
                if len(str(prev_num)) == 2:
                    messagebox.showerror("Error", "Ввод сотен, после ввода десятков")
                elif len(str(prev_num)) == 1 and len(str(next_num)) == 3:
                    messagebox.showerror("Error", "Ввод сотен, после ввода единиц")
                elif len(str(prev_num)) == 1 and len(str(next_num)) == 2:
                    messagebox.showerror("Error", "Ввод десятков, после ввода единиц или пропущенна связка und")
            else:
                messagebox.showerror("Error", "Не коректный ввод")
            return
        i += 1
    label1.config(text=str(general_num))
    label2.config(text=backend.to_oldRus_numbers(general_num))

root = Tk()
root.title("Перовод чисел с Немецкого в СтарРус")
root.geometry("400x300")
root.config(bg="#dce0ce")

str_num = StringVar()

btn = Button(text="Перевод", background ="#dcdcdc", width="7", font="5", command=button_click)
btn.place(relx=.5, rely=.3, anchor="c")

textbox1 = Entry(textvariable=str_num, width="30", font = "5")
textbox1.place(relx=.5, rely=.1, anchor="c")

label1 = Label(text ="Араб", bg="#dce0ce", width = "10", font = "5")
label1.place(relx=.2, rely=.5, anchor="c")

label2 = Label(text ="СтарРус", bg="#dce0ce", width = "10", font = "5")
label2.place(relx=.8, rely=.5, anchor="c")

root.mainloop()