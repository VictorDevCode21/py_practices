
from typing import List 



class Competence: 
    def __init__(self, category: str, date: str):
        self.category = category
        self.date = date 
        
    def __str__(self):
        return f'Competencia de la categoria {self.category} en la fecha {self.date}'
    
