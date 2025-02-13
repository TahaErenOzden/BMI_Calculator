from importlib.metadata import *
from tkinter import *

window = Tk()
window.title("BMI Calculator V3")
window.config(padx=30, pady=30)

def calculate_bmi():
    weight = kg_entry.get()
    height = cm_entry.get()

    if weight == "" or height == "":
        result_label.config(text="Enter both weights and height!")
    else :
        try:
            bmi = float(weight) / (float(height) / 100 ) ** 2
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Enter a valid number")



#label for KG
kg_label = Label(text="Enter Your weight(kg)")
kg_label.pack()
#entry for KG
kg_entry = Entry(width=10)
kg_entry.pack()
#label for CM
cm_label = Label(text="Enter your height(cm)")
cm_label.pack()
#entry for CM
cm_entry = Entry(width=10)
cm_entry.pack()
#button
button = Button(text="Calculate",command=calculate_bmi)
button.pack()
#label for result
result_label = Label()
result_label.pack()

def write_result(bmi):
    result_string = f"Your BMI is {(round(bmi, 2))}. Your are "
    if bmi < 16:
        result_string += "severely thin!"
    elif 16 <= bmi <= 17:
        result_string += "Moderate Thinness"
    elif 17 <= bmi <= 18.5:
        result_string += "Mid Thinness"
    elif 18.5 <= bmi <= 25:
        result_string += "Normal Thinness"
    elif 25 <= bmi <= 30:
        result_string += "Overweight Thinness"
    elif 30 <= bmi <= 35:
        result_string += "Obese Class I"
    elif 35 <= bmi <= 40:
        result_string += "Obese Class II"
    elif bmi >= 40:
        result_string += "Obese Class III"
    return result_string




window.mainloop()