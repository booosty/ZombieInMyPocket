import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.turn = 1
        self.turn_list = []
        self.health_list = []

    def increase_turn(self):
        self.turn_list.append(self.turn)
        self.turn += 1

    def add_health(self, health):
        self.health_list.append(health)

    def generate_health_turn_graph(self):
        x = self.turn_list
        y = self.health_list

        plt.plot(x, y)
        plt.title("Health at Each Turn")
        plt.xlabel("Turn Number")
        plt.ylabel("Health")
        plt.show()


