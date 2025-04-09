"Escribir un programa que permita emitir la FACTURA correspondiente, a una compra de un artículo determinado"
"del que se adquieren una o varias unidades. El IVA a aplicar es de 15% y si el Sub Total (precio de venta por cantidad)"
"es mayor de 1000, se aplicará un descuento del 12%"



def factura_simple():
    articulo = input("Nombre del artículo: ")
    precio = float(input("Precio unitario: "))
    cantidad = int(input("Cantidad: "))
    
    subtotal = precio * cantidad
    descuento = subtotal * 0.12 if subtotal > 1000 else 0
    total_con_descuento = subtotal - descuento
    iva = total_con_descuento * 0.15
    total = total_con_descuento + iva
    
    print("\n=== FACTURA ===")
    print(f"Artículo: {articulo}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento: ${descuento:.2f}")
    print(f"IVA: ${iva:.2f}")
    print(f"Total a pagar: ${total:.2f}")
    
factura_simple()