from inhabitant import Inhabitant

class Alien(Inhabitant):

    def __init__(self, n="Alien"):
        super().__init__(n)
        self.technology = []

    def __str__(self):
        return f"{self.name} with {self.technology} is here!"

    def __repr__(self):
        return f"Alien(name={self.name}, age={self.age}, energy={self.energy}, technology={self.technology})"

    def pickup(self, technology):
        self.technology.append(technology)

    def drop(self, technology):
        if technology in self.technology:
            self.technology.remove(technology)
