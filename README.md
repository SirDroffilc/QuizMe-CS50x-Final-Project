# QuizMe

#### Video Demo: https://www.youtube.com/watch?v=-Tn7PyloprY

#### Description:

**QuizMe** is a full-stack web application that allows users to create and share custom quizzes. Users can take quizzes created by others, view their results, and engage with the community through a feed where they can post updates. The app includes user authentication for secure access to personalized quiz experiences and content.

## Key Features

### 1. User Authentication

- Users can sign up for a new account.
- Users can log in an existing account.
- Usernames have a fixed number of minimum and maximum characters. Usernames should be unique to every user. Sign up will be rejected if the username is already taken
- Passwords have a fixed number of minimum and maximum characters. Passwords are securely hashed before being stored in the database to ensure privacy and security. This is implemented through generate_password_hash function from werkzeug.security
- User Authentication routes and related code can be found at ./web_app/blueprints/auth/routes.py

### 2. Multiple-Choice Quizzes

- Users can create, share, and answer custom multiple-choice quizzes.
- Users can modify (add questions, add title, change instructions) their quizzes even long after creating it.
- Users can answer their own quizzes, as well as other quizzes published by other users.
- Results are displayed immediately after completing a quiz.
- Quizzes routes and related code can be found at ./web_app/blueprints/quiz/routes.py

### 3. Community Feed

- Users can interact with other members of the community through a feed where they can post updates and share their thoughts.
- Users can only post a text-based post. The feed does not support images.
- All posts are public, which means every signed-up users can see all the posts in the feed.
- Date and time information are also included in the post.
- Community feed routes and related code can be found at ./web_app/blueprints/feed/routes.py

### 4. Profile Management

- Users can easily update their personal information, such as username and password.
- Same as the requirements when signing up, new usernames should still be unique and follow the number of minimum and maximum characters. This goes for the passwords as well.
- Option to delete their own account is available for those who choose to discontinue using the platform.
- Deleting the account means that all quizzes, questions, and posts created by the user will also be deleted from the database.
- For confirmation, the current password should be entered as a security measure when changing the username or password, as well as when deleting the account.
- Profile Management routes and related code can be found at ./web_app/blueprints/profile/routes.py

## Technologies Used

- **Backend**: Python with Flask
- **Frontend**: HTML, CSS, and JS with Bootstrap
- **Database**: SQLite with Flask-SQLAlchemy

## Installation Instructions

#### 1. Clone the repository

- > git clone https://github.com/SirDroffilc/QuizMe-CS50x-Final-Project

#### 2. Install dependencies

- > pip install -r requirements.txt

#### 3. Run

- Run 'run.py' and open the address or link on a browser.

## Usage

#### 1. Sign-Up and Log-In

- Look at the Sign Up or Log In Tabs on the navigation bar at the top.
- Create a new account or log in an existing account
- There is a set minimum and maximum characters for the username and password.
- Usernames cannot be the same as other users.
- Passwords are securely encrypted using the generate_password_hash function from werkzeug.security

#### 2. Feed

- Click the Feed Tab in the navigation bar.
- Share your thoughts by posting in the feed. These posts will contain the content, your username, as well as the date and time of posting.
-
- Scroll through all the posts in the feed.

#### 3. Quiz

- Click at the Quiz Tab. You will see Your Quizzes, Create a Quiz, and Answer Quizzes
- 'Your Quizzes' displays all your created quizzes. Select a quiz to modify it (change title, update instructions, add question, or delete quiz).
- 'Create a Quiz' prompts you for the title and instructions. You can then add questions by selecting this quiz at the 'Your Quizzes' Tab.
- 'Answer Quzzes' displays all the created quizzes by all users. Click on the 'Answer Quiz' to take the quiz.

#### 4. Profile

- Displays your profile information and all the posts you have created.
- You can choose to change your username or password, as well as to delete your account (deleting an account also deletes all the posts and quizzes of that account).

#### 5. Log Out

- Click the Log Out Tab at the navigation bar.
- This will log out your account and take you back to Home.
