import json

try:
    with open("users.json", "r") as file:
        users = json.load(file)
except FileNotFoundError:
    users = {}


class Account:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def create_account(self,menu):
        
        if self.email in users:
            print("Conta já existente. Faça login.")
            return

        users[self.email] = {'name': self.name, 'password': self.password,'history':[]}
        self.save_users()
        
        print("Conta criada com sucesso!")
        print()
        menu(self)

    def login(self, menu):
       
        if self.email in users and users[self.email]['password'] == self.password:
            self.name = users[self.email]['name']
            
            print(f"Bem-vindo, {self.name}!")
            print()
            menu(self)
        else:
            print()
            print("Email ou senha incorretos.")
            print()
            return
        
    def show_history(self):
        if self.email in users:
            user_history = users[self.email]["history"]
        
            if not user_history: 
                print()
                print("Nenhum histórico de reservas encontrado.")
                print()
            else:
                print(f"Histórico de reservas para {self.name}:")
                for i, history_entry in enumerate(user_history, 1):
                    print(f"Reserva {i}:")
                    print(f"  Cinema: {history_entry['Cinema']}")
                    print(f"  Filme: {history_entry['Filme']}")
                    print(f"  Cadeiras: {', '.join(history_entry['Cadeiras'])}")
                    print()
                     
        else:
            print("Usuário não encontrado.")
            print()
            

    def change_data(self):
       
        while True:
            option = input("Escolha uma opção:\n[1] Ver dados\n[2] Alterar senha\n[3] Ver Histórico\n[4] Sair\n")
            if option == "1":
                print()
                print(f"Nome: {self.name}\nE-mail: {self.email}\nSenha: {users[self.email]['password']}")
                print()
            elif option == "2":
                print()
                new_password = input("Digite a nova senha:\n")
                users[self.email]["password"] = new_password
                self.save_users()
                print()
                print("Senha atualizada com sucesso!")
                print()

            elif option == "3":
                self.show_history()
                return
            elif option == "4":
                print()
                print("Voltando para o menu...")
                print()
                return
            else:
                print("Opção inválida.")
                print()

    
    def save_users(self):
        with open("users.json", "w",encoding="utf-8") as file:
            json.dump(users, file, indent=4,ensure_ascii=False)
