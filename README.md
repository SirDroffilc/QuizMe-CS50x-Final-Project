# QuizMe

**QuizMe** is a full-stack web application that allows users to create and share custom quizzes. Users can take quizzes created by others, view their results, and engage with the community through a feed where they can post updates. The app includes user authentication for secure access to personalized quiz experiences and content.

## Key Features

### 1. User Authentication
- Users can sign up and log in with unique usernames.
- Passwords are securely hashed before being stored in the database to ensure privacy and security.

### 2. Multiple-Choice Quizzes
- Users can create, share, and answer custom multiple-choice quizzes.
- Results are displayed immediately after completing a quiz.

### 3. Feed
- Users can interact with other members of the community through a feed where they can post updates and share their thoughts.

### 4. Edit Profile
- Users can easily update their personal information, such as username and password.
- Option to delete their own account is available for those who choose to discontinue using the platform.


## Technologies Used

- **Backend**: Python with Flask
- **Frontend**: HTML, CSS, and JS with Bootstrap
- **Database**: SQLite

## Installation Instructions
#### 1. Clone the repository
- 'git clone https://github.com/SirDroffilc/QuizMe-CS50x-Final-Project'

#### 2. Install dependencies
- 'pip install -r requirements.txt'

#### 3. Run
- Run 'run.py' and open the address or link on a browser.

## Usage
#### 1. Sign-Up and Log-In
- Look at the Sign Up or Log In Tabs on the navigation bar at the top.
- Create a new account or log in an existing account

#### 2. Feed
- Click the Feed Tab in the navigation bar.
- Share your thoughts by posting in the feed. These posts will contain the content, your username, as well as the date and time of posting.
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
- Logs out your account and takes you back to Home.
