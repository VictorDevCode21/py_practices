from typing import List

from by_teams import ByTeams
from competitor import Competitor


class Team:
    def __init__(self, nationality: str, competitors: List[Competitor], id: int, category: str):
        self.nacionality = nationality
        self.competitors = competitors
        self.id = id
        self.category = category

    def show_attr(self):
        return super().show_attr()
