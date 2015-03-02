from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from admin import *

app = Flask(__name__)
app.debug = True
Bootstrap(app)
admin = Admin(app)
admin.add_view(AdminPanel(name='Images'))

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run()
