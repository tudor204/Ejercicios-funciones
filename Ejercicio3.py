def circulo_area(radio):
    pi = 3.1415
    return pi*radio**2

def volume_cilindro(radio, alto):
    return circulo_area(radio)*alto
print(volume_cilindro(3,5))