from flask import Flask, request

app = Flask(__name__)

# this function is called by flask framework
@app.route('/query')
def index():
    args = request.args
    id = args.get('id')
    print(id)
    return "Query String!!"

if __name__ == '__main__':
    app.run(debug=True)