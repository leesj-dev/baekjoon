w, h = float(input()), float(input())
bmi = w / (h * h)
if bmi > 25.0:
    print("Overweight")
elif bmi < 18.5:
    print("Underweight")
else:
    print("Normal weight")
