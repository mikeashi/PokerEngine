from pypokerengine.players import BasePokerPlayer
from rpc_client import rpc_client
from pypokerengine.engine.card import Card
import json

class RemotePlayer(BasePokerPlayer):
    def __init__(self, client):
        self.client = client

    def declare_action(self, valid_actions, hole_card, round_state):
        response = json.loads(self.client.call("declare.action", {"valid_actions":valid_actions, "hole_card":self.get_hole_card(hole_card), "round_state":self.format_round_state(round_state)}).decode("utf-8"))
        return response["action"], int(response["amount"])


    def receive_game_start_message(self, game_info):
        self.client.call("game.started", game_info)

    def receive_round_start_message(self, round_count, hole_card, seats):
        self.client.call("round.started", {"round_count":round_count, "hole_card":self.get_hole_card(hole_card), "seats":seats})

    def receive_street_start_message(self, street, round_state):
        self.client.call("street.started", {"street":street, "round_state":self.format_round_state(round_state)})

    def receive_game_update_message(self, new_action, round_state):
        self.client.call("game.updated", {"new_action":new_action, "round_state":self.format_round_state(round_state)})


    def receive_round_result_message(self, winners, hand_info, round_state):
        self.client.call("round.result", {"winners":winners, "hand_info":hand_info, "round_state":self.format_round_state(round_state)})


    # Helpers functions ......
    def get_hole_card(self,hole_card):
        return [self.get_card_str(Card.from_str(hole_card[0])), self.get_card_str(Card.from_str(hole_card[1]))]

    def format_round_state(self,round_state):
        round_state['formated_community_card'] = [self.get_card_str(Card.from_str(card)) for card in round_state['community_card']]
        return round_state
            

    def get_card_str(self, card):
        suits = {"S" : "Spades", "H":"Hearts", "D":"Diamonds", "C":"Clubs"}
        ranks = {"2" : "Two", "3" : "Three", "4" : "Four", "5" : "Five","6" :  "Six","7" :  "Seven","8" :  "Eight", "9" : "Nine","T" :  "Ten","J" : "Jack", "Q" :"Queen","K" : "King","A" : "Ace"}
        rank = ranks[card.RANK_MAP[card.rank]]
        suit = suits[card.SUIT_MAP[card.suit]]
        return "{0}Of{1}".format(rank, suit)


def setup_ai():
    return RemotePlayer(rpc_client())