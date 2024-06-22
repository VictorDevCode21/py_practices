from typing import List 
from competence import Competence

class ByTeams(Competence):
    def __init__(self, competitors, disqualified): 
        self.competitors = competitors 
        self.disqualified = disqualified 
        super().__init__()
        
    def show_attr(self):
        return super().show_attr() 
    