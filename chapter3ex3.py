score = input("Enter Score: ")

try:
s = float(score)
except:
print("Enter:Please enter a number from 0.0 to 1.0")
quit()

if 
s > 1.0:
print("Error:Out of range")

elif s == 1.0:
print('A')
elif s >= 0.9:
print('A')
elif s >= 0.8:
print('B')
elif s >= 0.7:
print('C')
elif s >= 0.6:
print('D')
elif s >= 0.0:
print('F')
elif s < 0.0:
print("Error:Out of range")

