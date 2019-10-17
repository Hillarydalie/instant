# Instant

This is a cloned of Instagram. Instagram has swept the way we have previously viewed social-media and marketing, not to mention how we shop online these days. Out of this model, I wanted to test my skills in django by building a clone of instagram using my knowledge in Django, a python framework. The application is accessible on both moble and desktop version. Your comments and feedback are highly welcome.


## Features (User Stories)
This app that allows users to post their photos and see others posted by others just as instagram.

- [x] User can register, activate their accounts and sign in.
- [x] Once signed in a user can add a their photos.
- [ ] Once signed in a user can view their photos and those of people they follow.
- [x] Once signed in User can edit their profile bio and profile picture.
- [ ] Once signed in a user can follow other users and see their pictures on my timeline.
- [ ] Once signed in a user can like a picture and comment on it.

## Screenshot

![A screenshot of the app page](https://github.com/Hillarydalie/instant/blob/master/static/localescreenshot.png "App Page")

## Getting Started

These instructions will help get you started and your copy of the project up and running on your local machine for development and testing purposes. Also see deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need to have the following. 

```
- [x] Python version 3.6 - Readily available on any linux distro one may be using.
- [x] A code editor of your choice. I personally use webstorm, but other good freebee ones are Atom and VS code.
- [x] Terminal. We will run most of our apps from the terminal. Good knowledge in using the terminal is a plus. To start the terminal CTRL + ALT + T for linux.
- [x] Dependencies required will be installed in the next stage.
```

### Installing

This is a step by step series of instruction that will tell you how to get a development env running and any other installations required.

- [ ] Cloning the repository from the link. Open terminal and run the following command.
```
git clone https://github.com/hillarydalie/instant.git
```
- [ ] When the cloning is complete, enter to the folder cloned by running this command.

```
cd instant/
```
- [ ] Create a virtual environment by running either of the two commands. <preffered_environment_name> replace this with your environment name.
```
*pip install virtualenv*, when complete then run *virtualenv <preffered_environment_name>* or *python3 -m venv virtual*
```
- [ ] Activate the virtual environment by running the following command.
```
source <preffered_environment_name>/bin/activate
```
- [ ] We will then install all the dependencies used in the project simply by running the requirements.txt file as follows.
```
pip install -r requirements.txt
```
- [ ] The last thing is to test and make sure everything is running fine. We shall use this command.
```
python3.6 manage.py runserver
```
Now we are ready to work on the project on our local server.


## Running the tests

An important aspect in python is writing tests to ensure our tests fail then writing code to ensure the tests pass. This has already been done. In order for you to run the tests you shall run the following code.

``` python3.6 manage.py tests```

Ensure all the tests ran and pass. If you need to add any features in the models, write the test, run the test to see if it fails, then write the code to ensure the test now passes. This is a good practise.

## Bugs

No bugs have so far been reported as of 11th of October 2019. If you find any do not hesitate to contact me. 
[GitHub](http://hillarydalie.github.com), [Mail](hidalie@gmail.com)

## Built With

* [Django](https://www.djangoproject.com/) - This is a python framework used for most of this project.
* [HTML5](https://www.w3schools.com/html/html5_intro.asp) - Mark up language for web pages.
* [CSS](https://www.w3schools.com/css/default.asp) - Used to style HTML pages.
* [BOOTSTRAP](https://getbootstrap.com/) - Bootstrap is an open source toolkit for developing with HTML, CSS, and JS.
* [JS](https://www.javascript.com/) - Interpreted scripting language for additional functionality HTML and CSS.

## Contributors

This is my sole work. No contirbutors in this project. If you have forked and used this repository, kindly add my profile link in your list of contributors.

## Authors

* **Hillary Dalie**


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* Hillary Dalie.
* Moringa School.
                                              Copyright Reserved  (c) 2019

