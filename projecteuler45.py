def beşgensel(x):
    return ((1+(1+24*x)**(1/2))/6).is_integer()
def üçgensel(x):
    return ((((1+8*x)**0.5)-1)/2).is_integer()
def altıgensel(x):
    return ((((1+8*x)**0.5)+1)/4).is_integer()
a=143
while True:
    a+=1
    b=a*(2*a-1)
    if altıgensel(b) and beşgensel(b) and üçgensel(b):
        print(b)
        print(a)
        break
