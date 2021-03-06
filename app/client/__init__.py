""" Client App """

from flask import Blueprint, render_template
from app.api.rest.payment.payment import PayU,PaymentFactory
import json
from flask import request

# client_bp = Blueprint('client_app', __name__,
#                         url_prefix='',
#                         static_url_path='/dist',
#                         static_folder='./app/dist',
#                         template_folder='./app/',
#                         )
client_bp = Blueprint('client_app', __name__,
                        url_prefix='',
                        static_url_path='/dist',
                        static_folder='./app',
                        template_folder='./app/',
                        )
@client_bp.route('/')
def index():
    return render_template('external_index.html')

@client_bp.route('/external')
def external():
    return render_template('external_index.html')

@client_bp.route('/juspay',methods=['GET','POST'])
def juspay():
    message = ""
    try:
        if request.method == "POST":
            message = str(request.form)
        elif request.method == "GET":
            message = request.args.get('status',"no status found") + request.args.get('signature','no signature found')
    except Exception as e:
        message = str(e)
    return render_template('juspay.html',message=message)

@client_bp.route('/paymentsuccess',methods=['GET','POST'])
def payment_success():
    try:
        #return render_template('payment.html',message=json.dumps(request.form))
        payment_gateway = PaymentFactory().get_payment_gateway("payu")
        payment_validated = payment_gateway.validate_payment_request(request.form)
        if payment_validated['validtransaction'] == 'true':
            return render_template('payment.html',message=payment_validated['message'])
        else:
            return render_template('payment.html',message=payment_validated['message'])
    except Exception as e:
        return render_template('payment.html',message=str(e))

@client_bp.route('/paymentfailure',methods=['GET','POST'])
def payment_failure():    
    payment_gateway = PaymentFactory().get_payment_gateway('payu')
    paymentfailure = payment_gateway.failed_transaction(request.form)
    return render_template('payment.html',message="Payment failure. Please contact the administrator at info@squiry.in")
