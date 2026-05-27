# Lab: Build a Planet Class
class Planet:
    def __init__(self, name, mass, radius):
        self.name = name
        self.mass = mass
        self.radius = radius

    @property
    def volume(self):
        return 4 / 3 * 3.14159 * self.radius ** 3

    @property
    def density(self):
        return self.mass / self.volume

earth = Planet("Earth", 5.97e24, 6.371e6)
print(f"{earth.name}: density = {earth.density:.1f} kg/m3")
