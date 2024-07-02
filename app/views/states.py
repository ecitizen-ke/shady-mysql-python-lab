from flask import Blueprint

states_bp = Blueprint('states_bp',__name__)

@states_bp.route('store',methods=['POST'])
def store():
    state ='
    return state