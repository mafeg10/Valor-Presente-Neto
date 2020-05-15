vpn1 = int(input("digte VPN1: "))
vpn2 = int(input("digite VPN2: "))

if vpn1 < 0 and vpn2 < 0:
    print("Ninguna opcion es rentable, ",end= "")
    if vpn1 > vpn2:
        print("pero con vpn1 hay menos perdida")
    elif vpn1 == vpn2:
        print("y tienen la misma perdida")
    else:
        print("pero con vpn2 hay menos perdida")
else:
    if vpn1 == vpn2:
        print("las dos opciones son igual de rentables")
    if vpn1 > vpn2:
        print("vpn1 es mas rentable que vpn2")
    else:
        print("vpn2 es mas rentable que vpn1")






 