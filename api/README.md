# API Status

## Description

* This Directory contains API files and documenation

---

### [3. Improve storage DB](./../models/engine/db_storage.py)
### [Improve storage File](./../models/engine/file_storage.py)
* Update to DBStorage and FileStorage modules, adding two new methods in order
to handle the API Rest HTTP verbs (GET to retrieve one object and COUNT to
return the number of objects in storage).

### [4. Status of your API](./v1/views/app.py)
### [Index of API](./v1/views/index.py)
* Flask App that integrates with AirBnB static HTML Template
* Flask index file that returns the json status response
