h_cm="175"
W_kg="68.5"

h_cm=int(h_cm)
W_kg=float(W_kg)

h_m=h_cm/100
bmi=W_kg/(h_m*h_m)
print("BMI:",bmi)
