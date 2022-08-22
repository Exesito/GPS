import random

from flask import render_template, request, redirect, url_for
from transbank.error.transbank_error import TransbankError
from transbank.webpay.webpay_plus.transaction import Transaction
from app.models import domo_reserva, domo_restaurante

from webpay import bp


@bp.route("create/<rsv_id>/<cli_id>", methods=["GET", "POST"])
def webpay_plus_create(rsv_id, cli_id):
    
    buy_order = str(rsv_id)
    session_id = str(cli_id)
    amount = 5000
    return_url = request.url_root + 'webpay-plus/commit'

    create_request = {
        "buy_order": buy_order,
        "session_id": session_id,
        "amount": amount,
        "return_url": return_url
    }

    response = (Transaction()).create(buy_order, session_id, amount, return_url)

    return render_template('webpay/create.html', response=response, request = create_request)


@bp.route("commit", methods=["GET"])
def webpay_plus_commit():
    token = request.args.get("token_ws")
    print("commit for token_ws: {}".format(token))

    response = (Transaction()).commit(token=token)
    print("response: {}".format(response))

    return redirect(url_for('reserva_exitosa', id_restaurante = domo_reserva.get_by_id(response['buy_order']).get_restaurante(), id_reserva= response['buy_order']))

@bp.route("commit", methods=["POST"])
def webpay_plus_commit_error():
    token = request.form.get("token_ws")
    print("commit error for token_ws: {}".format(token))

    #response = Transaction.commit(token=token)
    #print("response: {}".format(response))
    response = {
        "error": "Transacción con errores"
    }

    return redirect(url_for('reserva_error'))