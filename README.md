# Backend Coding Challenge

[![Build Status](https://github.com/Thermondo/backend-code-challenge/actions/workflows/main.yml/badge.svg?event=push)](https://github.com/Thermondo/backend-code-challenge/actions)

We appreciate you taking the time to participate and submit a coding challenge. In the next step we would like you to
create/extend a backend REST API for a simple note-taking app. Below you will find a list of tasks and limitations
required for completing the challenge.

### Application:

* Users can add, delete and modify their notes
* Users can see a list of all their notes
* Users can filter their notes via tags
* Users must be logged in, in order to view/add/delete/etc. their notes

### The notes are plain text and should contain:

* Title
* Body
* Tags

### Optional Features 🚀

* [ ] Search contents of notes with keywords
* [ ] Notes can be either public or private
    * Public notes can be viewed without authentication, however they cannot be modified
* [ ] User management API to create new users

### Limitations:

* use Python / Django
* test accordingly

### What if I don't finish?

Try to produce something that is at least minimally functional. Part of the exercise is to see what you prioritize first when you have a limited amount of time. For any unfinished tasks, please do add `TODO` comments to your code with a short explanation. You will be given an opportunity later to go into more detail and explain how you would go about finishing those tasks.

### How to setup

* Build the project using `make build`
* Run the app using `make start`
* Access application with [url](http://0.0.0.0:8000/)
* It will take you to login screen. Where you can use following credentials
    > username: jinojossy
    > password: thermondo
* To create notes, You have to create [tags](http://0.0.0.0:8000/notes/tags/)
* Now to create [notes](http://0.0.0.0:8000/notes/list/) with DRF UI
* You can now logout using [url](http://0.0.0.0:8000/logout)
* Even in logged out page you can access [notes](http://0.0.0.0:8000/notes/list/) but cannot modify

# TODO
* Add user to Note model, with private flag
* This will be useful for implementing private notes readable only to the user that created it.

