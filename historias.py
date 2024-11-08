class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.cordura = 100  # Sanidade do personagem, que pode diminuir com eventos assustadores.

class Jogo:
    def __init__(self):
        self.personagem = None
        self.historico_decisoes = []  # Armazena as escolhas feitas pelo jogador

    def iniciar_jogo(self):
        print("=== Bem-vindo ao Jogo de Terror: O Convite para o Baile do Porão ===")
        nome = input("Digite o nome do seu personagem: ")
        self.personagem = Personagem(nome)
        print(f"\nOlá, {self.personagem.nome}. Você recebeu um convite misterioso para um baile secreto no porão da escola...")
        self.capitulo_um()

    def capitulo_um(self):
        print("\nCapítulo 1: O Convite")
        print("Ao chegar na escola à noite, você encontra o prédio deserto e o portão do porão entreaberto, como se alguém estivesse esperando por você.")
        escolha = input("O que você deseja fazer?\n1. Entrar no porão.\n2. Ir embora imediatamente.\nEscolha: ")

        if escolha == "1":
            print("\nVocê decide entrar no porão. O ar é frio e denso, e uma sensação de medo começa a tomar conta de você.")
            self.historico_decisoes.append("Entrou no porão")
            self.personagem.cordura -= 10
            self.capitulo_dois()
        elif escolha == "2":
            print("\nVocê decide ir embora, mas ao se virar, percebe que a porta principal está trancada. Parece que alguém quer que você entre no porão...")
            self.historico_decisoes.append("Tentou sair")
            self.capitulo_dois()
        else:
            print("Escolha inválida.")
            self.capitulo_um()

    def capitulo_dois(self):
        print("\nCapítulo 2: A Descida")
        print("Você desce os degraus rangentes e chega a um corredor escuro. A única luz vem de velas dispostas ao longo do caminho.")
        escolha = input("O que você deseja fazer?\n1. Seguir as velas.\n2. Procurar uma saída alternativa.\nEscolha: ")

        if escolha == "1":
            print("\nVocê segue o caminho das velas, que parece guiar você a uma sala decorada para o 'baile'. No entanto, algo parece terrivelmente errado.")
            self.historico_decisoes.append("Seguiu as velas")
            self.personagem.cordura -= 20
            self.capitulo_tres()
        elif escolha == "2":
            print("\nVocê procura outra saída, mas o corredor parece se transformar, levando você de volta ao mesmo ponto de onde começou.")
            self.historico_decisoes.append("Procurou outra saída")
            self.personagem.cordura -= 15
            self.capitulo_tres()
        else:
            print("Escolha inválida.")
            self.capitulo_dois()

    def capitulo_tres(self):
        print("\nCapítulo 3: O Baile")
        print("Você entra na sala e percebe figuras dançando em silêncio. Ao se aproximar, percebe que não são pessoas... são manequins vestidos em trajes de gala.")
        escolha = input("O que você deseja fazer?\n1. Tentar falar com os manequins.\n2. Tentar sair da sala discretamente.\nEscolha: ")

        if escolha == "1":
            print("\nVocê tenta falar com um dos manequins, mas ele se move e começa a te perseguir. Você corre em direção à saída!")
            self.historico_decisoes.append("Tentou falar com os manequins")
            self.personagem.cordura -= 30
            self.capitulo_final()
        elif escolha == "2":
            print("\nVocê tenta sair discretamente, mas as portas se fecham, e os manequins começam a se mover em sua direção, cercando você.")
            self.historico_decisoes.append("Tentou sair discretamente")
            self.personagem.cordura -= 40
            self.capitulo_final()
        else:
            print("Escolha inválida.")
            self.capitulo_tres()

    def capitulo_final(self):
        print("\nCapítulo Final: A Fuga")
        print("Desesperado, você tenta encontrar uma saída antes que os manequins cheguem até você.")
        escolha = input("O que você deseja fazer?\n1. Correr para o corredor e subir as escadas.\n2. Procurar uma janela para escapar.\nEscolha: ")

        if escolha == "1":
            print("\nVocê corre de volta para o corredor e sobe as escadas. Ao chegar ao topo, a porta finalmente está destrancada, e você consegue escapar!")
            self.historico_decisoes.append("Correu para o corredor")
            self.fim("escapou")
        elif escolha == "2":
            print("\nVocê tenta encontrar uma janela, mas o tempo se esgota, e os manequins cercam você. Tudo escurece...")
            self.historico_decisoes.append("Procurou uma janela")
            self.fim("foi capturado")
        else:
            print("Escolha inválida.")
            self.capitulo_final()

    def fim(self, resultado):
        if resultado == "escapou":
            print("\nParabéns! Você conseguiu escapar do baile do porão. Ao olhar para trás, vê uma sombra acenando da janela do porão...")
        else:
            print("\nInfelizmente, você não conseguiu escapar. Agora você faz parte do baile eterno do porão...")
        
        print("\n=== Fim do Jogo ===")
        print(f"Histórico de escolhas: {self.historico_decisoes}")
        print(f"Cordura final: {self.personagem.cordura}")

# Execução do jogo
jogo = Jogo()
jogo.iniciar_jogo()