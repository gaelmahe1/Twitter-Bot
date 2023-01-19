# Twitter-Bot
This is a simple twitter bot that posts the latest stories from Hacker News to a Twitter account. It uses the Hacker News API to get the latest stories and the Tweepy library to post the stories to Twitter.

Prerequisites :

You'll need to have a Twitter account and create a Twitter developer account to get your API keys.
You'll also need to have Python and pip installed on your machine.
Usage
Clone the repository to your local machine

- git clone https://github.com/YOUR_USERNAME/twitter-bot.git

Install the required packages:

- pip install -r requirements.txt

Create a .env file in the root of the project with the following format:

-CONSUMER_KEY=YOUR_CONSUMER_KEY
CONSUMER_SECRET=YOUR_CONSUMER_SECRET
ACCESS_TOKEN=YOUR_ACCESS_TOKEN
ACCESS_SECRET=YOUR_ACCESS_SECRET

Replace the YOUR_CONSUMER_KEY, YOUR_CONSUMER_SECRET, YOUR_ACCESS_TOKEN, and YOUR_ACCESS_SECRET placeholders in the code with your actual API keys.

Run the script :

- python twitter-bot.py

Customization:

You can adjust the frequency at which stories are posted by changing the value of the time.sleep() function. The value is in seconds.
You can also customize the tweet format by editing the tweet = f"{story_title} {story_link}" line of code.

- Note
Be aware of the rate limits and usage policy of the API you are using.
Use of this code is at your own risk.



