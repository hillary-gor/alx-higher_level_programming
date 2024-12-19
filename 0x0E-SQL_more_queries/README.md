# 0x0E. SQL - More queries
![bc2575fee3303b731031](https://github.com/Zed-bard/alx-higher_level_programming/assets/132649828/e139af12-4e6e-4c80-9e5f-4951aefb9d1f)
The project involves setting up and working with MySQL 8.0 on Ubuntu 20.04 LTS. It includes creating SQL scripts adhering to specific requirements such as commenting syntax, starting files with task descriptions, and using uppercase SQL keywords. The README.md file provides comprehensive instructions for installation, connection to the MySQL server, and importing SQL dumps. Additionally, it includes an example SQL script for reference. This project aims to facilitate database management and query execution within a specified environment.


## Requirements

### General
- Allowed editors: vi, vim, emacs
- All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start with a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)

### README.md
- A README.md file, at the root of the folder of the project, is mandatory

## Setup Instructions

### Install MySQL 8.0 on Ubuntu 20.04 LTS
```bash
$ sudo apt update
$ sudo apt install mysql-server
$ mysql --version
```

### Connect to your MySQL server:
$ sudo mysql

### Use "container-on-demand" to run MySQL
- In the container, credentials are root/root
- Ask for container Ubuntu 20.04
- Connect via SSH or connect via the Web terminal
- In the container, start MySQL before playing with it:

$ service mysql start

### How to import a SQL dump
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows

