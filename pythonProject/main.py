def encriptar(codigo):
    letraascii = 0
    mensaje = ""

    for letra in codigo:
        letraascii = ord(letra) + 5
        mensaje += chr(letraascii)
    print(mensaje)

def desencriptar(codigo):
    letraascii = 0
    mensaje = ""

    for letra in codigo:
        letraascii = ord(letra) - 5
        mensaje += chr(letraascii)
    print(mensaje)

encriptar("")
desencriptar("")


def encriptar1(codigo):
    letraascii = 0
    mensaje = ""

    for letra in codigo:
        letraascii = ord(letra) + 2
        mensaje += chr(letraascii)
    print(mensaje)

encriptar1("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")

toascii = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print(chr(toascii))




