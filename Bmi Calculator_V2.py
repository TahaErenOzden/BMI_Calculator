from tkinter import *

#window
window = Tk()
window.title("BMI Calculator")
window.config(padx=30, pady=30)

def calculate_bmi():
    kg = weight_input_entry.get()
    cm = height_input_entry.get()

    m_converter = float(cm)
    bmi = float(kg) / (float(m_converter) / 100) ** 2

    if kg == "" or cm == "":
        result_label.config(text="Please enter both your weight and height!")
    elif bmi < 16:
        print(f"severely thin {bmi}")
        result_label.config(text=f"severely thin")
    elif 16 <= bmi <= 17:
        print(f"Moderate Thinness{bmi}")
        result_label.config(text=f"Moderate Thinness ")
    elif 17 <= bmi <= 18.5:
        print(f"Mid Thinness{bmi}")
        result_label.config(text=f"Mid Thinness ")
    elif 18.5 <= bmi <= 25:
        print(f"Normal{bmi}")
        result_label.config(text=f"Normal ")
    elif 25 <= bmi <= 30:
        print(f"Overweight{bmi}")
        result_label.config(text=f"Overweight")
    elif 30 <= bmi <= 35:
        print(f"Obese Class I {bmi}")
        result_label.config(text=f"Obese Class I ")
    elif 35 <= bmi <= 40:
        print(f"Obese Class II {bmi}")
        result_label.config(text=f"Obese Class II ")
    elif bmi >= 40:
        print(f"Obese Class III {bmi}")
        result_label.config(text=f"Obese Class III ")


#ui - kullanıcı arayüzü
weight_input_label = Label(text="Enter Your Weight (kg)")
weight_input_label.pack()

weight_input_entry = Entry(width=10)
weight_input_entry.pack()
#Height Label
height_input_label =  Label(text="Enter Your Height (cm)")
height_input_label.pack()
#Height Entry
height_input_entry = Entry(width=10)
height_input_entry.pack()
#Button
calculate_button = Button(text="Calculate",command=calculate_bmi)
calculate_button.pack()
#Result Label
result_label = Label()
result_label.pack()





window.mainloop()
