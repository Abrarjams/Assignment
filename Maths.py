# 1 # Area of a rectangle:
# write a python program to calculate the area of rectangle.use the formula
# area=lentgh*widt

length = float(input("Enter the length of the rectangle: "))  
width = float(input("Enter the width of rectangle: "))
area = length * width  
print(f"The area of a rectangle is {area}")

# # circumference of a circle:
# write a python program to calculate the circumference of a circle.use the formula
# circumference = 2^r
# take the radius r as input from the user  2
#circumference of a circle:

radius = float(input("Enter the radius of the circle: ")) 
pi = 3.1459
circumference = 2*pi*radius
print(f"The circumference of the circle is{circumference}")

##simple interest :
#write a python program to calculate the simple interest .use the formula .
#simple interest = principal *rate *time
#take principal ,rate and time as inputs from the user  3
#simple interest :

principal = float(input("Enter the principal amount:"))
rate = float(input("Enter the rate of interest:"))
time = float(input("Enter the time (in years): "))
simple_interest = principal *rate *time
print(f"The simple Interest is {simple_interest}")

#speed of an object
#write a python program to calculate the speed of an object, use the formula
# speed = Distance\time
#takedistance and time as inputs from the users

distance = float(input("Enter the distance traveled (in meters): "))
time = float(input("Enter the time taken(in seconds): "))
speed = distance / time
print(f"The speed of the object is {speed}m/s")

#5 BMI Calculator
# write a python program to calculate the body mass index (BMI)use the formula BMI=weight(kg)/(height*height) 
#take weight (in kg) and height in meters as in put from the users

weight = float(input("Enter weight in kg : "))
height = float(input("Enter height in meters : "))
bmi = weight/(height*height)
print(f"BMI={bmi}")

#6 force using newtons second law
#write a python program to cal culate the force of an object use the formula
# F=ma
# take mass m in kgs and a scceleration in meters per seconds *meters per second as inputs from the user

mass = float(input("Enter mass in kg : "))
acc = float(input("Enter accelertaion in m/s^2 : "))
force = mass * acc  
print(f"Force ={force}")  

#7  Compound Interest:
# Write a Python program to calculate compound interest. Use the formula:
# A = P \left(1 + \frac{r}{n}\right)^{n t}
# Where:
# A = total amount
# P = principal amount
# r = annual interest rate (decimal)
# n = number of times interest is compounded per year
# t = time in years
# Take P, r, n, and t as inputs from the user.

p = float(input("principal : "))
r = float(input("rate(decimal) : "))
n = float(input("compounds per year : "))
t = float(input("time in years : "))
A = p*(1+r/n)**(n*t) 
print(f"Total amount ={A}")

#Perimeter of a Triangle:
#Write a Python program to calculate the perimeter of a triangle. Use the formula:
#Perimeter = a + b + c
#Take a, b, and c (lengths of the three sides) as inputs from the user.

a = float(input("side a : ")) 
b = float(input("side b : "))
c = float(input("side c : "))
perimeter = a+b+c
print(f"Perimeter={p}")

#9 #9) Volume of a Sphere:
#Write a Python program to calculate the volume of a sphere. Use the formula:
#Volume = \frac{4}{3} \pi r^3
#Take r (radius) as input from the user.
#9) Volume of a Sphere:

r = float(input("Radius: "))
pi=3.1459
volume =(4/3)*pi*(r*r*r)
print(f"Volume={volume}")

#10 Kinetic Energy:
#Write a Python program to calculate the kinetic energy of an object. Use the formula:
#KE = \frac{1}{2} m v^2
#Take m (mass in kilograms) and v (velocity in meters/second) as inputs from the user.


mass = float(input("mass (kg): "))
velocity = float(input("velocity (m/s): "))
KE = 0.5 * mass * (velocity * velocity)
print(f"kinetic energy={KE}")

11) #Quadratic Equation Roots:

# Write a Python program to find the roots of a quadratic equation using the formula:
# X = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

discriminant = b**2 - 4*a*c

if discriminant >= 0:
    # real square root
    root_d = discriminant ** 0.5

    x1 = (-b + root_d) / (2*a)
    x2 = (-b - root_d) / (2*a)

    print(f"Root 1 = {x1}")
    print(f"Root 2 = {x2}")

else:
    # imaginary roots
    real_part = -b / (2*a)
    imaginary_part = ((-discriminant) ** 0.5) / (2*a)

    print(f"Root 1 = {real_part} + {imaginary_part}i")
    print(f"Root 2 = {real_part} - {imaginary_part}i")

#12) Temperature Conversion:
# Write a Python program to convert a temperature from Celsius to Fahrenheit using the formula:
# F = \frac{9}{5}C + 32


C = float(input("Enter temperature in celsius: "))
F = (9/5)*C + 32
print(f"Fahrenheit{F}")

#13) Gravitational Force:
# Write a Python program to calculate the gravitational force between two objects using:
# F = G \frac{m1 \times m2}{r^2}


G =6.674e-11
m1 = float(input("Mass 1: "))
m2 = float(input("Mass 2: "))
r = float(input("Distance: "))
F = G*m1*m2/(r**2)
print(f"Force ={F}")

#14) Volume of a Cylinder:
# Write a Python program to calculate the volume of a cylinder using:
# \text{Volume} = \pi r^2 h


r=float(input("enter radius:"))
h=float(input("enter height:"))
pi=3.142
square_r=r**2
volume=pi*square_r*h
print(f"volume={volume}")

#15) Pressure:
# Write a Python program to calculate pressure using the formula:
# P = \frac{F}{A}


F = float(input("Force: "))
A = float(input("Area: "))

P = F / A
print(f"Pressure = {P}")

# 16#16) Electric Power:
#Write a Python program to calculate electric power using:
 #𝑃=v/i
#Take voltage (V) and current (I) from the user.
#Electric Power:

V = float(input("voltage: "))
I = float(input("Current: "))
P=V/I
print(f"power ={P}")

#17) Perimeter of a Circle (Circumference):
# Write a Python program to calculate the circumference of a circle:
# P = 2\pi r

r = float(input("Radius: "))
pi=3.142  
p = 2*pi*r  
print(f"Perimeter = {p}")  

#18) Future Value in Savings:
# Write a Python program to calculate future value of investment:
# FV = PV(1 + r)^t


pv=float(input("enter present value:"))
r=float(input("enter anuual rate:" ))
t=float(input("enter years:"))
fv=pv*(1+r)**t
print(f"Future Value ={fv}")

#19) Work Done by a Force:
#Write a Python program to calculate work done using:
#W = f \cdot d \cdot \cos(\theta)


f = float(input("Enter force: "))
d = float(input("Enter distance: "))
theta = float(input("Enter angle (in degrees): "))
rad = theta * 3.14159 / 180
cos_theta = 1 - (rad*rad)/2 + (rad**4)/24   
W = f * d * cos_theta
print(f"Work done ={W}")

#20) Heat Transfer:
#Write a Python program to calculate heat transfer:
# Q = mc\Delta T


m = float(input("Mass: "))
c = float(input("Specific Heat: "))
T = float(input("Temperature Change: "))

Q = m * c * T
print(f"Heat ={Q}")

