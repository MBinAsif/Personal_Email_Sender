from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

def load_recipients(file_path):
    return pd.read_csv(file_path)

def create_email(sender_email, recipient_email, subject, html_content):
    msg = MIMEMultipart('alternative')
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(html_content, 'html'))
    return msg

def send_email(smtp_server, smtp_port, login, password, msg):
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(login, password)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            return True
    except Exception as e:
        return str(e)

def personalize_content(template, recipient_details):
    for key, value in recipient_details.items():
        template = template.replace(f"{{{{ {key} }}}}", str(value))
    return template

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sender_email = request.form['sender_email']
        subject = request.form['subject']
        header = request.form['header']
        content = request.form['content']
        footer = request.form['footer']
        recipients_file = request.files['recipients']

        recipients_path = os.path.join('uploads', recipients_file.filename)
        recipients_file.save(recipients_path)

        recipients = load_recipients(recipients_path)

        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        login = 'mbinasifmba18@gmail.com'
        password = 'qwnl zelk zbyw zoes'  # Use App Password for Gmail

        success_count = 0
        fail_count = 0

        for index, row in recipients.iterrows():
            recipient_email = row['email']
            recipient_details = row.to_dict()
            
            email_subject = personalize_content(subject, recipient_details)
            email_body = f"{header}\n\n{content}\n\n{footer}"
            email_content = personalize_content(email_body, recipient_details)

            msg = create_email(sender_email, recipient_email, email_subject, email_content)
            result = send_email(smtp_server, smtp_port, login, password, msg)

            if result is True:
                success_count += 1
            else:
                fail_count += 1
                flash(f"Failed to send email to {recipient_email}. Error: {result}", 'error')

        flash(f'Successfully sent {success_count} emails.', 'success')
        if fail_count > 0:
            flash(f'Failed to send {fail_count} emails.', 'error')
        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
