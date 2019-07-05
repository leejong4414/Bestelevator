class Elevator:
    def __init__(self, max_floor, algo):
        self.max_floor = max_floor
        self.algo = algo
        self.clicked_floors = set()
        self.current_floor = 1

    def person_click_floor(self, floor):
        self.clicked_floors.add(floor)
