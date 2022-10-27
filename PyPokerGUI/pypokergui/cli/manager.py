import yaml
from pypokerengine.api.game import setup_config, start_poker
import pypokergui.server.game_manager as GM

class manager:
    def __init__(self, config_path, rounds, verbose) -> None:
        # load config
        with open(config_path, "rb") as f:
            config_file = yaml.load(f)
        self.players = self.initPlayers(config_file)
        self.result = self.initResult()
        for i in range(rounds):
            self.config = setup_config(max_round=config_file["max_round"], initial_stack=config_file["initial_stack"], small_blind_amount=config_file["small_blind"], ante=config_file["ante"])
            for player in config_file["ai_players"]:
                self.config.register_player(name=player["name"], algorithm=GM._build_ai_player(player["path"]))
            print("Game %d started" % (i+1))
            self.parseResults(start_poker(self.config, verbose=verbose))
            print("Game %d ended" % (i+1))
        print("results : ", self.result)
            
    
    def initPlayers(self, config_file):
        players = []
        for player in config_file["ai_players"]:
            players.append(player["name"])
        return players

    def initResult(self):
        result = {}
        for player in self.players:
            result[player] = {"win": 0, "lose": 0, "draw": 0}
        return result

    def parseResults(self, game_result):
        winners = []
        max = 0
        for player in game_result["players"]:
            if player["stack"] > max:
                winners = []
                winners.append(player["name"])
                max = player["stack"]
        
        for player in self.players:
            if len(winners) > 1:
                if player in winners:
                    self.result[player]["draw"] += 1
                else:
                    self.result[player]["lose"] += 1
            else:
                if player in winners:
                    self.result[player]["win"] += 1
                else:
                    self.result[player]["lose"] += 1