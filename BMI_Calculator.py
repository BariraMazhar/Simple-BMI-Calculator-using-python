def Calculate_BMI(height, weight):
    BMI = round((weight / (height ** 2)), 2)
    if (BMI < 18.5):
        print(f"BMI = {BMI}, Underweight")
    elif(BMI > 18.5 and BMI < 24.9):
        print(f"BMI = {BMI}, Normal weight")
    elif(BMI > 25 and BMI < 29.9):
        print(f"BMI = {BMI}, Overweight")
    elif(BMI >= 30):
        print(f"BMI = {BMI}, Obese")
    
    


height = float(input("Enter your height (in meters): "))
weight = float(input("Enter your weight(in Kg): "))
Calculate_BMI(height, weight)
