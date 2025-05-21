def precedencia(op):
    if op == '(':
        return 0
    elif op in '+-':
        return 1
    elif op in '*/':gu
        return 2
    else:
        return -1

def conv_postfija(EI):
    PILA = []
    EPOS = ''
    
    for simb in EI:
        if simb.isalnum():   # Si es operando
            EPOS += simb
        else:
            if simb == '(':   # Si es '('
                PILA.append(simb)
            elif simb == ')': # Si es ')'
                while PILA and PILA[-1] != '(':
                    EPOS += PILA.pop()
                PILA.pop()  # Eliminar '(' de la pila
            else:  # Es operador
                while PILA and precedencia(PILA[-1]) >= precedencia(simb):
                    EPOS += PILA.pop()
                PILA.append(simb)
    
    # Vaciar la pila al final
    while PILA:
        EPOS += PILA.pop()
    
    return EPOS

# Prueba
expresion_infija = input("Ingrese la expresión infija (sin espacios): ")
expresion_postfija = conv_postfija(expresion_infija)
print("Expresión en notación postfija:", expresion_postfija)
