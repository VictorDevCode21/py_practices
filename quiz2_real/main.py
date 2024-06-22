from info import info 
from typing import List
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
            
        def show_categories():
            categories = set()
            for element in teams:
                categories.add(element.category)
            print(f'Las categorias disponibles son: : {categories}\n')
            print("Por favor seleccione una categoria: ")
            selected_category = input("Ingrese el nombre de la categoria que desea seleccionar: ")
            if selected_category in categories:
                print(f"Los equipos de la categoria: {selected_category} son: \n")
                for element in teams:
                    if selected_category == element.category:
                        print(f'{element.competitors}, {element.nationality}, {element.id}, {element.category}\n')
            if selected_category not in categories:
                print("La categoria ingresada no existe")
                
        def show_competences():
            for element in competences:
                print(f'Competencia de la categoria: {element.category}, en la fecha: {element.date} \n')

            
        try: 
            print("Bienvenido al menu \n")
            
            print("Las opciones son: \n")
            print("1: Ver Equipos por categoria \n")
            print("2: Ver Competencias \n")
            print("3: Agregar equipos \n")
            print("4: Rondas de competencia \n")
            print("5: Prueba de dopaje \n")
            print("6: Salir \n")
            option = int(input("Selecciona una opcion: "))
            
            if option == 1:
                show_categories()
                
            elif option == 2:
                show_competences()
                
            elif option == 6:
                break
            
            
        except Exception as e: 
            print(f"Ha ocurrido un error: {e}")
            
        
                
    
if __name__ == "__main__":
    Main()

