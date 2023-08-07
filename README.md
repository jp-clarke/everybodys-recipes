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

## Credits

## Acknowledgements