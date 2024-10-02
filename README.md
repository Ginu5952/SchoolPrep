# SchoolPrep Genie

<h1 align="center">SchoolPrepGenie</h1>
<h2 align="center">"Pack Smart, Stay Informed - The School App Every Parent Needs"</h2>
<p align="center">

# Mission Statement

" Connect teachers, parents and students and maintain their data that will make this connection reliable, effective and smooth "

# Mission Objectives

- List students-timetable (perticular to class)
- Lunch Menu
- Announcement (Upcoming Events)
- Attendance Sheet
- Teachers-Feedback / write to Teacher
- Course Calender 
- Leave Note (Leave Application)


# Instructions to run pogram

- Open a terminal
- Run following commands

Create DataBase

```psql
psql -U postgres
CREATE DATABASE schoolprep_django;
\q
```
### Please note that the commands for setting up the development environment, creating migrations, and applying them to the database are written in the Makefile for convenience.

The command is used to install the Python packages listed in a specific requirements file.

```psql
make dev-install
```


The command starts the Django development server using the settings defined in the config/settings/dev.py file. After starting the server, Django typically outputs a message indicating the URL where you can access your application.

```psql
make start
```

Once the server starts, you should see output similar to:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
September 16, 2024 - 03:34:56
Django version X.Y.Z, using settings 'config.settings.dev'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

#### Additional Notes
- To stop the development server, press CONTROL-C in the terminal where it is running.



