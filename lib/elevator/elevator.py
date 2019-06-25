class Eelevator:
    def __init__(self, floor_num, people_num, people_list, algo):
        self.floor_num = floor_num
        self.people_num = people_num
        self.algo = algo
        self.people_list = people_list

    def totalTime(self):
