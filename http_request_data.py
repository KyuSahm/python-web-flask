from flask import Flask, request

app = Flask(__name__)

# this function is called by flask framework
# Get Method with query string
@app.route('/query')
def index():
    args = request.args
    id = args.get('id')
    date = args.get('date')
    print(id)
    print(date)
    return "Query String!!"

# Get Method with path parameter
@app.route('/path/<id>/<date>')
def path_param(id, date):
    print(id)
    print(date)
    return "Path Param!!"

# Post Method
@app.route('/body', methods=['POST'])
def request_body():
    print(request.json)
    body = request.json
    id = body['id']
    name = body['name']

    print(id)
    print(name)
    return "Request Body!!"

if __name__ == '__main__':
    app.run(debug=True)