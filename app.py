from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/findhost', methods=['POST'])
def findhost():
    data = request.get_json()
    print(data)
    name = data['dns_name']
    return render_template('findhost.html', name=name)

if __name__ == '__main__':
    app.run()