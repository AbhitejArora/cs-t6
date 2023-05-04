from flask import Flask, request, make_response
import model

app = Flask(__name__)


@app.route('/')
def main():
    return "nothing here"


@app.route('/chat', methods=['POST'])
def chat():
    if request.method == 'POST':
        # data['query'] contains the user query
        data = request.get_json()

        # Call the model here and get the answer
        answer = model.get_answer(data['query'])

        return make_response({"answer": answer}, 200)
    else:
        return make_response("Method not allowed", 405)
