import json

import falcon

import arrow

class Timestamp(object):

	def on_get(self, req, resp):
		payload = {}
		payload['utc'] = arrow.utcnow().format('YYYY-MM-DD HH:mm:SS')
		payload['unix'] = arrow.utcnow().timestamp

		resp.body = json.dumps(payload)
		resp.status = falcon.HTTP_200
