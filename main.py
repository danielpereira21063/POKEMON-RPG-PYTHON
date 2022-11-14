from pokemon import *
from pessoa import *


def escolher_pokemon_inicial(player):
    print("Olá {}, você poderá agora escolher o Pokemon que irá te acompanhar nessa jornada!")
    pikachu = PokemonEletrico("Pikachu", level=1)
    charmander = PokemonFogo("Charmander", level=1)
    squirtle = PokemonAgua("Squirtle", level=1)

    print("Escolha um pokemon: ")
    print("1 - {}".format(pikachu))
    print("2 - {}".format(charmander))
    print("3 - {}".format(squirtle))

    while True:
        escolha = input("Digite o número do pokemon desejado: ")
        if escolha == "1":
            player.capturar(pikachu)
            break
        elif escolha == "2":
            player.capturar(charmander)
            break
        elif escolha == "3":
            player.capturar(squirtle)
            break
        else:
            print("Escolha inválida")


if __name__ == "__main__":
    print("----------------------------------------")
    print("Bem-vindo ao game Pokemon RPG de terminal")
    nome = input("Olá, qual é o seu nome? ")
    player = Player(nome)
    print("Olá {}, esse é um número habitado por pokemons, a partir de agora sua missão é se tornar um mestre dos pokemons!".format(player))
    print("Capture o máximo de pokemons que conseguir e lute com seus inimigos.")
    player.mostrar_dinheiro()

    if (player.pokemons):
        print("Já ví que você tem alguns pokemons")
        player.mostrar_pokemons()
    else:
        print("Você não tem nenhum pokemon, portanto precisa escolher um")
        escolher_pokemon_inicial(player)

    print("Pronto, agora que você já possui um pokemon, enfrente seu inimigo Gary")
    gary = Inimigo(nome="Gary", pokemons=[PokemonAgua("Squirtle", 1)])

    player.batalhar(gary)

    while True:
        print("----------------------------------------")
        print("O que deseja fazer? ")
        print("0 - Sair do jogo")
        print("1 - Explorar pelo mundo")
        print("2 - Lutar com um inimigo")

        escolha = input("Sua escolha: ")
        if escolha == "0":
            print("Fechando o jogo...")
            break
        elif escolha == "1":
            player.explorar()
        elif escolha == "2":
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
        else:
            print("Escolha inválida")
