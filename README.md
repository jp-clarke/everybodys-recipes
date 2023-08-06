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

### Feature Testing

### Validation Testing

#### HTML

#### CSS

#### Python

#### Javascript

### Bugs

## Deployment

## Credits

## Acknowledgements