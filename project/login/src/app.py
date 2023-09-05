from flask import Flask,request,redirect,render_template,url_for,Blueprint
from domain.user import user as users
from flask import Flask 
from domain.models.usermodel import db,usermodel
from services.user_service import user_service
from flask_login import LoginManager , login_user, logout_user,login_manager

app = Flask(__name__)
app.config.from_object('config')

 
service = user_service(db.session)
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
 
with app.app_context():
    db.create_all()
@login_manager.user_loader
def load_user(user_id):
    return usermodel.query.get(int(user_id))  
@app.route('/register', methods=["GET", "POST"])
def register():
# If the user made a POST request, create a new user
	if request.method == "POST":
		user = users(username=request.form.get("username"),
					password=request.form.get("password"))
		# Add the user to the database
		service.register(user.username,user.password)
  
		return redirect(url_for("login"))
	# Renders sign_up template if user made a GET request
	return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
	# If a post request was made, find the user by
	# filtering for the username
	if request.method == "POST":
		user = usermodel.query.filter_by(
			username=request.form.get("username")).first()
		# Check if the password entered is the
		# same as the user's password
		if user.password == request.form.get("password"):
			# Use the login_user method to log in the user
			login_user(user)
			return redirect(url_for("home"))
		# Redirect the user back to the home
		# (we'll create the home route in a moment)
	return render_template("login.html")



@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)


