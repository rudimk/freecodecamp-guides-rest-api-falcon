import falcon

from timestamp import Timestamp

api = application = falcon.API()

timestamp = Timestamp()

api.add_route('/timestamp', timestamp)