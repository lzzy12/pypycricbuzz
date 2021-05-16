class Team:
    """Id of the team"""
    teamId: int
    """Name of the team"""
    teamName: str
    """Team short name"""
    teamSName: str
    """Image id of the team (need to extract how to generate the link to image from this ID from the app)"""
    imageId: int

    def __init__(self, data) -> None:
        super().__init__()
        self.teamId = data['teamId']
        self.teamName = data['teamName']
        self.teamSName = data['teamSName']
        self.imageId = data['imageId']
