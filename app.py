from flask import Flask, request, jsonify
from flask_redis import FlaskRedis

import random
import string

app = Flask(__name__)
redis_client = FlaskRedis(app)


@app.route('/url/add', methods=["POST"])
def add_url():
    if request.content_type != 'application/json':
        return jsonify('Error: Data must be sent as JSON.')

    url = request.json.get('url')
    key = "".join([random.SystemRandom().choice(
        string.ascii_uppercase + string.ascii_lowercase) for _ in range(20)])

    redis_client.set(key, url)
    return jsonify(key)


if __name__ == "__main__":
    app.run(debug=True)
