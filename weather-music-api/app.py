import json
import requests
import pg8000
from datetime import datetime


def lambda_handler(event, context):
    city = event['city']
    user = event['user']
    access_time = now = datetime.now()
    try:
        temp, lat, lon = request_weather(city)
        print(temp)
        cat = temp_to_categorical(temp)
        playlist_id = get_playlist_id(cat)
        playlist = request_playlist(playlist_id)
        insert_into_dw(user, cat, playlist_id, access_time, city, temp, lat, lon)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "playlist": playlist,
                "temp": temp

            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": f"{e}"

            })
        }


def request_weather(city):
    request_temp = requests.get(
        F'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID=abc186d42faeec350e9e25fb02307fd4&units=metric')
    response_temp = request_temp.json()
    temp = response_temp['main']['temp']
    lat = response_temp['coord']['lat']
    long = response_temp['coord']['lon']
    return temp, lat, long


def temp_to_categorical(temp):
    cat = None
    if temp < 10:
        cat = 'classic'
    elif temp >= 10 and temp <= 25:
        cat = 'rock'
    elif temp > 25:
        cat = 'pop'

    return cat


def get_playlist_id(cat):
    playlist_id = None
    playlists = {
        'rock': '6046716724',
        'pop': '2021502402',
        'classic': '4590803744'
    }
    if cat == 'rock':
        playlist_id = playlists['rock']
    elif cat == 'pop':
        playlist_id = playlists['pop']
    elif cat == 'classic':
        playlist_id = playlists['classic']

    return playlist_id


def request_playlist(id):
    request = requests.get(
        f'https://api.deezer.com/playlist/{id}/tracks'
    )
    response = request.json()

    playlist = [music['title'] for music in response['data']]
    return playlist


def insert_into_dw(user, cat, playlist_id, access_time, city, temp, lat, lon):
    config = {"database": "postgres", "host": "ingaia-test.chgnxd3omlck.us-east-1.rds.amazonaws.com",
              "port": 5432,
              "user": 'ingaia', "password": 'dan969359'}

    con = pg8000.connect(database=config['database'], host=config['host'], port=config['port'], user=config['user'],
                         password=config['password'], ssl=True)

    con.autocommit = True

    cur = con.cursor()

    cur.execute(f"""INSERT INTO ingaia ("user", "cat","playlist_id","access_time","city","temp","lat","lon")
                    VALUES ('{user}','{cat}','{playlist_id}','{access_time}','{city}', {temp}, {lat},{lon})""")

    con.close()
