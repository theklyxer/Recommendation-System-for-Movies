# Movie Recommendation System

## Project Overview
This project develops a **Content-Based Movie Recommendation System** with a user-friendly web interface. Its primary goal is to help users discover new movies by recommending titles that are similar in content to their preferences. The system achieves this by analyzing movie attributes such as genres, keywords, cast, and crew using various machine learning models. It aims to provide personalized recommendations without relying on collaborative filtering (i.e., user-to-user or item-to-item interactions).

## Features
*   **User Authentication**: Secure sign-up and sign-in functionalities allow users to create personal accounts and log in to access the system.
*   **Interactive Movie Search**: Users can search for movies through a dedicated interface, making it easy to find specific titles.
*   **Personalized Content-Based Recommendations**: Once a user searches for or selects a movie, the system intelligently analyzes its characteristics (genres, keywords, cast, director) to suggest other movies with similar attributes, providing a tailored discovery experience.
*   **Efficient Data Import Management**: A custom Django management command simplifies the process of populating the database with movie metadata from large CSV files, ensuring the recommendation engine has the necessary data efficiently.

## Project Structure
The project is meticulously organized into the following key directories to separate concerns and enhance maintainability:

*   \`Code_For_Content_Based_Filtering/\`: This directory is dedicated to the **development and experimentation of the core content-based recommendation algorithms**. It contains Jupyter notebooks and raw data files, allowing for iterative development and analysis of different machine learning models before integrating them into the web application.
*   \`Movie_Recommendation/\`: This is the **main Django project configuration directory**. It holds global settings, URL routing for the entire application, and server configuration files.
*   \`website_app/\`: This is a **specific Django application** within the larger project. It encapsulates the front-facing web interface, defines database models for movies and users, handles view logic for web requests, and manages its own URL routing and static assets.

## Content-Based Filtering Models
The intelligence of this recommendation system stems from various content-based filtering models, primarily developed and tested in the Jupyter notebooks, and then integrated into the \`website_app\` for live recommendations.

*   **Jupyter Notebooks**: These notebooks demonstrate the development and application of different text processing and similarity algorithms:
    *   \`BAGOFWORDS.ipynb\`: This notebook likely explores and implements the **Bag of Words model**. This model is a foundational technique in natural language processing (NLP) that converts text data (movie overviews, keywords) into numerical feature vectors by counting word occurrences, enabling basic text similarity calculations.
    *   \`BM.ipynb\`: This notebook focuses on the **BM25 (Okapi BM25) ranking function**. BM25 is a probabilistic information retrieval algorithm used to estimate the relevance of documents to a given search query. In this project, it's used to rank movies based on their textual similarity to a user's searched movie, providing more nuanced and relevant results than simple Bag of Words.
    *   \`TF-IDF.ipynb\`: This notebook implements the **TF-IDF (Term Frequency-Inverse Document Frequency) model**. TF-IDF is a statistical measure that evaluates how relevant a word is to a document in a collection of documents. It helps to give higher importance to terms that are unique to a particular movie's description while downplaying common words, thus improving the accuracy of content-based recommendations.

*   **CSV Files**: These datasets are crucial for training and operating the recommendation models:
    *   \`credits.csv\`: Contains detailed **cast and crew information** for movies, including director, actors, and their roles. This data is vital for identifying movies with similar creative teams or lead actors.
    *   \`impwords.csv\`: Contains a collection of **important keywords and tags** associated with movies. These keywords enrich the content profile of each movie, allowing for more precise similarity matching.
    *   \`links_small.csv\` and \`links.csv\`: These files provide **mapping between different movie identifiers** (e.g., MovieLens IDs, IMDb IDs, TMDB IDs). While `links_small.csv` is a subset, `links.csv` provides a more comprehensive mapping, essential for integrating various datasets.
    *   \`movies_metadata.csv\`: This is the **primary dataset containing core movie information**. It includes attributes such as title, release date, genres, plot overview, popularity, and voting statistics. This file forms the backbone of the movie database and content-based analysis.

## Technologies Used
The project is built upon a robust stack of technologies, each serving a specific purpose:

*   **Backend**: \`Django\` (Python Web Framework) - Used for rapid web development, handling URL routing, database interactions (ORM), user authentication, and serving dynamic content. Version `5.0.3` is utilized for modern features and stability.
*   **Data Analysis & Manipulation**: \`pandas\` (`2.2.3`), \`numpy\` (`1.26.4`) - Essential libraries for efficient data loading, cleaning, transformation, and analysis of large datasets (CSV files) that feed into the recommendation models.
*   **Search & Ranking**: \`rank_bm25\` (`0.2.2`) - A specialized library implementing the BM25 algorithm, crucial for calculating the relevance of movie text descriptions to search queries or other movie descriptions.
*   **Character Encoding Detection**: \`chardet\` (`5.2.0`) - Used for robust detection of character encodings in textual data, ensuring proper processing of diverse movie metadata.
*   **Database**: \`SQLite\` (default for development) - A lightweight, file-based database system used during development for ease of setup and local data storage.
*   **Frontend**: \`HTML\`, \`CSS\`, \`JavaScript\` - Standard web technologies for building the user interface, styling the application, and adding interactive elements.

## Setup Instructions

### Prerequisites
Before you can set up and run this project, ensure your system meets the following requirements:
*   **Python 3.x**: The project is developed with Python 3. You can download it from [python.org](https://www.python.org/downloads/).
*   **pip**: The Python package installer, usually comes bundled with Python.

### Installation Steps

1.  **Clone the Repository**:
    First, clone the project repository to your local machine.
    ```bash
    git clone <repository_url>
    cd Movie-Recommendation-System/gitpush # Navigate into the gitpush directory
    ```
    *Replace `<repository_url>` with the actual URL of your Git repository.*
    *Ensure you are on the `main` branch or the branch containing the latest stable code.*

2.  **Create and Activate a Virtual Environment (Highly Recommended)**:
    Using a virtual environment is crucial for isolating project dependencies from your global Python environment, preventing conflicts with other projects.
    ```bash
    python -m venv venv
    # On Windows, activate with:
    .\\venv\\Scripts\\activate
    # On macOS/Linux, activate with:
    source venv/bin/activate
    ```
    *You should see `(venv)` prepended to your terminal prompt, indicating the virtual environment is active.*

3.  **Install Dependencies**:
    Once your virtual environment is active, install all required Python packages listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create Database Migrations (if models changed)**:
    If you have made any changes to the database models (`website_app/models.py`) or are setting up the project for the first time with a fresh database, you might need to create migration files. These files tell Django how to create or modify database tables to match your models.
    ```bash
    python manage.py makemigrations
    ```
    *Note: If you are cloning the repository for the first time, migration files are usually already provided (e.g., in `website_app/migrations/`), so you might not need to run `makemigrations` immediately unless you modify the models.*

5.  **Apply Database Migrations**:
    Django uses migrations to manage database schema changes. Apply the initial migrations to create the necessary tables in your SQLite database.
    ```bash
    python manage.py migrate
    ```

6.  **Import Movie Data**:
    This is a **critical step** for the recommendation system to function. The project includes a custom Django management command to import the movie metadata from your CSV files into the `MovieData` model in your database.
    ```bash
    python manage.py import_movie_data
    ```
    *   **Important**: Ensure that the CSV files (`credits.csv`, `impwords.csv`, `links_small.csv`, `links.csv`, `movies_metadata.csv`) are located in the `Code_For_Content_Based_Filtering/` directory. The `import_movie_data.py` script expects them to be accessible relative to its execution context. If you move these files, you might need to update the paths within `website_app/management/commands/import_movie_data.py`.
    *   This command might take some time to execute depending on the size of the CSV files.

7.  **Run the Django Development Server**:
    Finally, start the local Django development server to access the web application.
    ```bash
    python manage.py runserver
    ```
    The application will typically be accessible at `http://127.0.0.1:8000/` in your web browser. Watch your terminal for the exact URL.

## Usage
Once the development server is running and you have navigated to `http://127.0.0.1:8000/`:

1.  **Sign Up / Sign In**: If you are a new user, click on the "Sign Up" link to create an account. Existing users can "Sign In". This allows the system to potentially personalize experiences in the future or track user preferences.
2.  **Navigate to Search**: After logging in (or if browsing as a guest, depending on your application's setup), proceed to the movie search page.
3.  **Search for Movies**: Enter movie titles or keywords into the search bar. The system will use its underlying BM25 logic to find relevant movies.
4.  **Explore Recommendations**: Upon selecting a movie from the search results, the system will display a list of recommended movies based on content similarity (genres, keywords, cast, crew).

## Files Explained

### `manage.py`
A core Django command-line utility. It's used for various administrative tasks like running the development server (`runserver`), applying database migrations (`migrate`), and executing custom commands (`import_movie_data`).

### `Movie_Recommendation/` (Django Project Configuration)
This directory acts as the central configuration hub for your entire Django project.
*   \`settings.py\`: This is the **heart of your Django project's configuration**. It defines:
    *   `SECRET_KEY`: A unique key used for cryptographic signing.
    *   `DEBUG`: Boolean that turns debug mode on/off. Crucial for development but should be `False` in production.
    *   `ALLOWED_HOSTS`: A list of strings representing the host/domain names that this Django site can serve.
    *   `INSTALLED_APPS`: A list of Django apps that are active in this project (e.g., `django.contrib.admin`, `website_app`).
    *   `DATABASES`: Dictionary containing the settings for all databases used in the project, defaulting to SQLite for development.
    *   `STATIC_URL`: URL to use when referring to static files located in `STATIC_ROOT`.
    *   Other middleware, template configurations, and password validators.
*   \`urls.py\`: This is the **root URL configuration for the entire project**. It acts as a central dispatcher, including URL patterns from individual Django applications (like `website_app`) and directing requests to the appropriate views.
*   \`wsgi.py\` / \`asgi.py\`: These files serve as the **entry points for WSGI (Web Server Gateway Interface) and ASGI (Asynchronous Server Gateway Interface) compatible web servers**, respectively. They define how your Django application communicates with web servers in both synchronous and asynchronous modes.

### `website_app/` (Django Application)
This is the main Django application responsible for the user-facing features of the movie recommendation system.
*   \`models.py\`: This file defines the **database models** that structure your application's data. Key models include:
    *   `Member`: Likely stores general user information.
    *   `User`: Extends Django's default user model or provides custom user fields for authentication.
    *   `MovieData`: Stores comprehensive movie information imported from CSV files, including fields for title, genres, overview, keywords, cast, and crew, which are essential for content-based recommendations.
*   \`views.py\`: Contains the **logic for handling web requests and returning responses**. This is where the core functionality of your web application resides. It interacts with the models to retrieve and save data, renders HTML templates, and integrates the recommendation logic (using `rank_bm25`, `pandas`, `numpy`, etc.) to process user queries and generate movie recommendations. Key view functions might include `signup_view`, `signin_view`, `search_movie`, and `recommend_movie`.
*   \`urls.py\`: Defines the **URL patterns specific to the `website_app`**. These patterns map URLs (e.g., `/search/`, `/recommend/`) to corresponding view functions within `views.py`.
*   \`templates/\`: This directory holds all the **HTML templates** rendered by your Django views to generate dynamic web pages. Examples include:
    *   `index.html`: The main landing page.
    *   `search.html`: The page where users can input movie searches.
    *   `result.html`: Displays the movie search results and recommendations.
    *   `signin.html` / `signup.html`: Pages for user authentication.
*   \`static/\`: Contains **static files** directly served by the web server (e.g., CSS, JavaScript, images).
    *   `css/`: Contains stylesheets like `style.css` (general styling), `search.css` (for the search page), and `result.css` (for the results page).
    *   `js/`: Contains JavaScript files like `search.js` (for search functionality) and `result.js` (for interactive elements on the results page).
    *   `images/`: Stores all images used in the application, such as `logo.png`, `header-image.jpg`, and movie posters.
*   \`management/commands/\`: This directory holds **custom Django management commands**.
    *   \`import_movie_data.py\`: This is a crucial custom command. It automates the process of reading data from your `movies_metadata.csv` and `credits.csv` files and populating the `MovieData` model in your database. This command ensures that your recommendation engine has the necessary data to operate.
*   \`utils.py\`: Contains **utility functions** that are reusable across different parts of the `website_app`. This might include functions for data loading, text preprocessing for recommendation algorithms, or other helper functions used by `views.py` to keep the view logic clean and focused. 