# Asset Man

## Overview
Asset Man is a simple asset/inventory management software written in Python/Django.  It was designed with fast entry, editing, and deletion in mind, using a very simple and easy-to-understand UI.  It was written initially for an organization I was a part of, so the default models in the code reflect their needs.  

## Features
* Four categories of items, each with unique fields
* User authentication
* Simple default set of database models that can be modified and expanded
* User permissions that allow admins to tailor who can add/edit/delete/view objects
* Userstamps and timestamps on object create/edit

### Other notes
* In its current state, the system you deploy Asse Man on must have an environment variable named 'DJANGO_SECRET_KEY' with a 50-char secret key associated with it.  There is a hard-coded default, but this would leave the app vulnerable.  
* A demo environment can be found [here](https://assetman-test.herokuapp.com/)
  * U: testuser
  * P: password