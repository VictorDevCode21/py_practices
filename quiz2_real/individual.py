from typing import List 
from competence import Competence
from competitor import Competitor

class Individual(Competence):
    def __init__(self, competitors: List[Competitor], disquialified: List[Competitor]):
        self.competitors = competitors 
        self.disqualified = disquialified 
        
    def show_attr(self):
        return super().show_attr()
        