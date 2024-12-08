altura = 0
peso = 0


while True:
    altura = int(input('Informe sua Altura (em centímetros):'))
    peso = float(input('Informe o seu peso:'))
    imc = peso/((altura/100) ** 2)
    print('o seu IMC é:', imc)

    if imc < 18.5:
        print('Você está com peso baixo')
    elif 18.5 <= imc <= 24.99:
        print('Você está no peso ideal')
    elif 25 <= imc <=29.99:
        print('Você está sobrepeso')
    elif imc >= 30:
        print('Você está obeso')


