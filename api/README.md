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
* Error ![404](https://img.shields.io/badge/-404-red) handler for the app file in the API project
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

### [8. City](./v1/views/cities.py)
* View that handles all default RestFul API actions for cities

### [9. Amenity](./v1/views/amenities.py)
* View that handles all default RestFul API actions for amenities

### [10. User](./v1/views/users.py)
* View that handles all default RestFul API actions for users

### [11. Place](./v1/views/places.py)
* View that handles all default RestFul API actions for places

### [12. Reviews](./v1/views/places_reviews.py)
* View that handles all default RestFul API actions for reviews
