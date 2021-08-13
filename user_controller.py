from flask import Flask, request
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'codezero.cu4oiapmpfoz.ap-northeast-2.rds.amazonaws.com'
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'ehalthf93'
app.config['MYSQL_DATABASE_DB'] = 'metro'

mysql = MySQL()
mysql.init_app(app)

@app.route('/user')
def get_one_user():
    args = request.args
    id = args.get('id')

    cursor = mysql.get_db().cursor()
    cursor.execute("select * from user where id=%s", id)

    column_names = [x[0] for x in cursor.description]
    result = cursor.fetchone()

    print("cursor.description: {}".format(cursor.description))
    print("result: {}".format(result))
    response =dict(zip(column_names, result))

    return response

@app.route('/users')
def get_users():
    cursor = mysql.get_db().cursor()
    cursor.execute("select * from user")

    column_names = [x[0] for x in cursor.description]
    results = cursor.fetchall()

    print("cursor.description: {}".format(cursor.description))
    print("results: {}".format(results))
    user_list = []
    for result in results:
        user_list.append(dict(zip(column_names, result)))
    response = {"user_list":user_list}

    return response

@app.route('/user', methods=['POST'])
def save_user():
    body_data = request.json
    id = body_data['id']
    name = body_data['name']
    email = body_data['email']
    password = body_data['password']

    cursor = mysql.get_db().cursor()
    cursor.execute("INSERT INTO user VALUES (%s, %s, %s, %s)", (id, name, email, password))

    mysql.get_db().commit()

    return {"message":"success"}

@app.route('/user', methods=['DELETE'])
def delete_user():
    args = request.args
    id = args.get('id')

    cursor = mysql.get_db().cursor()
    cursor.execute("delete from user where id=%s", id)

    mysql.get_db().commit()
    return {"message": "success"}

if __name__ == '__main__':
    app.run(debug=True)
