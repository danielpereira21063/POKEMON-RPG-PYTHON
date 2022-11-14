from pokemon import *
from pessoa import *

def escolher_pokemon_inicial(player):
    print("Olá {}, você poderá agora escolher o Pokemon que irá te acompanhar nessa jornada!")
    pikachu = PokemonEletrico("Pikachu", level=1)
    charmander = PokemonFogo("Charmander", level=1)
    squirtle = PokemonAgua("Squirtle", level=1)

    print("Escolha um pokemon: ")
    print("1 - ", pikachu)
    print("2 - ", charmander)
    print("3 - ", squirtle)

    # while True:
    #     escolha = input("Digite o número do pokemon desejado: ")
    #     if escolha == "1":
    #         player.capturar(pikachu)
    #         break
    #     elif escolha == "2":
    #         player.capturar(charmander)
    #         break
    #     elif escolha == "3":
    #         player.capturar(squirtle)
    #         break
    #     else:
    #         print("Escolha inválida")

        
player = Player("Daniel")
player.capturar(PokemonAgua("Flarion"))

inimigo1 = Inimigo("Pedro", pokemons=[PokemonAgua("charmander")])

player.batalhar(inimigo1)