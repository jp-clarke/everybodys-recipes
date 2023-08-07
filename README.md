# Everybody's Recipes

## User Experience

### User Stories

| Epic | User Story | Description |
| --- | --- | --- |
| Site Navigation | Site pagination | As a Site User I can view a paginated list of posts so that I can select a recipe to view |
| | View Recipes | As a Site User I can click on a post so that I can open a recipe page |
| | Filter Recipes | As a Site User I can filter posts into categories so that I can easily find the recipe I want |
| Authenticated User | User Registration | As a Site User I can register so that I can add comments, likes and rate or favourite recipes |
| | Commenting | As a Site User I can comment on a recipe so that I can interact with other users |
| | Managing comments | As a Site User I can edit and delete my comments so that I can manage my contributions and interactions with other users |
| | Rating recipes | As a Site User I can rate a recipe so that I can contribute to rating recipes on the site |
| | Favourites | As a Site User I can select favourites so that I can easily view a list of my favourite recipes |
| | Create recipes | As a Site User I can create recipes so that I can share them with other users |
| | View star rating | As a Site User I can view the star rating so that I can see which recipes are the most popular |
| Site Administration | Manage content | As a Site Admin I can create, read, update and delete recipes so that I can manage my site content |
| | Control comments | As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments | 
| | Create draft recipes | As a Site Admin I can create draft recipes so that I can finish writing the content later |
| | Publish recipes | As a Site Admin I can view user submitted recipes so that I can approve and publish them to the site |

## Design

### Wireframe

### Database Model

| Model | Key | Name | Type | Notes |
| --- | --- | --- | --- | --- |
| Recipe Model | | Title (Unique) | Char | Max Length = 200 |
| | | Slug (Unique) | SlugField | Max Length = 200 |
| | ForeignKey | Author | User Model | |
| | | Date Created | DateTime | |
| | | Recipe Photo | CloudinaryField | |
| | | Description | TextField | |
| | | Ingredients | TextField | |
| | | Instructions | TextField | |
| | Many to Many | Favourited | User model | |
| | | Status | IntegerField | 0 = Draft, 1 = Published |


### Styling

## Features

### User Registration

### CRUD Functionality

### User Notifications

### Features to be Implemented

## Testing

### Manual Testing

| User Story | Expectation | Outcome | Result |
| --- | --- | --- | --- |
| Site pagination | User can see a paginated list of recipes and can browse by scrolling and clicking the next/previous buttons at the bottom of the page | The recipe cards are visible on the front page. There are 6 per page and more pages can be accessed using the next/previous buttons at the bottom of each page | Pass |
| View recipes | User can open a recipe page from the paginated list of recipes | When a recipe is clicked the user is taken to the corresponding recipe page | Pass |
| User registration | User can sign in or register to gain access to creating, favouriting and commenting on recipes | When a user is not logged in, the navbar shows both a Sign In and Register button, which takes the user to the corresponding page where they can sign in or create an account. They are then returned to the home page and notified of a successful sign in or registration | Pass |
| Commenting | When signed in, the user can comment on recipes | If signed in, a text field is visible at the bottom of the recipe page where the user can leave a comment | Pass |
| Managing comments | User can edit and delete their own comments | When signed in, both an edit comment and delete comment button appear directly below any of the user's own comments. These take the user to the corresponding page where they can confirm editing or deletion of the comment | Pass |
| Favourites | User can access and view a list of recipes they have favourited | When the user is signed in, a favourites button appears on the navbar, which can be used to access a paginated list of recipes that they have favourited | Pass |
| Create recipes | User can create their own recipe and add it to the site to share with others | When signed in, the user can access the page to create recipes via the navbar. Here, the user can fill in fields for title, description, ingredients, instructions and upload an image. On saving, the new recipe is sent to the site administrator to be published to the site | Pass |
| Manage content | Site admin can create, read, update and delete recipes and manage site content | When signed in as an administrator, the admin page can be accessed to manage recipe content, ie. create, edit, delete and publish recipes to the site | Pass |
| Control comments | Site admin can approve or disapprove new and edited comments to filter out objectionable comments and manage commenting on recipe pages | When signed in as an administrator, the admin page can be accessed to manage all comments and review, set to approved, or delete comments as required  | Pass |
| Create draft recipes | Site admin can create draft recipes to be saved and completed at a later date | When signed in as an administrator, the admin page can be accessed to manage all recipes and edit fields, save for later and set to draft or published | Pass |

### Validation Testing

#### HTML

#### CSS

#### Python

#### Javascript

### Bugs

## Deployment

This project was developed in GitHub and Gitpod from Code Institute's [gitpod template](https://github.com/Code-Institute-Org/gitpod-full-template), and has been deployed to Heroku. The process below requires an ElephantSQL database and Cloudinary storage.

The deployment process closely follows that of Code Institute's **'I Think Therefore I Blog'** walkthrough project and [Cheat Sheet](https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit#heading=h.5s9novsydyp1), and is as follows:

Gitpod Project
- Create a new workspace using the aforementioned [gitpod template](https://github.com/Code-Institute-Org/gitpod-full-template)
- Install Django: `pip3 install 'django<4' gunicorn`
- Install supporting libraries: `pip3 install dj_database_url==0.5.0 psycopg2`
- Install Cloudinary libraries: `pip3 install dj3-cloudinary-storage`
- Create requirements.txt file: `pip3 freeze --local > requirements.txt`
- Create project: `django-admin startproject PROJ_NAME .`
- Create app: `python3 manage.py startapp APP_NAME`
- In **settings.py**, add the app to **installed apps** and save file:<br>
`INSTALLED_APPS = [`<br>
&nbsp; &nbsp; &nbsp; &nbsp;`…`<br>
&nbsp; &nbsp; &nbsp; &nbsp;`'APP_NAME',`<br>
`]`
- Migrate changes: `python3 manage.py migrate`
- Run server to test: `python3 manage.py runserver`
- An error will be returned showing a disallowed hostname. Copy the hostname and add to **allowed hosts** in the **settings.py** file:<br>
`ALLOWED HOSTS = ['Add hostname here']`

ElephantSQL Database
- Login to ElephantSQL to access your dashboard
- Click 'Create New Instance'
- Set up a plan by selecting **Tiny Turtle (Free)** and entering a **Name** (typically the name of the project). Tags can be left blank
- Click 'Select Region' and select a data centre near you
- Click 'Review', confirm details are correct, then click 'Create Instance'
- From the ElephantSQL dashboard, click on the newly created database name
- Copy the database URL by clicking the adjacent copy icon

Create Heroku App
- Login to Heroku
- From the dashboard, create a new app
- Give the app a unique name and choose your region (United States or Europe)
- Click create app
- Go to the Settings tab
- Click Reveal Config Vars
- Add Config Var:<br>
KEY: DATABASE_URL | PORT: The database url copied from ElephantSQL (starting with postgres://)

Attach Database:
- Return to Gitpod file explorer and create a new **env.py** file in the top level directory
- In **env.py**, import os library: `import os`
- Set environment variables: `os.environ["DATABASE_URL"] = "ElephantSQL database URL"`
- Add secret key: `os.environ["SECRET_KEY"] = "User defined or generated secret key"`
- Return to Heroku App and add secret key to Config Vars:<br>
KEY: SECRET_KEY | PORT: "User defined or generated secret key"<br>

In **settings.py**:
- Reference env.py below `from pathlib import Path`:<br>
`import os`<br>
`import dj_database_url`<br>
`if os.path.isfile('env.py'):`<br>
 &nbsp; &nbsp; &nbsp; &nbsp;`import env`
- Replace SECRET_KEY with that matching the Heroku App:<br>
`SECRET_KEY = os.environ.get('SECRET_KEY')`
- Comment out the DATABASES section and add new database:<br>
`DATABASES = {`<br>
&nbsp; &nbsp; &nbsp; &nbsp;`'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))`<br>
`}`
- Save all files and make migrations from the terminal: `python3 manage.py migrate`

Cloudinary
- Login to Cloudinary
- From the dashboard, copy the CLOUDINARY_URL (API Environment Variable) using the 'Copy to clipboard' link
- Add the copied link to **env.py**: `os.environ["CLOUDINARY_URL"] = "cloudinary://***"`

In Heroku:
- Add Config Vars:<br>
KEY: CLOUDINARY_URL | PORT: "cloudinary://***"<br>
KEY: DISABLE_COLLECTSTATIC | PORT: 1 **(remove before deployment)**<br> 
KEY: PORT | PORT: 8000<br>

In **settings.py**:
- Add Cloudinary Libraries to installed apps section in the following order:<br>
`INSTALLED_APPS = [`<br>
&nbsp; &nbsp; &nbsp; &nbsp;`…`<br>
&nbsp; &nbsp; &nbsp; &nbsp;`'cloudinary_storage',`<br>
&nbsp; &nbsp; &nbsp; &nbsp;`'django.contrib.staticfiles',`<br>
&nbsp; &nbsp; &nbsp; &nbsp;`'cloudinary',`<br>
&nbsp; &nbsp; &nbsp; &nbsp;`…`<br>
`]`
- Tell Django to use Cloudinary to store media and static files (below `STATIC_URL = '/static/'`):<br>
`STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'`<br>
`STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]`<br>
`STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')`<br>
<br>
`MEDIA_URL = '/media/'`<br>
`DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'`<br>
- Link file to templates directory (below `BASE_DIR = Path(__file__).resolve().parent.parent`):<br>
`TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')`<br>
- Change the templates directory to TEMPLATES_DIR:<br>
`TEMPLATES = [`<br>
&nbsp; &nbsp; &nbsp; &nbsp;`{`<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;`…,`<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;`'DIRS': [TEMPLATES_DIR],`<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;`…,`<br>
&nbsp; &nbsp; &nbsp; &nbsp;`},`<br>
`]`
- Add Heroku Hostname to ALLOWED_HOSTS. This can be found in the Heroku App Settings, under Domains:<br>
`ALLOWED HOSTS = [`<br>
&nbsp; &nbsp; &nbsp; &nbsp;`'Heroku Hostname',`<br>
&nbsp; &nbsp; &nbsp; &nbsp;`'Hostname',`<br>
`]`<br>
- Add media, static and templates folders on top level directory
- Create a **Procfile** in the top level directory
- Add code to **Procfile**: `web: gunicorn PROJ_NAME.wsgi`
- Add, Commit and Push

In Heroku
- Go to the Deploy tab of the Heroku App
- Connect GitHub account to Heroku
- Search for the relevant repository to connect to
- Click on Deploy branch

## Credits

## Acknowledgements