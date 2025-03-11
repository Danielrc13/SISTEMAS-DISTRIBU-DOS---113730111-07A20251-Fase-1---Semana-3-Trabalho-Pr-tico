from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def receber_login():
    dados = request.get_json()
    login = dados.get("login")
    senha = dados.get("senha")

    if not login or not senha:
        return jsonify({"erro": "Login ou senha não fornecidos"}), 400

    return jsonify({"login": login, "senha": senha}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
