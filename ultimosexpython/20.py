def validarEmail(email, email_aux):
    validar = False

    if ("@" in email and ".com" in email_aux):
        validar = True
    else:
        validar = False
    return validar

email = input("Digite seu email: ")

email_aux = email.partition(".com")
email = email.partition("@")

validar = validarEmail(email, email_aux)

if(validar):
    print("Email válido")
else:
    print("Email inválido")