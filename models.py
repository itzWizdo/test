class Recipe:
    title = ""
    thumbnailImage = ""
    sourceUrl = ""
    rating = 0
    totalTime = 0
    ingredients = []
    directions = []

    def __init__(self, name, image, sourceUrl, rating, totalTime, ingredients, directions):
        self.name = name
        self.thumbnailImage = image
        self.sourceUrl = sourceUrl
        self.rating = rating
        self.totalTime = totalTime
        self.ingredients = ingredients
        self.directions = directions
    
    def toDict(self):
        return {
            "name": self.name,
            "thumbnailImage": self.thumbnailImage,
            "source_url": self.sourceUrl,
            "rating": self.rating,
            "totalTime": self.totalTime,
            "ingredients": self.ingredients,
            "directions": self.directions
        }


def create_recipe(name, image, sourceUrl, rating, totalTime, ingredients, directions):
    s = Recipe(name, image, sourceUrl, rating, totalTime, ingredients, directions)
    return s