class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__=='__main__':
    luiza = Pessoa(nome='Luiza')
    rafael = Pessoa(luiza, nome='Rafael')
    print(Pessoa.cumprimentar(rafael))
    print(rafael.cumprimentar())
    print(rafael.nome)
    print(rafael.idade)
    for filho in rafael.filhos:
        print(filho.nome)
    rafael.sobrenome = 'Brito'
    del rafael.filhos
    rafael.olhos = 1
    print(rafael.__dict__)
    print(luiza.__dict__)
    print(Pessoa.olhos)
    print(rafael.olhos)
    print(luiza.olhos)
    print(id(Pessoa.olhos), id(rafael.olhos), id(luiza.olhos))
