from pypokerengine.players import BasePokerPlayer

class RemotePlayer(BasePokerPlayer):

    def declare_action(self, valid_actions, hole_card, round_state):
        err_msg = self.__build_err_msg("declare_action")
        raise NotImplementedError(err_msg)

    def receive_game_start_message(self, game_info):
        print(game_info)

    def receive_round_start_message(self, round_count, hole_card, seats):
        err_msg = self.__build_err_msg("receive_round_start_message")
        raise NotImplementedError(err_msg)

    def receive_street_start_message(self, street, round_state):
        err_msg = self.__build_err_msg("receive_street_start_message")
        raise NotImplementedError(err_msg)

    def receive_game_update_message(self, new_action, round_state):
        err_msg = self.__build_err_msg("receive_game_update_message")
        raise NotImplementedError(err_msg)

    def receive_round_result_message(self, winners, hand_info, round_state):
        err_msg = self.__build_err_msg("receive_round_result_message")
        raise NotImplementedError(err_msg)


def setup_ai():
    return RemotePlayer()