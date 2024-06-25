from flask import Flask, request, redirect, url_for, render_template, flash
from flask_mail import Mail, Message
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'jc1234'  # Replace with your generated secret key

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ilaraecodes@gmail.com'
app.config['MAIL_PASSWORD'] = 'cjyr hofv smwa ajaz'

mail = Mail(app)

# MongoDB connection setup
mongo_client = MongoClient('mongodb+srv://ilaraecodes:Prayalways1986!@emaillist.tpnge6l.mongodb.net/')
db = mongo_client['EmailList']
collection = db['contacts']

def send_email(recipient_email):
    """Send an email to the specified recipient with HTML styling and a signup link."""
    msg = Message("Join Our Community!", sender=app.config['MAIL_USERNAME'], recipients=[recipient_email])

    # HTML Content with a signup
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Join Our Community</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                margin: 0;
                padding: 0;
                -webkit-font-smoothing: antialiased;
                -moz-osx-font-smoothing: grayscale;
            }
            .container {
                width: 100%;
                max-width: 400px;
                margin: 0 auto;
                padding: 20px;
                background-color: #ffffff;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                text-align: center;
            }
            .container img {
                width: 100%;
                border-radius: 8px 8px 0 0;
            }
            .content {
                padding: 20px;
            }
            .content h2 {
                font-size: 24px;
                margin-bottom: 16px;
            }
            .content p {
                font-size: 16px;
                margin-bottom: 24px;
            }
            .btn {
                background-color: #007bff;
                border: none;
                border-radius: 4px;
                color: #ffffff;
                padding: 10px 20px;
                text-decoration: none;
                font-size: 16px;
                display: inline-block;
                margin-top: 10px;
            }
            .btn:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <img src="https://foothillranchliving.com/assets/foothill-C4Za23dy.png" alt="Community">
            <div class="content">
                <h2>Join Our Community!</h2>
                <p>We are excited to have you join our community. Click the link below to sign up:</p>
                <a href="http://localhost:5000/" class="btn">Sign Up Here</a>
            </div>
        </div>
    </body>
    </html>
    """
    msg.html = html
    mail.send(msg)
    print(f'Email sent to {recipient_email}')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email_route():
    email = request.form['email']
    send_email(email)
    flash('Email sent successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
