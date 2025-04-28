def informar_idade():
    idade = int(input("Digite sua idade: "))

    match idade:
        case idade if idade >= 0 and idade <= 12:
            print("Você é Criança!")
        case idade if idade > 12 and idade <=18:
            print("Você é Adolescente!")
        case idade if idade > 18:
            print("Você é Adulto!")
        case _:
            print("Opção inválida!")

def main():
    informar_idade()

if __name__ == '__main__':
    main()
