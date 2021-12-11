# LSPT_CrawlingA
Crawling A for class project

## Environment Setup
* Install Python 3
* Run `pip install beautifulsoup4 requests` to get required packages

## Note: Local Test Cases
* Use a webserver such as apache, or use something like XAMPP to host the test websites locally

## Note: Running crawler
Since we use Github REST API and Reddit API for crawling github and reddit pages, you need to set up your own access token for those API before running the crawler.
* Github Credential: set up an environment vairable "Github_token" holding your github personal token
* Reddit Credential: a dictionary of format {"username": , "password": , "appID": , "secret": } with corresponding information stored as "redditCredential.pickle"
