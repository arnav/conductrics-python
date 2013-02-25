Python Wrapper for the Conductrics API.

Install
-------

    git clone git@github.com:conductrics/conductrics-python.git

Add a Project Reference to the Conductrics.csproj within.


Code
----


Set your credentials (they are in your signup email).
		
    import conductrics

    conductrics.apiKey = "...";
    conductrics.ownerCode = "...";


Create one or more agents.

    sortAgent = conductrics.Agent("sample-agent");


Make a choice between any number/type of things.

    order = sortAgent.decide(sessionId, "asc", "desc")


Send a reward when a session reaches one of your application's goals.

    sortAgent.reward(sessionId, value=11.99);

The Agent will learn over time which decisions maximize the reward.
