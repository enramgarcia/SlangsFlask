import redis
from flask import Flask, request

HOST = "localhost"
PORT = 6379

app = Flask(__name__)


def init_con():
    return redis.Redis(
        host=HOST,
        port=PORT,
        db=0,
        charset="utf-8",
        decode_responses=True)


def seed():
    words = [
        {'word': 'Xopa', 'description': 'Forma coloquial de decir Hola.'},
        {'word': 'Chantin', 'description': 'Casa'}
    ]

    redis_con = init_con()

    for definition in words:
        result_set = redis_con.get(definition['word'])
        if result_set is not None:
            continue

        redis_con.set(definition['word'], definition['description'])


@app.route('/palabras', methods=['POST'])
def create():
    word = request.form['word']
    description = request.form['description']

    redis_con = init_con()
    result_set = redis_con.get(word)

    if result_set is not None:
        return {'error': 'El record ya existe.'}, 500

    redis_con.set(word, description)

    return {'word': word, 'description': description}, 201


@app.route('/palabras/<word>', methods=['GET'])
def get(word):
    redis_con = init_con()
    result_set = redis_con.get(word)

    if result_set is None:
        return {'error': 'El record no existe.'}, 404

    return {'word': word, 'description': redis_con.get(result_set)}


@app.route('/palabras/<word>', methods=['PUT'])
def put(word):
    description = request.form['description']

    redis_con = init_con()
    result_set = redis_con.get(word)

    if result_set is None:
        return {'error': 'El record no existe.'}, 404

    redis_con.set(word, description)

    return {'word': word, 'description': description}, 202


@app.route('/palabras/<word>', methods=['DELETE'])
def delete(word):

    redis_con = init_con()
    result_set = redis_con.get(word)

    if result_set is None:
        return {'error': 'El record no existe.'}, 404

    redis_con.delete(word)

    return {'word': word}, 202


@app.route('/')
def index():
    slangs = []
    redis_con = init_con()

    for r_key in redis_con.keys():
        slangs.append({'word': r_key, 'description': redis_con.get(r_key)})

    return slangs


if __name__ == '__main__':
    app.run()

    seed()
