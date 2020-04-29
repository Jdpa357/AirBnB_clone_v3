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
* Flask App that integrates with AirBnB static HTML Template

### [5. Some stats?](./v1/views/index.py)
* Flask index file that returns the json status response

### [6. Not found](./v1/views/app.py)
* Error 404 handler for the app file in the API project
[![404](https://img.shields.io/badge/404-404-red)]
```@app.errorhandler(404)
def handle_404(exception):
    """
    Handler for 404 error (Not Found)
    """
    code = exception.__str__().split()[0]
    description = "Not found"
    message = {'error': description}
    return make_response(jsonify(message), code)
```
### [7. State](./v1/views/states.py)
* View that handles all default RestFul API actions for states
