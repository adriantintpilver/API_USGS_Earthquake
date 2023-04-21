from flask import Flask, request, jsonify
from functions import add_city_DB, find_city, find_earthquakes_DB, get_earthquakes_insert_DB

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    # Get request parameters
    city = request.args.get('city')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    print("argumentos: " + str(city) + " " + str(start_date) + " " + str(end_date))
    # Get the coordinates of the city
    result = find_city(city)
    if result is None:
        return jsonify({'message': 'City not found'}), 404
    latitude, longitude = result
    # Control of duplicates, we look in the DB for the search to see if it is already there, if it is, we show the saved result and if it is not, if the response is already in the DB, the API query is not made
    resultsearchcity = find_earthquakes_DB(city, start_date, end_date)
    if resultsearchcity is None:
        message = get_earthquakes_insert_DB(city,start_date,end_date,latitude,longitude)
    else:
        magnitude, location, time = resultsearchcity
        formatted_time = time.strftime("%B %d %Y")
        message = f"Result for {city} between {start_date} and {end_date}: The closest earthquake was a M {magnitude} - {location} on {formatted_time}"

    # return the results
    return jsonify({'message': message}), 200

@app.route('/city', methods=['POST'])
def add_city():
    # Get request parameters
    city = request.json.get('city')
    latitude = request.json.get('latitude')
    longitude = request.json.get('longitude')
    # Add the city to the database
    message = add_city_DB(city, latitude, longitude)
    # return an answer
    return jsonify({'message': message}), 200

def page_not_found(error):
    return "<h1>Page not found!, sorry d:-D </h1>", 404

if __name__ == '__main__':
    app.register_error_handler(404, page_not_found)
    app.run(host='0.0.0.0', port=5000)