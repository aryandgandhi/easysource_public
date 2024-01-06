# EasySource

## Introduction

Welcome to EasySource, a web application designed to bridge the gap between new developers and the world of open-source projects. Built with Django, this tool simplifies the exploration of GitHub repositories, offering insights into project structures and coding languages. It helps in understanding and contributing to the vibrant open-source community.

## Key Features

- **Streamlined Browsing**: Effortlessly explore open-source projects on GitHub.
- **Educational Tool**: Understand project structures and languages, ideal for new developers.
- **Technical Backbone**: Built with Django for robustness and efficiency.

## Technical Architecture

- **Backend**: Django Framework, chosen for its comprehensive features and rapid development capabilities.
- **Hosting**: Heroku, providing seamless integration and ease of use.
- **Database**: PostgreSQL, for its SQL compliance, JSON support, and robustness.
- **Caching**: Redis, enhancing performance with in-memory data storage.
- **Asynchronous Tasks**: RabbitMQ and Celery, for efficient handling of background processes.

## Getting Started

### Prerequisites

- Python 3.x
- Git

### Installation

**the purpose of this repo is to just show the barebones of the code written, I've removed a handful of files that weren't necessary for a barebones demo. DM me on Twitter @aryan_gandhi101 if you'd like to install the whole project

1. Clone the repository: `git clone https://github.com/aryandgandhi/easysource_public.git`
2. Navigate to the project: `cd easysource_public`
3. Install dependencies: `pip install -r requirements.txt`
4. Set up your local environment settings.
5. Run the Django migrations: `python manage.py migrate`
6. Start the server: `python manage.py runserver`
   

### Usage

Navigate to `http://localhost:8000` in your browser to start exploring open-source projects on GitHub.

## Future Roadmap

- **Integration with Other Platforms**: Expanding beyond GitHub to platforms like GitLab and Bitbucket.
- **Project Ranking System**: Introducing metrics-based rankings for projects.
- **Notification System**: Opt-in alerts for updates on starred or followed projects.
- **Performance Optimization**: Strategies to handle growing user base and traffic.

