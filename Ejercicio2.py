def factura(cantidad, vat=21):
    return cantidad + cantidad*vat/100

print(factura(1000,10))
print(factura(1000))