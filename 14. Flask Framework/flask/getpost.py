from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
  return "<html>Welcome to the flask course</html>"

@app.route('/index',methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

# post request
@app.route('/contact', methods=['GET', 'POST'])
def contact():
  if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # process the form data
    return f"Thank you {name} for contacting us!"
  return render_template('contact.html')

if __name__ == '__main__':
  app.run(debug=True)