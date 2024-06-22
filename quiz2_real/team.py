from typing import List

from by_teams import ByTeams
from competitor import Competitor


class Team:
    def __init__(self, nationality: str, competitors: List[Competitor], id: int, category: str):
        self.nationality = nationality
        self.competitors = competitors
        self.id = id
        self.category = category

    def __str__(self):
        return f'Equipo: {self.id} de {self.nationality} en la categoria {self.category} con los competidores {self.competitors}'
