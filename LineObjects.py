class LineObjects:
    # __slots__ reduces memory usage by setting a specific amount of attributes
    # to the class LineObjects, usually attributes are linked to the class through
    # a dict, which uses a lot of memory.
    __slots__ = ["state", "county", "runner", "party", "votes", "w_or_l"]

    def __init__(self, state, county, runner, party, votes, w_or_l):
        self.state = state
        self.county = county
        self.runner = runner
        self.party = party
        self.votes = votes
        self.w_or_l = w_or_l
