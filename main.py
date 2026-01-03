import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_text = data.get('msg', '')
    try:
        # Это простой поиск, чтобы бот хоть что-то отвечал
        url = f"https://api.duckduckgo.com/?q={user_text}&format=json"
        res = requests.get(url).json()
        answer = res.get('AbstractText') or f"Брат, я нашел инфу про '{user_text}', но сформулируй точнее."
    except:
        answer = "Ошибка связи."
    return jsonify({"response": answer})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
