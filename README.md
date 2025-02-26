## Authentication feature
1. Listen on localhost:5000   
2. Authentication form is rendered at http://localhost:5000/   
3. User is redirected to the profile page if successfully authenticated  
4. Profile page is shown for the authenticated user only at http://localhost:5000/profile 
5. User name and password are stored in Redis

## How to run the program:
1. Execute `pip install -r requirements.txt`
2. Start a redis via docker: `docker run -p 6379:6379 -it redis/redis-stack:latest`
2. Execute `python app.py`
3. Open http://localhost:5000
