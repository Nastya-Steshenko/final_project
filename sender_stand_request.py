import configuration
import requests
import data
from data import headers_get_track_number


def post_new_orders(body):

   responses = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_ORDER,
                         json=body,
                         headers=data.headers)

   return responses.json()

#print(post_new_orders(data.orders_body))

def save_track():
    track = post_new_orders(data.orders_body)
    track_number = track['track']
    return track_number

#print(save_track())

def get_orders_track():
    track_number = save_track()
    url = configuration.URL_SERVICE + configuration.GET_ORDERS_TRACK + "?t=" + str(track_number)
    responses = requests.get(url)
    return responses

print(get_orders_track())