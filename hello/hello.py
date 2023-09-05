from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)


@app.route('/aj')
def hello():
    return 'hi'


@app.route('/',methods=['GET'])
def info():
    
    if request.method == 'GET':
   # If 'name' is None, the user has requested page the first time
        if(request.args.get('name') == None):
            return render_template('index.html')
          
        elif(request.args.get('name' ) == ''):
            return "<html><body> <h1>Invalid number</h1></body></html>"
        else:       
            name = request.args.get('name')
            age = request.args.get('age')
            roll = request.args.get('roll')
            if name == 'a':
                return redirect(url_for('hello'))
            
            return render_template('hello.html',age=age,roll=roll,name=name)
        
  
@app.route("/video")
def serve_video():
    message = "Video Route"
    return render_template('video.html', message=message)
  
  
@app.route("/audio")
def serve_audio():
    message = "Audio Route"
    return render_template('audio.html', message=message)
  
  
@app.route("/image")
def serve_image():
    message = "Image Route"
    return render_template('image.html', message=message)
  
        


if __name__== "__main__":
    app.run(debug=True)
    


