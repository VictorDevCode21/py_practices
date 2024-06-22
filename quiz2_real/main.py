from info import info 

# information = info.get("Competidores")


# for element in information:
#     print(element.get("Nombre"))

from competitor import Competitor
from team import Team
from competence import Competence

def Main():
    
    while True: 
        competitors_info = info.get("Competidores")
        teams_info = info.get("Equipos")
        competences_info = info.get("Competencias")
        competitors = []
        teams = []
        competences = []
        
        for element in competitors_info:
            competitors.append(Competitor(element.get("Nombre"), element.get("Edad"), element.get("ID"), element.get("Test"), element.get("Nacionalidad"), element.get("Categoría")))
            
            
        for element in teams_info:
            teams.append(Team(element.get("Nacionalidad"),element.get("Competidores"), element.get("ID"), element.get("Categoría")))

        for element in competences_info:
            competences.append(Competence(element.get("Categoría"), element.get("Fecha")))
            
        try: 
            print("Bienvenido al menu \n")
            
            option = int(input("Selecciona una opcion: "))
            print("1: Ver Equipos por categoria \n")
            print("2: Ver Competencias \n")
            print("3: Agregar equipos \n")
            print("4: Rondas de competencia \n")
            print("5: Prueba de dopaje \n")
            
            if option == 1:
                show_categories()
            
            
            
            
            
        except: 
            print("la cagamos")
            
        
        def show_categories():
            print("Las categorias disponibles son: ")
            categories = set()
            for element in teams:
                categories.add(element.category)
            print(categories)
            
            categoria_seleccionada = input("Ingrese el nombre de la categoria que desea seleccionar: ")
            for element in teams: 
                if element.categoria_seleccionada == teams.category:
                    print(element)
    
    
if __name__ == "__main__":
    Main()

