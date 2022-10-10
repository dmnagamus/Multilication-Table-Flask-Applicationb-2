from flask import *
app = Flask(__name__)

@app.router('/')
def message():
	return render_template('message.html')
if__name__ == '__main__' :
app.run(debug = True)
