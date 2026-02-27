from flask import Flask, render_template

'''
It creates an instance of Flask class,
which will be your WSGI application. 
'''

# WSGI application 
app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('welcome.html')
  
@app.route('/about')
def about():
    return '<h1>About Page</h1><p>This is a simple Flask application.</p>'

if __name__ == '__main__':
    '''
    It runs the application on the local development server.
    '''
    app.run(debug=True)