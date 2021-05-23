''' Esta funcion eleve a la potencia deseada un rango de numeros que hay que definir'''

def math_powers (range, power):
    the_list = [(a ** power) for a in range(range)]   
    print(the_list)
math_powers(10,3)
# me da error int objetc is not callable. Prefiero dejar la funcion asi y resolver la duda el lunes en tutoria.