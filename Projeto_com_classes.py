class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def fazer_login(self, email, senha):
        return self.email == email and self.senha == senha


class Filme:
    def __init__(self, nome, assentos):
        self.nome = nome
        self.assentos_disponiveis = assentos

    def mostrar_assentos(self):
        print(f"Assentos disponíveis para {self.nome}: {', '.join(self.assentos_disponiveis)}")

    def escolher_assento(self, assento):
        if assento in self.assentos_disponiveis:
            self.assentos_disponiveis.remove(assento)
            return True
        return False


class Cinema:
    def __init__(self, nome, filmes):
        self.nome = nome
        self.filmes = {filme: Filme(filme, assentos) for filme, assentos in filmes["seat"].items()}

    def mostrar_filmes(self):
        print(f"Filmes disponíveis no {self.nome}:")
        for i, filme in enumerate(self.filmes.keys(), 1):
            print(f"{i}-{filme}")

    def escolher_filme(self, indice):
        if 1 <= indice <= len(self.filmes):
            filme_escolhido = list(self.filmes.keys())[indice - 1]
            return self.filmes[filme_escolhido]
        return None


class SistemaCinema:
    def __init__(self):
        self.cinemas = {
            "Centerplex": {
                "Movies": ["1-High School Musical", "2-De Volta Para O Futuro", "3-Elvis"],
                "seat": {
                    "1-High School Musical": ["A1", "A2", "A3", "A4", "A5"],
                    "2-De Volta Para O Futuro": ["B1", "B2", "B3"],
                    "3-Elvis": ["C1", "C2", "C3", "C4"]
                }
            },
            "Cinesystem": {
                "Movies": ["1-High School Musical", "2-Mamma Mia", "3-Grease"],
                "seat": {
                    "1-High School Musical": ["A1", "A2", "A3", "A4", "A5"],
                    "2-Mamma Mia": ["B1", "B2", "B3", "B4", "B5"],
                    "3-Grease": ["C1", "C2", "C3", "C4", "C5"]
                }
            },
            "Kinoplex": {
                "Movies": ["1-Elvis", "2-O Rei Do Show", "3-Mamma Mia"],
                "seat": {
                    "1-Elvis": ["A1", "A2", "A3", "A4"],
                    "2-O Rei Do Show": ["B1", "B2", "B3", "B4", "B5"],
                    "3-Mamma Mia": ["C1", "C2", "C3", "C4"]
                }
            }
        }
        self.usuarios = {}
        self.usuario_logado = None

    def criar_conta(self):
        nome = input("Digite seu nome: ")
        email = input("Digite seu E-mail: ")
        senha = input("Digite sua senha: ")

        if email in self.usuarios:
            print("Conta já existente.")
        else:
            self.usuarios[email] = Usuario(nome, email, senha)
            print(f"Usuário {nome} criado com sucesso!")
            self.menu()

    def fazer_login(self):
        email = input("Digite seu E-mail: ")
        senha = input("Digite sua senha: ")

        if email in self.usuarios and self.usuarios[email].fazer_login(email, senha):
            self.usuario_logado = self.usuarios[email]
            print(f"Bem-vindo, {self.usuario_logado.nome}!")
            self.menu()
        else:
            print("E-mail ou senha incorretos. Tente novamente.")
            self.escolha_inicial()

    def escolha_inicial(self):
        while True:
            try:
                escolha = int(input("Digite o número do que deseja fazer:\n1-Login\n2-Criar Conta\n"))
                if escolha == 1:
                    self.fazer_login()
                    break
                elif escolha == 2:
                    self.criar_conta()
                    break
                else:
                    print("Número inválido! Por favor, digite novamente.")
            except ValueError:
                print("Entrada inválida.")

    def menu(self):
        while True:
            try:
                escolha = int(input("1-Ver cinemas\n2-Avaliar filmes\n"))
                if escolha == 1:
                    self.ver_cinemas()
                    break
                elif escolha == 2:
                    self.avaliar_filmes()
                    break
                else:
                    print("Escolha indisponível. Por favor, escolha novamente.")
            except ValueError:
                print("Entrada inválida.")

    def ver_cinemas(self):
        print("Não perca a oportunidade! Use o cupom '10CONTO' para ganhar 10% de desconto!!")
        while True:
            try:
                escolha_cinema = int(input("Qual cinema gostaria de ir?\n1-Centerplex\n2-Cinesystem\n3-Kinoplex\n"))
                if escolha_cinema in [1, 2, 3]:
                    nome_cinema = list(self.cinemas.keys())[escolha_cinema - 1]
                    cinema = Cinema(nome_cinema, self.cinemas[nome_cinema])
                    cinema.mostrar_filmes()

                    while True:
                        try:
                            escolha_filme = int(input("Escolha o filme que deseja ver: "))
                            filme = cinema.escolher_filme(escolha_filme)
                            if filme:
                                self.escolher_assentos(filme)
                                break
                            else:
                                print("Opção inválida. Tente novamente.")
                        except ValueError:
                            print("Entrada inválida.")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    def escolher_assentos(self, filme):
        filme.mostrar_assentos()
        while True:
            try:
                total_ingressos = int(input("Quantos ingressos vai querer? "))
                if 1 <= total_ingressos <= len(filme.assentos_disponiveis):
                    assentos_escolhidos = []
                    for i in range(total_ingressos):
                        while True:
                            assento = input(f"Escolha o assento {i + 1}: ").strip().upper()
                            if filme.escolher_assento(assento):
                                assentos_escolhidos.append(assento)
                                break
                            else:
                                print("Assento indisponível ou inválido. Escolha outro.")
                    print(f"Assentos escolhidos: {', '.join(assentos_escolhidos)}")
                    self.realizar_pagamento(total_ingressos)
                    break
                else:
                    print(f"A quantidade de ingressos deve ser entre 1 e {len(filme.assentos_disponiveis)}.")
            except ValueError:
                print("Entrada inválida.")

    def realizar_pagamento(self, total_ingressos):
        while True:
            try:
                tem_cupom = int(input("Possui cupom?\n1-SIM\n2-NÃO\n"))
                if tem_cupom == 1:
                    cupom = input("Digite seu cupom: ")
                    if cupom == '10CONTO':
                        print("Cupom válido!")
                        valor_total = (total_ingressos * 20.00) * 0.9
                    else:
                        print("Cupom inválido! Tente novamente.")
                        tentar_novamente = int(input("Deseja tentar outro cupom?\n1-SIM\n2-NÃO\n"))
                        if tentar_novamente == 2:
                            valor_total = total_ingressos * 20.00
                        break
                elif tem_cupom == 2:
                    valor_total = total_ingressos * 20.00
                else:
                    print("Opção inválida. Digite 1 ou 2.")
                    continue

                print("Estamos quase lá!!!\nPara realizar o pagamento, faça um PIX para essa chave: 82999706005")
                print(f"Valor final: R${valor_total:.2f}")
                self.finalizar_compra(valor_total)
                break
            except ValueError:
                print("Entrada inválida.")

    def finalizar_compra(self, valor_total):
        while True:
            try:
                escolha = int(input("O pagamento foi finalizado?\n1-SIM\n2-NÃO\n"))
                if escolha == 1:
                    print("Sua compra foi realizada com sucesso!")
                    break
                elif escolha == 2:
                    print("Por favor, volte e finalize o pagamento.")
                    self.realizar_pagamento(valor_total / 20.00)
                    break
                else:
                    print("Opção inválida. Digite 1 ou 2.")
            except ValueError:
                print("Entrada inválida.")

    def avaliar_filmes(self):
        filme = input("Digite qual filme deseja avaliar: ")
        avaliacao = input(f"Digite sua avaliação sobre {filme}:\n")
        while True:
            try:
                nota = int(input("Qual sua nota de 0 a 10:\n"))
                if 0 <= nota <= 10:
                    print("Obrigado pela sua avaliação!\nAgora o que deseja fazer?\n")
                    self.menu()
                    break
                else:
                    print("Por favor, digite uma nota entre 0 e 10.")
            except ValueError:
                print("Entrada inválida.")

sistema = SistemaCinema()
sistema.escolha_inicial()
