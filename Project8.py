# Jeswanth Veeramusti

bmi = None

def f_bmi(inches, pounds):
  global bmi
  height = inches * 0.0254
  weight = pounds * 0.453592
  bmi = weight / height ** 2
  return bmi

inches = float(input("Height in inches:"))
pounds = float(input("Weight in pounds:"))
f_bmi(inches, pounds)

time_save = f"You're bmi is {bmi} and you're"

if bmi < 16 and bmi < 18.5:
  print(f"{time_save} underweight.")
elif bmi >= 18.5 and bmi <= 24.9:
  print(f"{time_save} normal weight.")
elif bmi > 24.9 and bmi <= 29.9:
  print(f"{time_save} overweight")
else:
  print(f"{time_save} obese")