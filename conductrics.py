import httplib
import json
from urlparse import urlparse

class Conductrics:
	baseUrl = "http://api.conductrics.com"
	apiKey = None
	ownerCode = None

def _request(session, *parts, **args):
	u = '/'.join(str(x) for x in (Conductrics.baseUrl, Conductrics.ownerCode) + parts)
	if len(args):
		u += "?" + "&".join("%s=%s"%item for item in args.items())
	u = urlparse(u)
	h = httplib.HTTPConnection(u.netloc, timeout=2)
	h.request("GET", u.path + "?" + u.query, headers = {
		"x-mpath-apikey": Conductrics.apiKey,
		"x-mpath-session": session
	})
	return json.loads(h.getresponse().read())

class Agent:
	def __init__(self, name):
		self.name = name
	
	def decide(self, session, *choices):
		try:
			decision = _request(session, self.name, "decision", len(choices))
			return choices[int(decision['decision'])]
		except:
			return choices[0]

	def reward(self, session, goalCode="goal-1", value=1.0):
		return _request(session, self.name, "goal", goalCode, reward=value)

if __name__ == "__main__":
	import uuid
	Conductrics.apiKey = "api-DfEfOmMFMXJCVAJFwRwXvgLk"
	Conductrics.ownerCode = "owner_EQNeYdvBb"

	a = Agent("python-agent")
	
	sessionId = str(uuid.uuid4())
	print( a.decide(sessionId, "a", "b") )
	print( a.reward(sessionId, value=1.2) )

	sessionId = str(uuid.uuid4())
	print( a.decide(sessionId, "a", "b") )
	print( a.reward(sessionId) )
