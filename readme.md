## Flask application to search for earthquakes closest to a city in a period of time
The app.py file contains the Flask application to look up earthquake information for a city and the function to add a city to the database.

To use this application, HTTP requests must be sent to the following routes:

```bash
/search: to search for information about earthquakes in a city.

/city: to add a city to the database.
```
In addition, the application connects to a MySQL database to store information on cities and earthquakes.

## Route /search
This route accepts GET requests and expects the following parameters in the query string:

```bash
city: The name of the city to search for.
start_date (optional): The start date to search for earthquakes (format YYYY-MM-DD).
end_date (optional): The end date to search for earthquakes (format YYYY-MM-DD).
```
The route returns information about the nearest earthquake in the city and within the specified date range. If an earthquake is found, the response will include the magnitude, location, and date of the earthquake. If no earthquake is found, the response will indicate that no information was found for the city. The response is returned in JSON format.

### call Example:
```bash
URL: http://localhost:5000/search?city=Tokyo&start_date=2004-04-02&end_date=2018-01-31
```

## Route /city
This route accepts POST requests and expects the following parameters in the request body:

```bash
city: The name of the city to add.
latitude: The latitude of the city.
longitude: The longitude of the city.
```
The route adds the city and its coordinates to the database. If the city is already in the database, the response will indicate that the city already exists. The response is returned in JSON format.

### call Example:
```bash
URL: http://localhost:5000/city
```
```bash
JSON: {"city": "Buenos Aires", "latitude": -34.603722, "longitude": -58.381592}
```

## File functions.py
This file contains the helper functions used by the Flask application to search for earthquake information in a city and add a city to the database.
```bash
add_city_DB(city, latitude, longitude): Adds a city and its coordinates to the database. If the city is already in the database, the function returns a message indicating that the city already exists.

find_city(city): Searches for a city in the database and returns its coordinates if found.

find_earthquakes_DB(city, start_date, end_date): Searches for earthquakes in a city and within the specified date range in the database and returns information about the nearest earthquake if found.

get_earthquakes_insert_DB(city, start_date, end_date, latitude, longitude): Searches for earthquakes in a city and within the specified date range in an external API and adds them to the database. The function returns information about the nearest earthquake if found.
```

## Setting up a project with Docker
This guide will show you how to set up the project with Docker. We'll be using Docker Compose to orchestrate two containers (Python app and Mysql db).

### Prerequisites
Make sure you have the following software installed:
```bash
Docker
Docker Compose
```
From the root directory of the project run the following scripts
    ```bash
    docker-compose up
    ```
you can now point to http://localhost:5000/ to use the different services of the application

## Unit Tests

Add a unit_test.py file to the project, which tests the earthquake search function, passing a call to the endpoint and the response that the API should receive.

### Parameters:

```bash
    url (str): The URL of the API endpoint to test.
    expected_result (str): The expected result of the API response.
```

### Returns:
```bash
    str: The actual result of the API response.
```

### Raises:
```bash
    AssertionError: If the API response does not match the expected result or if the API returns a non-200 status code.
```

You can iterate the call to this API over a list of calls and responses and thus automatically test the functionality of the api.

