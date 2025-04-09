def calcular_compra():
    precio_por_docena = float(input("Ingrese el precio por docena del producto: "))
    cantidad_docenas = int(input("Ingrese la cantidad de docenas compradas: "))
    
    monto_compra = precio_por_docena * cantidad_docenas
    
    if cantidad_docenas > 3:
        descuento = monto_compra * 0.15  
        unidades_obsequio = (cantidad_docenas - 3)  
    else:
        descuento = monto_compra * 0.10  
        unidades_obsequio = 0
    
    monto_a_pagar = monto_compra - descuento
    
    print("\n=== DETALLE DE COMPRA ===")
    print(f"Monto de compra: ${monto_compra:.2f}")
    print(f"Descuento aplicado: ${descuento:.2f}")
    print(f"Monto a pagar: ${monto_a_pagar:.2f}")
    print(f"Unidades de obsequio: {unidades_obsequio}")
            
calcular_compra()
