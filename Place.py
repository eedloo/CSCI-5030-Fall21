class Place:
    placeName = ''
    placeType = ''

    def create_place(self, placeName, placeType):
        self.placeName = placeName
        self.placeType = placeType
        return [f'CreatePlace({self.placeName}, {self.placeType})']
