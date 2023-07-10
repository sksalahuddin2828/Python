import math
 
def calculate_bmi(weight, height):
    """
    Calculates the Body Mass Index (BMI) given weight in kilograms (kg) and height in meters (m).
    """
    return weight / (height ** 2)

def calculate_blood_pressure(age, systolic, diastolic):
    """
    Calculates the blood pressure category based on age, systolic pressure, and diastolic pressure.
    """
    if age < 18:
        return "Not applicable for individuals under 18 years of age."
    elif systolic < 90 or diastolic < 60:
        return "Hypotension (low blood pressure)"
    elif systolic < 120 and diastolic < 80:
        return "Normal blood pressure"
    elif systolic < 130 and diastolic < 80:
        return "Elevated blood pressure"
    elif systolic < 140 or diastolic < 90:
        return "Hypertension stage 1"
    elif systolic < 180 and diastolic < 120:
        return "Hypertension stage 2"
    else:
        return "Hypertensive crisis (consult a doctor immediately)"

def calculate_ideal_body_weight(height, gender):
    """
    Calculates the ideal body weight based on height and gender.
    """
    if gender.lower() == "male":
        return (height - 100) - ((height - 150) / 4)
    elif gender.lower() == "female":
        return (height - 100) - ((height - 150) / 2.5)
    else:
        return "Gender should be either 'male' or 'female'."

# Additional functions for other medical calculations can be added here.

# Example usage:
weight = 70  # kg
height = 1.75  # meters
bmi = calculate_bmi(weight, height)
print(f"BMI: {bmi:.2f}")

age = 25
systolic_pressure = 120
diastolic_pressure = 80
blood_pressure_category = calculate_blood_pressure(age, systolic_pressure, diastolic_pressure)
print(f"Blood Pressure Category: {blood_pressure_category}")

height = 170  # cm
gender = "male"
ideal_weight = calculate_ideal_body_weight(height, gender)
print(f"Ideal Body Weight: {ideal_weight:.2f} kg")

