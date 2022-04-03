from flask import Flask, render_template, request 
import managedb
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
# from docker.director import Director
import utils.extract_validate as extract_validate
import utils.data_helper as data_helper

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'files'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/')  
def message():  
      return render_template("login.html")  
    
@app.route('/signup', methods=["GET"])  
def signup():
    return render_template("signup.html")  

@app.route('/storeinfo', methods=["POST"])  
def storeinfo():
    username= request.form['username']
    password=request.form['password']
    AI =request.form.get('AI Developer')
    Deployer=request.form.get('Deployer')
    Admin=request.form.get('Admin')
    App=request.form.get('App Developer')
    roles_list=[]
    if AI is not None:
        roles_list.append("AI")
    if Deployer is not None:
        roles_list.append("Deployer")
    if Admin is not None:
        roles_list.append("Admin")
    if App is not None:
        roles_list.append("App")
    print(roles_list)
    ret_statement=managedb.storeData(username,password,roles_list)
    if(ret_statement=="User Already Exist"):
        return render_template("signup.html")
    return render_template("login.html")  


@app.route('/login', methods=["POST"])  
def login():
    username= request.form['username']
    password=request.form['password']
    role =request.form['role']
    check=managedb.checkCredentials(username,password,role)
    if(check=="Invalid Credentials" or check=="Invalid Role"):
        return render_template("login.html")  

    # print(username)
    # print(password)
    if(role=="AI"):
        return render_template("appaccess.html")  
    if(role=="Deployer"):
        return render_template("appaccess.html")  
    if(role=="Admin"):
        return render_template("appaccess.html")  
    if(role=="App"):
        return render_template("appaccess.html")  


@app.route('/upload', methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        #create a custom filename
        cur_index = data_helper.get_last_index()
        filename = "model_"+str(cur_index)+".zip"
        print(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER']))
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],filename)) # Then save the file
    
        # validation_val=extract_validate.validation()
        # if(validation_val):
        #     return "File uploaded and Authenticated successfully" 
        return "File is not uploaded and Auth successfully"
    return render_template('index.html', form=form)



if __name__ == '__main__':  
   app.run(debug = True)  