# CEN3031-Project
Group Project for Intro to Software Engineering.

Goal: Creating a website for accessing many different charities/non-profit foundations.

Running the website:
in command prompt/ terminal(bash):
cd [location of files]
python3 -m http.server

then run server.py in python
if you get an error that server is occupied you can either change ther port to 5000 and run then stop running and run again with the port as 5001
or you can kill the program with bash command: kill [id], the id can be founf by using this bash command: lsof -i :5001

Now run index.html by typing http://localhost:8000/index.html/

For testing reset browsing history to signout as a button for that has yet to be made
