from flask import Flask, render_template

app = Flask(__name__)

# this function is called by flask framework
@app.route('/')
def index():
    personal_info = {
        'blood_type': 'B',
        'height':180,
        'mbti':'INTJ'
    }
    foods = ['라면', '떡복기', '낙지']
    return render_template('index.html',
                           name='KyuSahm Kim',
                           age=47,
                           info=personal_info,
                           foods=foods)

if __name__ == '__main__':
    app.run(debug=True)