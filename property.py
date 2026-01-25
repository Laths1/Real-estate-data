class Property:
    def __init__(self, title, price, bed, bath, garage, sqm, location, details_url=None):
        self.title = title
        self.price = price
        self.bed = bed
        self.bath = bath
        self.garage = garage
        self.sqm = sqm
        self.details_url = details_url
        self.location = location

    def prop_to_string(self):
        return f"Title: {self.title},Location: {self.location} ,Price: {self.price}, Beds: {self.bed}, Baths: {self.bath}, Garage: {self.garage}, Size: {self.sqm}, Details URL: {self.details_url}"