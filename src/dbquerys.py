sql_querys = {
    # insert_city query
    'insert_city' : """INSERT INTO cities (city, latitude, longitude) VALUES (%s, %s, %s)""",
    # select_city query
    'select_city' : """SELECT latitude, longitude FROM cities WHERE city = %s""",
    # select_earthquakes_event query
    'select_earthquakes_event' : """SELECT magnitude, location, time FROM earthquakes WHERE city = %s and start_date = %s and end_date = %s""",
    # insert_earthquakes_event query
    'insert_earthquakes_event' : """INSERT INTO earthquakes (city, start_date, end_date, magnitude, location, time) VALUES (%s, %s, %s, %s, %s, %s)"""
}