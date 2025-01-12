from flask import *
from flask import Blueprint
from database import *
import os
from werkzeug.utils import secure_filename
from flask_socketio import SocketIO, send


app = Flask(__name__)
public = Blueprint('public',__name__)
app.secret_key = 'Ann28784'
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
#if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}


log_f=0
img_yes=0

# seller_bp = Blueprint('seller', __name__, url_prefix='/welcome')
@public.route('/')
def home():
    qry="select * from plot"
    plots=select(qry)
    return render_template('index.html',plots=plots)

    
@public.route('/register',methods=['GET','POST'])
def register():
    if 'submit' in request.form:
        name=request.form['name']
        email=request.form['email']
        phno=request.form['phno']
        pan=request.form['pan']
        password=request.form['password']

        qry4="insert into register values(null,'%s','%s','%s','%s',%s,null,CURRENT_TIMESTAMP)"%(name,email,phno,pan,password)
        res=insert(qry4)
        if res>0:
            return render_template('login.html')
    return render_template('register.html')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@public.route('/welcome',methods=['GET','POST'])
def welcome():
    id=session['id']
    file = request.files['image']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Insert image path into database
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        qry="update register set img='%s' where id=%s"%(image_path,id)
        update(qry)
    return render_template('welcome.html',image_path=image_path)

@public.route('/login',methods=['GET','POST'])
def login():
    if 'submit' in request.form:
        username=request.form['username']
        password=request.form['password']
        qry="select * from register where email='%s' AND pass='%s'"%(username,password)
        n=select(qry)
        if n:
            session['id']= n[0]['id']
            session['name']= n[0]['name']
            session['email']= n[0]['email']
            session['phno']= n[0]['phno']
            image=n[0]['img']
            if n[0]['img'] is 'None':
                img_yes=0
            else:
                img_yes=1
    # Access values by column names
            qry="insert into login values(null,'%s','%s',CURRENT_TIMESTAMP)"%(username,password)
            log_f=1
            insert(qry)
            return render_template('welcome.html',name=session['name'],id=session['id'],image=image)
        else:
            return "No username provided"
    return render_template('login.html')


@public.route('/add_plot',methods=['GET','POST'])
def addplot():
    if 'submit' in request.form:
        pname=request.form['name']
        email=request.form['email']
        phno=request.form['phno']
        location=request.form['loc']
        size=request.form['size']
        price=request.form['price']
        feature=request.form['feature']
        view=request.form['view']
        if 'img' not in request.files:
            return "No file part", 400 
    file = request.files.get('img')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
        # qry="insert into login values(null,'%s','%s','buyer')"%(email,password)
        # res=insert(qry)

        qry1="insert into plot values(null,'%s','%s',%s,'%s',%s,%s,'%s','%s','%s',CURRENT_TIMESTAMP)"%(pname,email,phno,location,size,price,feature,view,img_path)
        n=insert(qry1)
        if n :
            return "Plot added successfully"
        else:
            return "Plot not added"
    return render_template('add_plot.html',name=session['name'],email=session['email'],phno=session['phno'])

@public.route('/view_plot',methods=['GET','POST'])
def viewplot():
    qry="select * from plot where email='%s'"%(session['email'])
    plots=select(qry)
    return render_template('view_plot.html',plots=plots)




@public.route('/edit_plot',methods=['GET','POST'])
def edit_plot():
    id= request.args.get('pid')#access the id from html page
    qry="select * from plot where id='%s'"%(id)
    plot=select(qry)
    if 'submit' in request.form:
        pname=request.form['name']
        email=request.form['email']
        phno=request.form['phno']
        location=request.form['loc']
        size=request.form['size']
        price=request.form['price']
        feature=request.form['feature']
        view=request.form['view']
        if 'img' not in request.files:
            return "No file part", 400 
        file = request.files.get('img')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
        qry1="update plot set name='%s',email='%s',phno='%s',location='%s',size='%s',price='%s',features='%s',view='%s',img='%s' where id='%s'"%(pname,email,phno,location,size,price,feature,view,img_path,id)
        res=update(qry1)
        if res>0:
            return render_template('view_plot.html')
    return render_template('edit_plot.html',plot=plot[0])


@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    image_name = file.filename
    image_data = file.read()  # Read image data as binary

    # insert_image_into_db(image_name, image_data)
    
    return jsonify({'success': 'Image uploaded and stored in database'})


@public.route('/chat',methods=['GET','POST'])
def chat():
    qry="select * from plot where email='%s'"%(session['email'])
    plots=select(qry)
    return render_template('chat.html',plots=plots)

@public.route('/find_plot',methods=['GET','POST'])
def find_plot():
    #search codeusing AI
    return render_template('find_plot.html')

@public.route('/delete_plot',methods=['POST'])
def delete_plot():
    #search codeusing AI
    return jsonify({'status': 'Plot deleted successfully!'})