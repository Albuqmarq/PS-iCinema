import json 

with open("review.json", "r", encoding="utf-8") as file:
    movies_options=json.load(file)

class Review:
    def __init__(self, number):
        self.number = number

    
    def show_reviews(self,menu,user):
        movie = list(movies_options['Movies'].keys())[self.number - 1]
        reviews = movies_options["Movies"].get(movie, [])
    
        if not reviews:
            print()
            print(f"Nenhuma avaliação encontrada para o filme {movie}.")
            print()
            menu(user)
            return
        else:
            print()
            print(f"Avaliações para o filme {movie}:")
            for i, review in enumerate(reviews, 1):
                print(f"Avaliação {i}:")
                print(f"  Review: {review['review']}")
                print(f"  Nota: {review['rating']}/10")
                print()
            menu(user)
            return  

    def options(self,menu,user):
        while True:
            try:
                if self.number in [1,2,3,4,5,6]:
                    movie = list(movies_options['Movies'].keys())[self.number - 1]
                    name_movie = movie
                    print()
                    review_text = input(f"Digite sua review sobre {name_movie}:\n")
                    while True:
                        try:
                            rating = int(input("Qual sua nota de 0 a 10:\n"))
                            if 0 <= rating <= 10:
                                print("Obrigado pela sua avaliação!")
                                print()                                
                                movies_options["Movies"][name_movie].append({
                                    "review": review_text,
                                    "rating": rating
                                })
                                
                                
                                with open("review.json", "w", encoding="utf-8") as file:
                                    json.dump(movies_options, file, indent=4, ensure_ascii=False)
                              
                                menu(user)
                                break
                                
                            else:
                                print("Por favor, digite uma nota entre 0 e 10.")
                        except ValueError:
                            print("Entrada inválida.") 
                    break      
                else:  
                    print("Opção inválida. Tente novamente.")
                    print()
                    
            except ValueError:
                print("Opção inválida. Tente novamente.")
        