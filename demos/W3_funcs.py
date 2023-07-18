#Definition of a function - specifying what the procedure is, what does and how, so that it can be later called/used (maybe multiple times)
#Parameter - data given into/injected into your function
def t_area(b=1, h=1):
    height = float(input("Enter the height: "))
    base = float(input("Enter the base: "))
    area = 0.5*height*base
    print(f"Area is {area}")

#Call to the function - make your program execute the function
t_area(10, 20)
t_area(5, 4)
height = float(input("Enter Height: "))
base = float(input("Enter Base: "))
t_area(height, base)


