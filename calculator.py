from tkinter import *
from tkinter import messagebox

bmi = 0

def calculate_bmi(weight, height):
    return weight / (height / 100) ** 2

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Zayıf"
    elif 18.5 <= bmi < 24.9:
        return "Normal Kilolu"
    elif 25 <= bmi < 29.9:
        return "Fazla Kilolu"
    elif 30 <= bmi < 39.9:
        return "Obez"
    else:
        return "Ciddi Obez"

window = Tk()
window.title("BMI Calculator")
window.geometry("300x300")

def validate_int_input(P):
    if P.isdigit() or P == "":
        return True
    else:
        messagebox.showerror("Geçersiz Giriş", "Lütfen sadece tamsayı değeri giriniz.")
        return False

vcmd = (window.register(validate_int_input), '%P')

# KG label
name_kg_label = Label(window, text="Enter your weight (KG)", font=("calibre", 10, "bold"))
name_kg_label.pack()

# Entry KG
kg_entry = Entry(window, width=20, justify="center", validate='key', validatecommand=vcmd)
kg_entry.pack()

# CM label
cm_label = Label(window, text="Enter your height (CM)", font=("calibre", 10, "bold"))
cm_label.pack()

# Entry CM
cm_entry = Entry(window, width=20, justify="center", validate='key', validatecommand=vcmd)
cm_entry.pack()

def button_clicked():
    kg = kg_entry.get()
    cm = cm_entry.get()
    if kg.isdigit() and cm.isdigit():
        kg = int(kg)
        cm = int(cm)
        bmi = calculate_bmi(kg, cm)
        category = get_bmi_category(bmi)
        messagebox.showinfo("BMI Sonucu", f"Kitle Endeksi {bmi:.2f}. Kategorisi: {category}")
    else:
        messagebox.showerror("Geçersiz Giriş", "Lütfen sadece tamsayı değeri giriniz.")

button = Button(window, text="Calculate", command=button_clicked)
button.config(padx=10, pady=10)
button.pack()

window.mainloop()
