from tablero.objects.ficha_tateti.ficha_cruz import FichaCruz
from turno_manager.turno_manager import TurnoManager
from team.teams import Team

class TeamOrientedTurnoManager(TurnoManager):
    def __init__(self, teams: list[Team]):
        super().__init__(teams)
        self.__teams = teams
        self.__team_index = self.__get_team_turn_with_ficha_cruz(teams)
        self.__player_index = {team_index: 0 for team_index in range(len(teams))}

    def get_player_turn(self):
        player_index = self.__player_index[self.__team_index]
        return self.__teams[self.__team_index][player_index]

    def get_team_turn(self):
        return self.__teams[self.__team_index]
    
    def __get_team_turn_with_ficha_cruz(self, teams):
        for team in teams:
            if isinstance(team._TatetiTeam__ficha, FichaCruz):
                return teams.index(team)
        return 0 # Si no hay ficha cruz entonces toma el primer equipo

    def next_turn(self):
        ultimo_equipo = self.__team_index == len(self.__teams) - 1 # Condition
        ultimo_jugador = self.__player_index[self.__team_index] == len(self.__teams[self.__team_index]) - 1 # Condition

        if ultimo_jugador:
            self.__player_index[self.__team_index] = 0
        else:
            self.__player_index[self.__team_index] += 1

        if ultimo_equipo:
            self.__team_index = 0
        else:
            self.__team_index += 1
