from flask import Flask, request, render_template
from flaskext.mysql import MySQL

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates'
            )

app.config['MYSQL_DATABASE_HOST'] = 'codezero.cu4oiapmpfoz.ap-northeast-2.rds.amazonaws.com'
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'ehalthf93'
app.config['MYSQL_DATABASE_DB'] = 'metro'

mysql = MySQL()
mysql.init_app(app)

@app.route("/")
def index():
    cursor = mysql.get_db().cursor()
    cursor.execute("select * from todo order by id desc")

    column_names = [x[0] for x in cursor.description]
    results = cursor.fetchall()
    print(results)

    todo_list = []
    for result in results:
        todo_list.append(dict(zip(column_names, result)))

    print(todo_list)
    return render_template('todo.html', todo_list=todo_list)

@app.route("/todo", methods=['POST'])
def save_todo():
    body_data = request.json
    todo = body_data['todo']

    cursor = mysql.get_db().cursor()
    cursor.execute("INSERT INTO todo(todo) values (%s)", todo)
    mysql.get_db().commit()
    return {"message":"success"}

@app.route("/todo", methods=['DELETE'])
def delete_todo():
    args = request.args
    id = args.get('id')

    cursor = mysql.get_db().cursor()
    cursor.execute("delete from todo where id = %s", id)
    mysql.get_db().commit()
    return {"message":"success"}

if __name__ == '__main__':
    app.run(debug=True)