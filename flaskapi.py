from flask import Flask, json

companies = [{"id": 1, "name": "Company one"},
             {"id": 2, "name": "Company two"}]

api = Flask(__name__)


@api.route('/companies', methods=['GET'])
def get_companies():
    return json.dumps(companies)


@api.route('/companies', methods=['POST'])
def post_companies():
    return json.dumps({"success": True}), 201


if __name__ == '__main__':
    api.run()
