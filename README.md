# BLHA application

## Overview

Aim of the project is to implement a simple user login system with a small set of user management features. The implementation approach should consist of a database backend system, which performs the database information exchange using object-relational mapping (ORM). For passing information between back- and frontend a Rest-API have to be realized.  

![Current project infrastructure](blha_project.png)

## Getting started

### DB Scheme

To abstract a very simple user list, the following database scheme is used:

```
DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL,
  password TEXT NOT NULL
);

```

For preparing the SQLITE database run the following snippet:

``` 
sqlite3 database.db < db/scheme.sql
```

An alternative way for creating and filling the database with pre-defined user entries is implemented using [Peewee ORM](https://docs.peewee-orm.com/en/latest/).
```
python3 db/dbmodel.py
```

### Backend

The backend features a Rest(ful)-API to access the database indirectly. It establishes the database connection using ORM and allows requesting an list of created users and the creation of new ones. The user list represented as JSON string.
