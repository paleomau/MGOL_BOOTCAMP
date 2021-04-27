def f1x(variable1 = 1):
    print(variable1)
    import sys, os
    ruta = __file__
    print(ruta)
    N = 2  # carpeta imports
    for i in range(N):
        ruta = os.path.dirname(ruta)
        print(ruta)
    print("---------")
    sys.path.append(ruta)
    print(sys.path)
    import imports.b.c.y as y
    y.f1y(variable3 = 3)

def f2x(variable2 = 2):
    print(variable2)
    import sys, os
    ruta = __file__
    print(ruta)
    N = 2  # carpeta imports
    for i in range(N):
        ruta = os.path.dirname(ruta)
        print(ruta)
    print("---------")
    sys.path.append(ruta)
    print(sys.path)
    import imports.b.c.z as z
    z.f2z(variable6 = 6)