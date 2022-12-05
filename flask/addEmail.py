import boto3
import requests
from flask import Flask,jsonify,request,render_template


app = Flask(__name__)


@app.route('/')
def index():
        return render_template("index.html")

client = boto3.client(
        "sns",
        aws_access_key_id="xxxxxxxxxxxxxxxxx",
        aws_secret_access_key="xxxxxxxxxxxxx",
        region_name="us-east-1")

topic_arn=""

#create joke of day topic
def createTopic():
        response = client.create_topic(Name="joke_of_day")
        global topic_arn
        topic_arn = response["TopicArn"]

#add email to topic joke_of_day
def sns(email):
        subscribed = False
        subscriptions = client.list_subscriptions_by_topic(TopicArn=topic_arn).get('Subscriptions')
        for subscription in subscriptions:
                if ((email == subscription.get('Endpoint')) and (subscription.get('SubscriptionArn') != 'PendingConfirmation')):
                        subscribed = True
        if not subscribed:
                response = client.subscribe(TopicArn=topic_arn, Protocol="Email", Endpoint= email)
                subscription_arn = response["SubscriptionArn"]

#get email from user input
@app.route('/recievedEmail', methods = ['POST'])
def getEmail():
        createTopic()
        email = request.form.get('email')
        sns(email)
        return render_template("recivedEmail.html")


if __name__ == '__main__':
        app.run (host="0.0.0.0", port=8080)
