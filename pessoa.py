import random
from pokemon import *

NOMES = ["Daniel", "Guilherme", "João", "Antônio", "Vanessa",
         "Fernanda", "Maria", "Diego", "Júlia", "Daniele", "Lucas"]


POKEMONS = [
    PokemonFogo("Charmander"),
    PokemonFogo("Flarion"),
    PokemonFogo("Charmilion"),
    PokemonEletrico("Pikachu"),
    PokemonEletrico("Raiuchu"),
    PokemonAgua("Squirtle"),
    PokemonAgua("Magicarp")
]


class Pessoa:
    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

        self.dinheiro = dinheiro

    def __str__(self):
        return self.nome

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou {}".format(self, pokemon))

    def mostrar_pokemons(self):
        if self.pokemons:
            print("Pokemons de {}".format(self))
            for index, pokemon in enumerate(self.pokemons):
                print("({}) - {}".format(index, pokemon))
        else:
            print("{} não tem nenhum pokemon".format(self))

    def batalhar(self, pessoa):
        print("{} iniciou uma batalha com {}".format(self, pessoa))

        pessoa.mostrar_pokemons()

        pokemon_inimigo = pessoa.escolher_pokemon()
        pokemon = self.escolher_pokemon()

        if (pokemon and pokemon_inimigo):
            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print("{} venceu a batalha".format(self))
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break

                vitoria_inimiga = pokemon_inimigo.atacar(pokemon)
                if vitoria_inimiga:
                    print("{} venceu a batalha".format(pessoa))
                    break
            else:
                print("Essa batalha não pode ocorrer")

    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print("Você ganhou R${0:.2f}".format(quantidade))
        self.mostrar_dinheiro()

    def mostrar_dinheiro(self):
        print("Você possui R${0:.2f}".format(self.dinheiro))

    def escolher_pokemon(self):
        if (self.pokemons):
            pokemon_escolhido = random.choice(self.pokemons)
            print("{} escolheu {}".format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print("{} não tem nenhum pokemon para ser escolhido".format(self))


class Player(Pessoa):
    tipo = "player"

    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                try:
                    escolha = int(
                        input("Digite o número do pokemon desejado: "))
                    pokemon_escolhido = self.pokemons[escolha]
                    print("{} eu escolho você!".format(pokemon_escolhido))
                    return pokemon_escolhido
                except:
                    print("Escolha inválida")
        else:
            print("{} não tem nenhum pokemon para ser escolhido".format(self))


class Inimigo(Pessoa):
    tipo = "Inimigo"

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choice(POKEMONS))

        super().__init__(nome=nome, pokemons=pokemons)
