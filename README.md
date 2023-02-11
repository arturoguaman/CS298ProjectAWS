# CS298ProjectAWS

This application uses aws SNS,EC2 and JokeofDay API to send email of a joke to all sbscribers of topic Joke_of_day
1) A python script 'addEmail.py' retrives email from user input. Checks if email is subscribed. If not a subscribe request 
   email will be sent.
2) A python script 'sendEmail.py' retrieves random joke from API and sends joke to all subscribers of topic Joke_of_day
3) Optionally a cron command can be run to send emails to all subscribers at a sheduled time.

![My Image](Diagram.png)
