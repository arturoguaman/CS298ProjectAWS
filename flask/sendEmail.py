import boto3
import requests
from flask import Flask,jsonify,request
from jokeapi import Jokes
import asyncio

app = Flask(__name__)

client = boto3.client(
        "sns",
        aws_access_key_id="xxxxxxxxxxxxxxx",
        aws_secret_access_key="xxxxxxxxxxxxxxxxxx",
        region_name="us-east-1")

response = client.create_topic(Name="joke_of_day")
topic_arn = response["TopicArn"]

#retrive joke from jokeapi
async def print_joke():
        global jokeLine
        j = await Jokes()  # Initialise the class
        joke = await j.get_joke(blacklist=['nsfw','racist','religious','political','sexist','explicit'])  # Retrieve a random joke
        if joke["type"] == "single": # Print the joke
                jokeLine = joke["joke"]
                print(jokeLine)
        else:
                jokeLine = joke["setup"] + joke["delivery"]
                print(jokeLine)

asyncio.run(print_joke())

#send joke to all subscribers in email
client.publish(TopicArn=topic_arn,
                Message = jokeLine,
                Subject="Joke Of The Day!")
