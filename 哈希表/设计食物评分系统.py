from collections import defaultdict


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodMap={}
        self.cusineMap=defaultdict(SortedList)
        for food,cuisine,rating in zip(foods,cuisines,ratings):
            self.foodMap[food]=[rating,cuisine]
            self.cusineMap[cuisine].add((-rating,food))
    def changeRating(self, food: str, newRating: int) -> None:
        rating,cuisine=self.foodMap[food]
        sl=self.cusineMap[cuisine]
        sl.discard((-rating,food))
        sl.add((-newRating,food))
        self.foodMap[food][0]=newRating

    def highestRated(self, cuisine: str) -> str:
        return self.cusineMap[cuisine][0][1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)