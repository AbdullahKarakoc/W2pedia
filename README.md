# Django Wikipedia Application

This Django application allows users to add, read, search, and edit articles. On this website, users can add, read, and edit new articles. They can also access the article they want from the search section. Additionally, there is a button in the application for accessing a random article, which redirects users to a random article page.

# Installation

1. Firstly, ensure that Python and Django are installed on your computer.
2. Clone or download this project.
3. Navigate to the project folder and create a virtual environment:
  -> - python -m venv myenv
4. Activate the virtual environment:

On Windows:
  -> - myenv\Scripts\activate

On Linux/Mac:
  -> - source myenv/bin/activate

5. Install the required dependencie:
  -> - pip install django
  -> - pip install markdown2

6. Run migrations to create the database:
  -> - python manage.py makemigrations
  -> - python manage.py migrate

7. Start the server:
  -> - python manage.py runserver

8. You can now start using the application by visiting http://localhost:8000 in your browser.

# Usage

* Adding an Article: You can add a new article by clicking on the "Add Article" link on the homepage. Fill in the necessary information in the form to save the article.
* Reading an Article: You can read the content of a specific article by clicking on it from the list displayed on the homepage.
* Editing an Article: You can edit an existing article by clicking the "Edit" button on the article content page. Make the necessary changes and save.
* Searching for an Article: You can search for articles by their titles using the search bar at the top of the homepage.
* Random Article: By clicking on the "Random Article" button on the homepage, you can access a random article.
  

# Contribution
If you have any feedback or suggestions regarding this project, feel free to contribute by opening an issue or sending a pull request. We welcome any contributions!
# License
This project is licensed under the MIT License. See the LICENSE file for more information.

