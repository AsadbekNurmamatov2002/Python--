# ru-Сравниваем с помощью операторов if, elif и else
# uz-Shart operatorlar
suz=True
if suz:
    print("Привет, я Асадбек")
else:
    print("до свидания")

# --------------------------------

# 1-m
#       { 2*sin(x), если x>0   
#  f(x)={     
#       { x-6   , если x<=0

from math import *

x=float(input("x="))
if x>0:
    f=2*sin(x)
else:
    f=x-6
print("f=", f)

# -------------------------------------
# 2-m
#       { -x, если 0>=x
#  f(x)={  x**2 , если x<0<2  
#       { 4  , если 2<=x

x=float(input("x="))
if x<=0:
    f=-x
elif 0<x<2:
    f=x**2
else:
    f=4
print("f(x)=",f)