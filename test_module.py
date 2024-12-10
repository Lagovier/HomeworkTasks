import tkinter as tk
from math import sqrt

window = tk.Tk()
window.title("Считалка качества веток, топора. камня")
window.geometry("400x400")
window.resizable(False, False)
def create_frame():
    frame = tk.Frame(window)

    def get_values_1():
        num1_1 = float(entry1_1.get())
        num1_2 = float(entry1_2.get())
        return round(sqrt(num1_1 * num1_2),1)

    def get_values_2():
        num2_1 = float(entry2_1.get())
        num2_2 = float(entry2_2.get())
        res = (num2_1 + num2_2) / 2
        return res

    def get_values_3():
        num3_1 = float(entry3_1.get())
        num3_2 = float(entry3_2.get())
        if num3_1 <= num3_2:
            return num3_1
        else:
            return (num3_1 + num3_2) / 2

    def get_quarry():
        num3_1 = float(entry3_1.get()) * 1.5
        num3_2 = float(entry3_2.get())
        if num3_1 <= num3_2:
            return num3_1
        else:
            return (num3_1 + num3_2) / 2

    def count1():
        result1.config(text = f"{get_values_1()}")

    def count2():
        result2.config(text = f"{get_values_2()}")

    def count3():
        result3.config(text = f"{get_values_3()}")
        result4.config(text = f"Максимальное качество кварри-кварца: {get_quarry()}")

    frame.columnconfigure(0, minsize = 100)
    frame.columnconfigure(1, minsize = 100)
    frame.columnconfigure(2, minsize = 100)
    frame.columnconfigure(3, minsize = 100)
    greetings = tk.Label(frame, text = "Посчитать ветку из полена и топора (дробь через точку):")
    greetings.grid(row=0, column=0, columnspan=4, pady=(20,2))
    label1_1 = tk.Label(frame, text="Полено:")
    label1_1.grid(row=1, column=0)
    label1_2 = tk.Label(frame, text="Топор:")
    label1_2.grid(row=1, column=1)
    label1_3 = tk.Label(frame, text="Ветка:")
    label1_3.grid(row=1, column=3)
    entry1_1 = tk.Entry(frame, width=10)
    entry1_1.grid(row=2, column=0)
    entry1_2 = tk.Entry(frame, width=10)
    entry1_2.grid(row=2, column=1)
    button_1 = (tk.Button(frame, text = "Подсчёт", width=10, height = 1, command = count1))
    button_1.grid(row=2, column = 2)
    result1 = tk.Label(frame, text="")
    result1.grid(row=2, column=3)

    greetings = tk.Label(frame, text = "Посчитать топор из ветки и камня:")
    greetings.grid(row=3, column=0, columnspan=4, pady=(30,2))
    label2_1 = tk.Label(frame, text="Ветка:")
    label2_1.grid(row=4, column=0)
    label2_2 = tk.Label(frame, text="Камень:")
    label2_2.grid(row=4, column=1)
    label2_3 = tk.Label(frame, text="Топор:")
    label2_3.grid(row=4, column=3)
    entry2_1 = tk.Entry(frame, width=10)
    entry2_1.grid(row=5, column=0)
    entry2_2 = tk.Entry(frame, width=10)
    entry2_2.grid(row=5, column=1)
    button_2 = (tk.Button(frame, text = "Подсчёт", width=10, height = 1, command = count2))
    button_2.grid(row=5, column = 2)
    result2 = tk.Label(frame, text="")
    result2.grid(row=5, column=3)

    greetings = tk.Label(frame, text = "Посчитать максимальный камень:")
    greetings.grid(row=6, column=0, columnspan=4, pady=(30,2))
    label3_1 = tk.Label(frame, text="Масонри:")
    label3_1.grid(row=7, column=0)
    label3_2 = tk.Label(frame, text="Инструмент:")
    label3_2.grid(row=7, column=1)
    label3_3 = tk.Label(frame, text="Макс. камень:")
    label3_3.grid(row=7, column=3)
    entry3_1 = tk.Entry(frame, width=10)
    entry3_1.grid(row=8, column=0)
    entry3_2 = tk.Entry(frame, width=10)
    entry3_2.grid(row=8, column=1)
    button_3 = (tk.Button(frame, text = "Подсчёт", width=10, height = 1, command = count3))
    button_3.grid(row=8, column = 2)
    result3 = tk.Label(frame, text="")
    result3.grid(row=8, column=3)
    result4 = tk.Label(frame, text="")
    result4.grid(row=9, column=0, columnspan = 4,pady=2)

    button_exit = tk.Button(frame, text="Выход", width=10, height = 1, command=window_exit)
    button_exit.grid(row = 10, column = 3, pady = 40)
    return frame
def window_exit():
    window.quit()
frame = create_frame()
frame.pack()

window.mainloop()
