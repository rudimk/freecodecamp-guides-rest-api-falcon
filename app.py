import falcon

from timestamp import Timestamp

api = falcon.API()

timestamp = Timestamp()

api.add_route('/timestamp', timestamp)