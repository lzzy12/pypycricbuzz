from .team import Team


class VenueInfo:
    """Venue ID"""
    id: int
    """Ground name"""
    ground: str
    """City"""
    city: str
    """Timezone"""
    timezone: str

    def __init__(self, data) -> None:
        super().__init__()
        self.id = data['id']
        self.ground = data['ground']
        self.city = data['city']
        self.timezone = data['timezone']


class Match:
    """Match id"""
    matchId: int
    """id of the series"""
    seriesId: int
    """name of the series"""
    seriesName: str
    """match description"""
    matchDesc: str
    """match format"""
    matchFormat: str
    """timestamp of start date of the match"""
    startDate: int
    """timestamp of end date of the match"""
    endDate: int
    """state of the match"""
    state: str
    """team 1"""
    team1: Team
    """team 2"""
    team2: Team
    """timestamp of start date of the series"""
    seriesStartDt: str
    """timestamp of end date of the series"""
    seriesEndDt: str
    """whether the time has been announced or not"""
    isTimeAnnounced: bool
    """title of the state of match"""
    stateTitle: str
    """Info about venue of the match"""
    venueInfo: VenueInfo

    def __init__(self, data) -> None:
        super().__init__()
        self.matchId = data['matchId']
        self.seriesId = data['seriesId']
        self.seriesName = data['seriesName']
        self.matchDesc = data['matchDesc']
        self.matchFormat = data['matchFormat']
        self.startDate = int(data['startDate'])
        self.endDate = int(data['endDate'])
        self.state = data['state']
        self.team1 = Team(data['team1'])
        self.team2 = Team(data['team2'])
        self.seriesStartDt = data['seriesStartDt']
        self.seriesEndDt = data['seriesEndDt']
        self.isTimeAnnounced = data['isTimeAnnounced']
        self.stateTitle = data['stateTitle']
        self.venueInfo = VenueInfo(data['venueInfo'])
