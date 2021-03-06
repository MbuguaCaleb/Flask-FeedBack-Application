from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/lexus'

else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://aisanoxjesqgaw:c9c47714ed6d51fe87884290a496ea7106d19e719a4cebf853a7805713676018@ec2-174-129-33-75.compute-1.amazonaws.com:5432/d7cds56hov5aon'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# creating a database object
db = SQLAlchemy(app)


# SQL Alchemy ORM database class
# creating table instance via an ORM
# database Model Class
class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200))
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    # initializer//constructor
    def __init__(self, customer, dealer, rating, comments):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']

       # print(customer, dealer, rating, comments)

       # Validtion checks
        if customer == '' or dealer == '':
            return render_template('index.html', message='Please enter required fields!!')

        #Quering  from the Model if the customer already exists
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer, dealer,rating,comments)
            db.session.add(data)
            db.session.commit()
            send_mail(customer, dealer,rating,comments)
            return render_template('success.html')
        
        #Runs if above is not true
        #like an else stmt
        return render_template('index.html', message='You have already submitted feedback!!')



if __name__ == '__main__':
    app.debug = True
    app.run()
