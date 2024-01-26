# Project Name

Semantic Kernel Hackathon Project

## What

This is a hackakathon project to utilize Semantic Kernel to build a web application. The web application is a simple web application that allows users to retrieve his/her unread emails in a summary format, propose possible replies, and detect the sentiment of the email.

## Get started

- Deploy an OpenAI instance in a subscription
- Set up `.env` file in /django. See [.env.sample](./django/.env.sample) for an example.
- Install dependencies and set up shell by running 

```bash
pip install -U pipenv
cd django
pipenv install django
pipenv shell
```

- Start the server by running

```bash
python manage.py runserver 
```

- Done! Visit your application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


## Tech Stack

- semantic-kernel
- django

## Contributing

Feel free to clone this repo and submit a pull request with any changes.

## Is it ready for re-use?

No, this was built for a hackathon. It is currently not in a state to be re-used.