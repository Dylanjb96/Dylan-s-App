# Dylan's App 
This project is a web-based Todo application that allows users to manage their tasks. Users can add, edit, delete, and mark tasks as complete and add, edit and delete thier profile. The application also includes a messaging feature where users can send and receive messages.

## Features
- User authentication and authorization
- Task management (CRUD operations)
- Messaging system
- Search functionality
- Responsive design
  
## Installation 
Instructions for installing and running the project.
- Python 3
- Django
- PostgreSQL
- Node.js
  Step 1: Create a virtual environment and activate it
  ```bash
  python -m venv myenv
  ```
  ```bash
  source myenv/bin/activate
  ```
  ```bash
  myenv\Scripts\activate
  ```
  Step 2: Install the required Python packages
  ```bash
  pip install -r requirements.txt
  ```
  Step 3: Set up the Database
  - Ensure PostgreSQL is running
  - Create a new database for the project.
  - Update the 'settings.py' file with your database credentials.
    ```bash
    python manage.py migrate
    ```
  Step 4: Create a superuser (you need this otherwise you wont be able to login when you run it)
  ```bash
  python manage.py createsuperuser
  ```
  Steps 5: Run the development server (backend)
  ```bash
  python manage.py runserver
  ```
  Step 7: Set up the frontend
  Navigate to the frontend directory and install dependencies:
  ```bash
  cd frontend
  npm install
  npm start
  ```
## Usage 
Examples and explanations of how to use the project.
Once everything is set up, navigate to http://127.0.0.1:8000/admin/ in your web browser to access the application. (When you run the frontend, it will automatically popup on your browser)

Login: Access the login page at http://127.0.0.1:8000/login.
Register: Register a new account at http://127.0.0.1:8000/register.
Todo Management: Manage your tasks from the dashboard.
Messaging: Send and receive messages via the messaging feature.

## Techbologies Used
- Backend: Django, Django REST Framework, PostgreSQL
- Frontend: React, Bootstrap
- Authentication: JWT

## Contributing 
Guidelines for contributing to the project. Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch ('git checkout -b feature/your-feature').
3. Make your changes.
4. Commit your changes ('git commit -m 'Add some feature'').
5. Push to the branch ('git push origin feature/your-feature').
6. Open a pull request.

## Conclusion
The main problem i have faced when doing this project, was the messaging section. I could not make the messaging part look normal or professional (See the screenshots). So i could not find the time and resources to solve the problem i have in this part of the project. Also the online status I had it's now gone and I did not pay attention to it while I was trying to solve the messaging issue. But nevertheless, I think what i have at the moment is good as it can get. Feel free to suggest a solution to solve this issue. 

##Screenshots
![Alt text] (C:\Users\Dylan B\Pictures\Screenshots\Screenshot(182)


- *** Link to Render.com ***
  https://dashboard.render.com/d/dpg-cr31d8g8fa8c73c3n380-a
- *** Link to GitHub Repo ***
  https://github.com/Dylanjb96/Dylan-s-App
 
