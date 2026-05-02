# Sports Event Calendar

## Project overview
This application provides a calendar of sports events along with related information. It is built as a web application with two main pages: Home and Calendar.

Home Page
- Displays live and upcoming events.

Calendar Page
- Shows all sports events.
- Allows filtering events by status: Scheduled, Live, or Finished.
- Allows filtering events by sport.
- Supports adding new events directly through the interface.

### Technical Stack:
Backend: Python with Flask framework and SQLAlchemy<br>
Frontend: HTML, CSS, JavaScript<br>
Database: MySQL<br>

### How to set up and run the app:
1. Install dependencies: `pip install -r requirements.txt`
2. Create a `.env` file in the project root and specify these variables:
```
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DATABASE="Sports_Events"
```
3. Run the application (from the project folder): `python3 src/main.py`

### Assumptions and decisions:
- MySQL is used to store structured data.
- The database consists of 6 tables, each responsible for a different part of event data.
- Tables are connected with foreign keys to prevent data duplication.
- A `Database` class is used to reuse common database operations.
- JavaScript is used to filter data dynamically on the frontend.
- Flask is used handle API requests and send data to the frontend.
