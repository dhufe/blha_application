# BLHA application

## Overview

## Getting started

### DB Scheme

To abstract a very simple user list, the following database scheme is used:

```
DROP TABLE IF EXISTS USERS;

CREATE TABLE USERS ( 
  ID INTEGER PRIMARY KEY AUTOINCREMENT,
  USERNAME TEXT NOT NULL,
  PASSWORD TEXT NOT NULL
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


