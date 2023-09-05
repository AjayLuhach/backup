from flask import Flask,request,redirect,url_for,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/success')
def success():
    return "<html>hi</html>"

@app.route('/login',methods=['GET'])
def login():
    if request.method == 'GET':
        if request.args.get('name') == "ajay":
            return redirect(url_for('success'))
        else:
            return 'invalid'
        
        
if __name__==('__main__'):
    app.run(debug=True)
    
        

    
