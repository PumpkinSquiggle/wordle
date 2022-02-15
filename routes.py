from flask import Flask, request, make_response, jsonify
from wordle import get_all_words, random_answer, guess

app = Flask(__name__)


@app.route('/games', methods=['POST'])
def create():
    if request.method == 'POST':
        all_words = get_all_words("list-of-five-letter-words.txt")
        answer = random_answer(all_words).strip()
        return make_response(jsonify({"game_id": answer}), 201)


@app.route('/games/<string:game_id>', methods=['PATCH'])
def update(game_id):
    player_json = request.json
    player_guess = player_json.get("guess")
    return make_response(jsonify(guess(player_guess, game_id)), 200)

# TODO
# - sanitize game_id
# - JavaScript front-end
