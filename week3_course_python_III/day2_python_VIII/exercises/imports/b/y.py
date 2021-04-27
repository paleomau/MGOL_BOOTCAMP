def f1y(variable3 = 3):
    print(variable3)
    import sys, os
    ruta = __file__
    print(ruta)
    N = 2  # carpeta imports
    for i in range(N):
        ruta = os.path.dirname(ruta)
        print(ruta)
    print("---------")
    sys.path.append(ruta)
    print(sys.path)()
    import imports.a.x as x
    x.f1x(variable1 = 1)

def f2y(variable4 = 4):
    print(variable4)
    import sys
    sys.path
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
    import x as x
    x.f2x(variable2 = 2)