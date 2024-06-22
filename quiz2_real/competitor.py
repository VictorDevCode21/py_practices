from typing import List 


class Competitor: 
    def __init__(self, name: str, age: int, id: int, color_test: str, nationality: str, category: str):
        self.name = name 
        self.age = age
        self.id = id 
        self.color_test = color_test 
        self.nationality = nationality 
        self.category = category 
        
    def show_attr(self):
        return f'Los competidores son {self.name}, '
            
    
