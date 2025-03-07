
from files import FileManager
from pagamento import CardPayment,CashPayment,PixPayment
import uuid
from datetime import datetime, timedelta


class CinemaManager:
    def __init__(self, cinemas_file, users_file,user,menu):
        self.user = user
        self.menu=menu
        self.cinemas_file = cinemas_file
        self.users_file = users_file 
        self.cinemas_manager = FileManager(self.cinemas_file)
        self.users_manager = FileManager(self.users_file)
        self.cinemas = self.cinemas_manager.load()
        self.users = self.users_manager.load()
    

    def choose_seat_schedule(self, cinema_name, movie_index):
        cinema = self.cinemas[cinema_name]
        movie_key = cinema["Movies"][movie_index - 1]
        seats = cinema["seat"][movie_key]
        schedules = cinema['schedule'][movie_key]
        print()

        #Horarios dos filmes
        print(f"Horários disponíveis para {movie_key}:")
        current_time = datetime.now().strftime("%H:%M")  
        current_time_obj = datetime.strptime(current_time, "%H:%M").time()
        valid_schedule=[]

        for i,schedule in enumerate(schedules):

            schedule_obj = datetime.strptime(schedule, "%H:%M") + timedelta(minutes=30)
            schedule_obj2=schedule_obj.time()
                       
            if schedule_obj2 > current_time_obj:
                valid_schedule.append((i+1,schedule))
        if not valid_schedule:
                print("Não há horarios disponíveis para esse filme.")
                self.menu(self.user)
                return
        
        for i,schedule in valid_schedule:          
            print(f"[{i}] {schedule}")
        while True:
            try:
                
                chosen_schedule=int(input("Escolha o horário do filme:\n=> "))
                valid_choices = [i for i, _ in valid_schedule]
                if chosen_schedule in valid_choices:
                    selected_schedule = schedules[chosen_schedule - 1]
                    break
                elif chosen_schedule==0:
                    self.menu(self.user)
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Opção inválida. Tente novamente.")  

        #Cadeiras dos filmes
        print(f"Assentos disponíveis para {movie_key}:")
        rows, cols = 3, 4
        for i in range(rows):
            for j in range(cols):
                seat_index = i * cols + j
                if seat_index < len(seats):
                    seat_key = list(seats.keys())[seat_index]
                    if seats[seat_key] == "disponível":
                        print(f"[{seat_key}]", end=" ")
                    else:
                        print("[ X ]", end=" ")
                else:
                    print("[   ]", end=" ")
            print()

        while True:
            try:
                print("X -> Indisponível.")
                total_tickets = int(input("Quantos ingressos vai querer? \n"))
                print()
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
                                print()
                    print(f"Assentos escolhidos: {', '.join(chosen_seats)}")
                    print()

                    self.payment(total_tickets, cinema_name, movie_key, chosen_seats,selected_schedule)
                    break
                elif total_tickets==0:
                    self.menu(self.user)
                    break
                else:
                    print(f"A quantidade de ingressos deve ser entre 1 e {max_seats}. Por favor, escolha novamente.")
            except ValueError:
                print("Entrada inválida.")

    def available_cinemas(self):
        print()
        print("----------------------------------------------------------------------------------")
        print("  Não perca a oportunidade! Use o cupom '10CONTO' para ganhar 10% de desconto!!!")
        print("----------------------------------------------------------------------------------")
        print()
        while True:
            try:
                print("PARA VOLTAR AO MENU PRESSIONE '0'")
                cinemas_option = int(input("Qual cinema gostaria de ir?\n[1] Centerplex\n[2] Cinesystem\n[3] Kinoplex\n"))
                if cinemas_option in [1,2,3]:
                    cinema_name = list(self.cinemas.keys())[cinemas_option - 1]
                    cinema = self.cinemas[cinema_name]
                    print()
                    print("Filmes disponíveis:")
                    for i, movie in enumerate(cinema["Movies"], 1):
                        print(f"[{i}] {movie}")

                    while True:
                        try:
                            print()
                            chosen = int(input("Escolha o filme que deseja ver: "))
                            if 1 <= chosen <= len(cinema["Movies"]):
                                print()
                                print("Boa escolha!")
                                
                                self.choose_seat_schedule(cinema_name, chosen)
                                return
                            elif chosen==0:
                                self.menu(self.user)
                                return
                            else:
                                print("Opção inválida. Tente novamente.")
                        except ValueError:
                            print("Entrada inválida.")
                elif cinemas_option==0:
                    self.menu(self.user)
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")
    
    def payment(self, total_tickets, cinema, movie, seats, schedule):
        price_per_ticket = 20 
        total_price = total_tickets * price_per_ticket
        
        print(f"Total a pagar: R${total_price:.2f}")
        print()

        while True: 
            coupon = input("Digite o cupom de desconto (ou pressione Enter para pular): ").strip().upper()
            if coupon == "10CONTO":
                total_price *= 0.9  
                print(f"Desconto aplicado! Novo total: R${total_price:.2f}")
                print()
                break 
            elif coupon == "":  
                print("Nenhum cupom aplicado. Continuando...")
                print()

                break  
            else:
                print("Cupom inválido.")
        while True:
            try:       
                payment_method=int(input("Escolha a forma de pagamento:\n[1] Cartão\n[2] Dinheiro\n[3] PIX\n"))
                if payment_method==1:
                    payment = CardPayment()
                    break
                elif payment_method==2:
                    payment = CashPayment()
                    break
                elif payment_method==3:
                    payment = PixPayment()
                    break
                elif payment_method==0:
                    self.menu(self.user)
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Opção inválida. Tente novamente.")               

        payment.process_payment(total_price)
        while True:
            try:
                
                paid = input("Você realizou o pagamento?\n[y] SIM\n[n] NÃO\n").strip().lower()
                print()
                if paid == 'n':
                    print("Por favor, realize o pagamento.")
                    print()
                elif paid == 'y':
                    ticket = str(uuid.uuid4())[:8]
                    print(f"Aqui está o código do seu ingresso: {ticket}")
                    print("Muito obrigado! Aproveite o filme!")
                    print()
                    self.cinemas_manager.save(self.cinemas)
                    self.save_user_history(cinema, movie, seats,ticket,schedule)
                    self.menu(self.user)
                    break
                elif paid=='0':
                    self.menu(self.user)
                    break

                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Opção inválida. Tente novamente")

    def save_user_history(self, cinema, movie, seats,ticket,schedule):
       
        email = self.user.get_email()
        purchase_time = datetime.now().strftime("%H:%M:%S %d-%m-%Y")
        
    
        self.users[email]["history"].append({
                "Ticket": ticket,
                "Cinema": cinema,
                "Filme": movie,
                "Cadeiras": seats,
                "Horario_filme": schedule,
                "Horario_compra": purchase_time
                })
       
        self.users_manager.save(self.users)
        self.users = self.users_manager.load()

      
            
          
       
