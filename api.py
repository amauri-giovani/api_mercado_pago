import json

from flask import Flask, render_template

from main import generate_link_payment

app = Flask(__name__)
items = [
    {
        "id": "1",
        "title": "Coca-Cola",
        "description": "Refrigerante Coca-Cola",
        "quantity": 3,
        "currency_id": "BRL",
        "unit_price": 8,
    }
]


@app.route("/")
def homepage():
    link_to_payment = generate_link_payment(items)
    return render_template("index.html", link_to_payment=link_to_payment)


@app.route("/compra-certa")
def compra_certa():
    return "Compra Aprovada"


@app.route("/compra-errada")
def compra_errada():
    return "Pagamento não aprovado"


@app.route("/compra-pendente")
def compra_pendente():
    return "Aguardando confirmação de pagamento"


# @app.route("/notifications")
# def notifications(request):
#     print(request)
#     return "Notificação recebida"


@app.route("/notifications/")
async def notifications(request):
    body = await request.json()  # Ler JSON da requisição
    print("🔹 Webhook recebido:", json.dumps(body, indent=2))  # Exibir JSON formatado
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=True)
