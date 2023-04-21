from flask import Flask, request, jsonify
import requests
import mysql.connector
import os
from datetime import datetime
from dbquerys import sql_querys


# Function that add city data into DB
def add_city_DB(city, latitude, longitude):
    try:
        # Get the connection parameters to the DB
        db_host = os.environ.get('DB_HOST')
        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')
        db_name = os.environ.get('DB_NAME')
        result = find_city(city)
        if result is None:
            # Insert the city in the database
            cnx = mysql.connector.connect(user=db_user, password=db_password, host=db_host, database=db_name)
            cursor = cnx.cursor()
            values = (city, latitude, longitude)
            cursor.execute(str(sql_querys['insert_city']), values)
            cnx.commit()
            cursor.close()
            cnx.close()
            message = f"City {city} added successfully"
        else:
            message = f"City {city} already exists"  
        return message
    except Exception as ex:
        raise ex 

# Function that add city data into DB
def find_city(city):
    try:
        # Get the connection parameters to the DB
        db_host = os.environ.get('DB_HOST')
        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')
        db_name = os.environ.get('DB_NAME')
        # Insert the city in the database
        cnx = mysql.connector.connect(user=db_user, password=db_password, host=db_host, database=db_name)
        cursor = cnx.cursor()
        values = (city,)
        cursor.execute(str(sql_querys['select_city']), values)
        result = cursor.fetchone()
        cursor.close()
        cnx.close()
        return result
    except Exception as ex:
        raise ex 
# Function that find for an earthquake in the DB
def find_earthquakes_DB(city,start_date,end_date):
    try:
        # Get the connection parameters to the DB
        db_host = os.environ.get('DB_HOST')
        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')
        db_name = os.environ.get('DB_NAME')
        
        cnx = mysql.connector.connect(user=db_user, password=db_password, host=db_host, database=db_name)
        cursor = cnx.cursor()
        values = (city, start_date, end_date)
        cursor.execute(str(sql_querys['select_earthquakes_event']), values)
        result = cursor.fetchone()
        cursor.close()
        cnx.close()
        return result
    except Exception as ex:
        raise ex 

# Function that find for an earthquake in the API of earthquake.usgs.gov and saves the result in the DB
def get_earthquakes_insert_DB(city,start_date,end_date,latitude,longitude):
    try:
        # Get the connection parameters to the DB
        db_host = os.environ.get('DB_HOST')
        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')
        db_name = os.environ.get('DB_NAME')
        # Build the USGS Earthquake API URL
        url = f'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={start_date}&endtime={end_date}&minmagnitude=5.0&latitude={latitude}&longitude={longitude}&maxradiuskm=5000'
        print("url: " + str(url))
        # Get the data from the API
        response = requests.get(url)
        data = response.json()

        # Get the nearest earthquake
        try:
            earthquake = data['features'][0]
        except IndexError:
            return jsonify({'message': 'No results found'}), 404

        # Convert time to a readable date
        time = datetime.fromtimestamp(earthquake['properties']['time'] / 1000)
        formatted_time = time.strftime("%B %d %Y")
        formatted_time_DB = time.strftime('%Y-%m-%d %H:%M:%S')
        # Save the results in the database
        cnx = mysql.connector.connect(user=db_user, password=db_password, host=db_host, database=db_name)
        cursor = cnx.cursor()
        values = (city, start_date, end_date, earthquake['properties']['mag'], earthquake['properties']['place'], formatted_time_DB)
        cursor.execute(str(sql_querys['insert_earthquakes_event']), values)
        cnx.commit()
        cursor.close()
        cnx.close()
        return f"Result for {city} between {start_date} and {end_date}: The closest earthquake was a M {earthquake['properties']['mag']} - {earthquake['properties']['place']} on {formatted_time}"
    except Exception as ex:
        raise ex 