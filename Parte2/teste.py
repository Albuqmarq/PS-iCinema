
import json


class CinemaManager:
    def __init__(self, json_file):
        self.json_file = json_file
        self.cinemas = self.load_cinemas()

    def load_cinemas(self):
        """Carrega os dados dos cinemas a partir do arquivo JSON."""
        with open(self.json_file, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_cinemas(self):
        """Salva as alterações no arquivo JSON."""
        with open(self.json_file, "w", encoding="utf-8") as file:
            json.dump(self.cinemas, file, indent=4, ensure_ascii=False)

    def choose_seats(self, cinema_name, movie_index):
        cinema = self.cinemas[cinema_name]
        movie_key = cinema["Movies"][movie_index - 1]
        seats = cinema["seat"][movie_key]

        print(f"Assentos disponíveis para {movie_key}:")
        for seat, status in seats.items():
            print(f"{seat}: {status}")

        while True:
            try:
                total_tickets = int(input("Quantos ingressos vai querer? "))
                available_seats = [seat for seat, status in seats.items() if status == "disponível"]
                max_seats = len(available_seats)

                if 1 <= total_tickets <= max_seats:
                    chosen_seats = []
                    for i in range(total_tickets):
                        while True:
                            seat_choice = input(f"Escolha o assento {i+1}: ").strip().upper()
                            if seat_choice in seats and seats[seat_choice] == "disponível":
                                chosen_seats.append(seat_choice)
                                seats[seat_choice] = "reservado" 
                                break
                            else:
                                print("Assento indisponível ou inválido. Escolha outro.")
                    print(f"Assentos escolhidos: {', '.join(chosen_seats)}")
                    self.save_cinemas()  
                    self.payment(total_tickets)
                    break
                else:
                    print(f"A quantidade de ingressos deve ser entre 1 e {max_seats}. Por favor, escolha novamente.")
            except ValueError:
                print("Entrada inválida.")

    def available_cinemas(self):
        print("Não perca a oportunidade! Use o cupom '10CONTO' para ganhar 10% de desconto!!")
        while True:
            try:
                cinemas_option = int(input("Qual cinema gostaria de ir?\n[1] Centerplex\n[2] Cinesystem\n[3] Kinoplex\n"))
                if cinemas_option in [1, 2, 3]:
                    cinema_name = list(self.cinemas.keys())[cinemas_option - 1]
                    cinema = self.cinemas[cinema_name]

                    print("Filmes disponíveis:")
                    for i, movie in enumerate(cinema["Movies"], 1):
                        print(f"[{i}] {movie}")

                    while True:
                        try:
                            chosen = int(input("Escolha o filme que deseja ver: "))
                            if 1 <= chosen <= len(cinema["Movies"]):
                                print("Boa escolha!")
                                self.choose_seats(cinema_name, chosen)
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
    


    def payment(self, total_tickets):
        price_per_ticket = 20 
        total_price = total_tickets * price_per_ticket
        print(f"Total a pagar: R${total_price:.2f}")
        coupon = input("Digite o cupom de desconto (ou pressione Enter para pular): ").strip().upper()
        if coupon == "10CONTO":
            
            total_price -= total_price*0.9
            print(f"Desconto aplicado! Novo total: R${total_price:.2f}")
        print("Pagamento realizado com sucesso. Bom filme!")


