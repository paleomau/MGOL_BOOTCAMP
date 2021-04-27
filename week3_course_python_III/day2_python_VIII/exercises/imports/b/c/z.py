def f1z(variable5 = 5):
    print(variable5)
    import sys, os
    ruta = __file__
    print(ruta)
    N = 3  # carpeta imports
    for i in range(N):
        ruta = os.path.dirname(ruta)
        print(ruta)
    print("---------")
    sys.path.append(ruta)
    print(sys.path)
    import imports.b.c.y as y
    y.f1y(variable3 = 3)
    

def f2z(variable6 = 6):
    print(variable6)
    import sys, os
    ruta = __file__
    print(ruta)
    N = 3  # carpeta imports
    for i in range(N):
        ruta = os.path.dirname(ruta)
        print(ruta)
    print("---------")
    sys.path.append(ruta)
    print(sys.path)
    import imports.a.x as x
    x.f2x(variable2= 2)