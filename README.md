# What The F**d

What The Food is a web application that allows users to upload and share their favorite recipes with others. Users can create an account, log in, and start adding their recipes along with preparation steps and ingredients.

## Features

- User Authentication: Users can sign up and log in to the application using their email and password.
- Recipe Upload: Authenticated users can upload their recipes, including the name, preparation time, cooking time, ingredients, steps, optional link to the original recipe, and difficulty level.
- Categorization: Users can categorize their recipes using checkboxes for vegetarian, dairy-free, beef, pork, and chicken options.
- Recipe Details: Each recipe has a detail page that displays all the information added by the user.
- Media Upload: Users can upload images or files for their recipes.
- User Profile: Users can view and update their profile information, including name and profile picture.

## Technologies Used

- Django: Backend framework for building the web application.
- PostgreSQL: Database for storing recipe and user data.
- HTML, CSS, JavaScript: Frontend technologies for the user interface.
- Heroku: Platform for deploying and hosting the application.

## Local Development

1. Clone the repository: `git clone https://github.com/rushang-patel/what-the-food.git`
2. Create a virtual environment: `python3 -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Set up the database: `python manage.py migrate`
6. Run the development server: `python manage.py runserver`

#### The application should now be running at: 
`https://what-the-food-d4a1522bc189.herokuapp.com/`.

## Contributors

- Rushang Patel, `https://github.com/rushang-patel`
- Mabel Lam, `https://github.com/mabelam`

## LOGO

![What The Food Logo](https://github.com/rushang-patel/what-the-food/raw/main/main_app/static/readme_images/WTF_LOGO.png)


## Screenshots

![Recipe Image](https://github.com/rushang-patel/what-the-food/raw/main/main_app/static/readme_images/Recipes.png)
![Recipe Form](https://github.com/rushang-patel/what-the-food/raw/main/main_app/static/readme_images/Recipeform.png)

