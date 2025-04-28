def informar_numero():
    numero = int(input("Digite um número: "))

    match numero % 2:
        case 0:
            print("O número é par!")
        case _:
            print("O número é impar!")

def main():
    informar_numero()

if __name__ == '__main__':
    main()
