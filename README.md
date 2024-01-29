# Project Name

Semantic Kernel Hackathon Project

## What

This is a hackakathon project to utilize Semantic Kernel to build a sample web application. The web application is a simple tool that allows users to retrieve his/her unread emails in a summary format, propose possible replies, detect the sentiment of the email, and search for email with keywords.

It features
- 3 Semantic Functions (reply email, summarize emails) in the folder [plugins](./semantic_kernel/plugins/)
- 1 Native Function with Semantic Memory integration - [search email](./semantic_kernel/search_emails.py#55)

[![Watch the Demo](./assets/image.png)](./assets/demo.mp4)

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

- [Semantic-Kernel](https://github.com/microsoft/semantic-kernel)
- [django web framework](https://www.djangoproject.com/)
- [python](https://www.python.org/)

## Contributing

Feel free to clone this repo and submit a pull request with any changes.

## Is it ready for re-use?

No, this was built for a hackathon. It is currently not in a state to be re-used.