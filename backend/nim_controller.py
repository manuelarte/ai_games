from flask import Blueprint, request
import json
from nim.nim import *
import uuid
from expiringdict import ExpiringDict

controller_page = Blueprint('nim_page', __name__, template_folder='templates')


# ai_easy = train(1000)
ai_medium = train(5200)
# ai_difficult = train(10000)

cache = ExpiringDict(max_len=100, max_age_seconds=5*60)


@controller_page.route('/nim', methods=['POST'])
def new_game():
    # think about using decorators to store it in the map
    game = Nim()
    id = str(uuid.uuid1())
    cache[id] = game
    return NimDto(id, game.piles).toJSON()


@controller_page.route('/nim/<id>', methods=['GET'])
def get_game(id):
    return cache[id].toDto()


@controller_page.route('/nim/<id>', methods=['PUT'])
def submit_action(id):
    data = request.json
    action = (data['pile'], data['number'])
    game = cache[id]
    winner = None
    # player move
    if do_action(game, action) is not None:
        # game finished
        winner = False # in theory if you are here the AI wins

    if winner is None:
        ai_action = ai_medium.choose_action(game.piles, epsilon=False)
        if do_action(game,  ai_action) is not None:
            # game finished
            winner = True  # in theory if you are here, you win

    cache[id] = game
    return to_dto(id, game).toJSON()


class NimDto:
    def __init__(self, id, piles, winner=None):
        self.id = str(id)
        self.human_turn = True if winner is None else None
        self.piles = piles
        self.winner = winner

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


def to_dto(id, nim):
    return NimDto(id, nim.piles, human_wins(nim))


def do_action(game, action):
    """

    :param game:
    :param action:
    :return: None if the game is still on, true if human wins, and false if AI wins
    """
    pile, count = action
    game.move((pile, count))
    return human_wins(game)

def human_wins(game):
    if game.winner is not None:
        return True if game.winner == 0 else False
    else:
        return None
