# Young Masterbuilders in Motion

- [Young Masterbuilders in Motion](#young-masterbuilders-in-motion)
  - [Getting Started With The App](#getting-started-with-the-app)
    - [Mac/Linux Users](#maclinux-users)
    - [PC Users (currently incomplete)](#pc-users-currently-incomplete)
  - [Developing On The App](#developing-on-the-app)
  - [What Technologies Are We Using?](#what-technologies-are-we-using)

## Getting Started With The App

I'm going to be very blunt: this will be much, much easier on a Mac or Linux system than it will be on a PC. On any PC that doesn't have Hyper-V (any system running any OS older/less powerful than Win10 Pro), you're going to need to run older, mostly unsupported programs. We strongly recommend that you either use a Mac or move to Linux.

### Mac/Linux Users
- Install homebrew

        /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

- Install Node & NPM

        brew install node

- Install Pipenv: 
  
        brew install pipenv

- [Download and Install Docker](https://download.docker.com/mac/stable/Docker.dmg)
- Set up Pipenv:
    ```
    cd backend
    pipenv install
    cd ..
    ```
- Start Docker containers: 

        docker-compose up

### PC Users (currently incomplete)

- Install [Docker Toolbox for Windows](https://docs.docker.com/toolbox/overview/)

## Developing On The App
Once you have your containers running, the code in your local directory will be linked with the code inside the Docker containers. When you make changes, the app will reboot inside the containers to reflect those changes. The API will be accessible in your browser at `localhost:8000`, and the frontend application will be available at `localhost:3000`.

## What Technologies Are We Using?
The backend application is written in Python, using the [Django](https://www.djangoproject.com/) framework and the [Django REST Framework](https://www.django-rest-framework.org/) library. The frontend application is written in Javascript, using the [React](https://reactjs.org/) framework and several other third party libraries, bootstrapped via the [create-react-app](https://github.com/facebook/create-react-app) tool.

If you need to add new packages to the backend app, you can use Pipenv to do so:

    pipenv install <package_name>

If you need to add new packages to the frontend app, you can use Yarn to do so:

    yarn install <package_name>

Generally speaking, look to handle data manipulation on the backend and visualization on the frontend.