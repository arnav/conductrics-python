import httplib
import json
from urlparse import urlparse

baseUrl = "http://api.conductrics.com"
apiKey = None
ownerCode = None

def _request(session, *parts, **args):
	u = '/'.join(str(x) for x in (baseUrl, ownerCode) + parts)
	if len(args):
		u += "?" + "&".join("%s=%s"%item for item in args.items())
	u = urlparse(u)
	h = httplib.HTTPConnection(u.netloc, timeout=2)
	h.request("GET", u.path + "?" + u.query, headers = {
		"x-mpath-apikey": apiKey,
		"x-mpath-session": session
	})
	return json.loads(h.getresponse().read())

class Agent:
	def __init__(self, name):
		self.name = name
	
	def decide(self, session, *choices, **opts):
		try:
			decision = _request(session, self.name, "decision", len(choices), **opts)
			return choices[int(decision['decision'])]
		except:
			return choices[0]

	def reward(self, session, goalCode="goal-1", value=1.0):
		return _request(session, self.name, "goal", goalCode, reward=value)

        def expire(self, session):
            return _request(session, self.name, "expire")

if __name__ == "__main__":
	import uuid
	apiKey = "api-nQyALpnyPsZHQrVbvtOhZpYz"
	ownerCode = "owner_sxvgyHUlj"

	a = Agent("python-test-features")
	
	sessionId = str(uuid.uuid4())
	print( a.decide(sessionId, "a", "b", features="ugly") )
	print( a.reward(sessionId, value=.8) )

	sessionId = str(uuid.uuid4())
	print( a.decide(sessionId, "a", "b", features="handsome") )
	print( a.reward(sessionId, value=1.2) )
