//chapter3ex1
time = input("Enter Hours: ")
rate = input("Enter enter: ")
try:
fotime = float(time)
forate = float(rate)
except:
    print("Error, please enter numeric input")
    print(fotime, forate)
if forate >40 :
reg = forate * fortime
otp = (fotime - 40.0) * (forate * 0.5)
pay = reg + otp
else:
pay = float(time) * float(rate)
print("pay:",pay)