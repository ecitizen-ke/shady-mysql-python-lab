from flask import Blueprint, request, jsonify

from app.models import State

states_bp = Blueprint('states_bp', __name__)


@states_bp.route('/api/states', methods=['GET'])
def get_states():
    state = State()
    states = state.get_states()
    return jsonify({"message": "states retrieved successfully", "status": 200, "result": states})


@states_bp.route('/api/create', methods=['POST'])
def store():
    data = request.get_json()
    name = data.get("name")
    abbreviation = data.get("abbreviation")
    capital = data.get("capital")
    population = data.get("population")
    year_admitted = data.get("year_admitted")

    state = State()

    result = state.save(name, abbreviation, capital, population, year_admitted)
    return jsonify({"result": result['result'], 'message': result['message'], 'status': result['status']})


# Filter States by Starting Letter
@states_bp.route('/api/states/starting_with/<string:letter>', methods=['GET'])
def get_states_starting_with(letter):
    state = State()
    result = state.filter_states_by_starting_letter(letter)
    return jsonify({"message": result['message'], "status": result['status'], "result": result['result']})


# Update a State's Population
@states_bp.route('/api/states/<int:id>', methods=['PUT'])
def update_state_population(state_id):
    data = request.get_json()
    population = data.get("population")

    state = State()
    result = state.update_state_population(state_id, population)
    return jsonify({"message": result['message'], "status": result['status'], "result": result['result']})


# Task 5: Delete a State
@states_bp.route('/api/states/<int:id>', methods=['DELETE'])
def delete_state(state_id):
    state = State()
    result = state.delete_state(state_id)
    return jsonify({"message": result['message'], "status": result['status'], "result": result['result']})


# Task 6: Search for a State by Name
@states_bp.route('/api/states/search/<string:name>', methods=['GET'])
def search_state(name):
    state = State()
    result = state.search_state_by_name(name)
    return jsonify({"message": result['message'], "status": result['status'], "result": result['result']})


# Task 7: List All State Capitals
@states_bp.route('/api/states/capitals', methods=['GET'])
def get_state_capitals():
    state = State()
    result = state.list_all_state_capitals()
    return jsonify({"message": result['message'], "status": result['status'], "result": result['result']})


# Task 8: Find the Most Populous State
@states_bp.route('/api/states/most_populous', methods=['GET'])
def get_most_populous_state():
    state = State()
    result = state.find_most_populous_state()
    return jsonify({"message": result['message'], "status": result['status'], "result": result['result']})


# Task 9: Calculate the Average Population
@states_bp.route('/api/states/average_population', methods=['GET'])
def calculate_average_population():
    state = State()
    result = state.calculate_average_population()
    return jsonify({"message": result['message'], "status": result['status'], "result": result['result']})


# Task 10: List States Admitted After a Certain Year
@states_bp.route('/api/states/admitted_after/<int:year>', methods=['GET'])
def list_states_admitted_after_year(year):
    state = State()
    result = state.list_states_admitted_after_year(year)
    return jsonify({"message": result['message'], "status": result['status'], "result": result['result']})


# Task 11: Count States by Population Range
@states_bp.route('/api/states/population_range/<int:lower_bound>/<int:upper_bound>', methods=['GET'])
def count_states_by_population_range(lower_bound, upper_bound):
    state = State()
    result = state.count_states_by_population_range(lower_bound, upper_bound)
    return jsonify({"message": result['message'], "status": result['status'], "result": result['result']})


# Task 12: Join States with Capitals Table
@states_bp.route('/api/states/join_with_capitals', methods=['GET'])
def join_states_with_capitals():
    state = State()
    result = state.join_states_with_capitals()
    return jsonify({"message": result['message'], "status": result['status'], "result": result['result']})
