""" Client App """

from flask import Blueprint, render_template
from app.api.rest.payment import payment
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
    return render_template('index.html')

@client_bp.route('/external')
def external():
    return render_template('external_index.html')

@client_bp.route('/paymentsuccess',methods=['GET','POST'])
def payment_success():
    try:

        #return render_template('payment.html',message=json.dumps(request.form))
        payment_gateway = PaymentFactory().get_payment_gateway(gateway)
        payment_validated = payment_gateway.validate_payment_request(request.form)
        if payment_validated['validtransaction'] == 'true':
            return render_template('payment.html',message=payment_validated['message'])
        else:
            return render_template('payment.html',message=payment_validated['message'])
    except Exception as e:
        return render_template('payment.html',message=str(e))


@client_bp.route('/paymentfailure',methods=['GET','POST'])
def payment_failure():    
    render_template('payment.html',message=request.POST["status"])
