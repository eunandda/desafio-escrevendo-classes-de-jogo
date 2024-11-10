class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        # Definindo o ataque baseado no tipo
        if self.tipo.lower() == 'mago':
            ataque = 'magia'
        elif self.tipo.lower() == 'guerreiro':
            ataque = 'espada'
        elif self.tipo.lower() == 'monge':
            ataque = 'artes marciais'
        elif self.tipo.lower() == 'ninja':
            ataque = 'shuriken'
        else:
            ataque = 'ataque desconhecido'

        # Exibindo a mensagem de ataque
        print(f"O {self.tipo} atacou usando {ataque}.")

# Criando instâncias da classe Heroi
heroi1 = Heroi('Gandalf', 300, 'mago')
heroi2 = Heroi('Aragorn', 87, 'guerreiro')
heroi3 = Heroi('Li Mu Bai', 30, 'monge')
heroi4 = Heroi('Naruto', 17, 'ninja')

# Chamando o método atacar para cada herói
heroi1.atacar()  # Saída: O mago atacou usando magia.
heroi2.atacar()  # Saída: O guerreiro atacou usando espada.
heroi3.atacar()  # Saída: O monge atacou usando artes marciais.
heroi4.atacar()  # Saída: O ninja atacou usando shuriken.