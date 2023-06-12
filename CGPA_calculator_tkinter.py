import tkinter as tk

def calculate_cgpa():
    try:
        subjects = int(subjects_entry.get())
        grades = [int(grade) for grade in grades_entry.get().split(",")]
        
        total_grade_points = sum(grades)
        cgpa = total_grade_points / subjects
        
        result_label.config(text=f"CGPA: {cgpa:.2f}")
    except (ValueError, ZeroDivisionError):
        result_label.config(text="Invalid input!")

# Create the main window
root = tk.Tk()
root.title("CGPA Calculator")

# Create the form elements
subjects_label = tk.Label(root, text="Number of Subjects:")
subjects_label.pack()

subjects_entry = tk.Entry(root)
subjects_entry.pack()

grades_label = tk.Label(root, text="Grades (Separated by comma):")
grades_label.pack()

grades_entry = tk.Entry(root)
grades_entry.pack()

calculate_button = tk.Button(root, text="Calculate CGPA", command=calculate_cgpa)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()
