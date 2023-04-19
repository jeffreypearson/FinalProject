from flask import Flask, render_template, request
import boto3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('error.html')

@app.route('/FinalProject/dashboard.html/upload', methods=['POST'])
def upload():
    try:
        s3 = boto3.client('s3')
        bucket = 'jp-finalproject'
        key = 'arn:aws:kms:us-west-1:159174804900:key/cf9b6d23-eb04-44c9-965f-72d445eef657'
        file = request.files['file']

        s3.upload_fileobj(file, bucket, key)

        return 'File uploaded successfully!'
    except:
        return render_template('error.html')

if __name__ == '__main__':
    app.run()