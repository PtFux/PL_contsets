class Vehicle:
    def __init__(self, item: int, max_speed: int):
        self.item = item
        self.max_speed = max_speed

    def riding(self, track: int, tr_time: int):
        dist = (self.max_speed * tr_time) % track     # distance to finish
        return min(dist, track - dist)


class MechanicalVehicle(Vehicle):
    def __init__(self, item: int, max_speed: int, petrol: int):
        super().__init__(item, max_speed)
        self.refueling(petrol)

    def refueling(self, petrol: int):
        pass


class Car(MechanicalVehicle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def refueling(self, petrol: int):
        power = {98: 1, 95: 0.9, 92: 0.8}
        self.max_speed = self.max_speed * power.get(petrol)


class Bike(MechanicalVehicle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def refueling(self, petrol: int):
        power = {98: 1, 95: 0.8, 92: 0.6}
        self.max_speed = self.max_speed * power.get(petrol)


class Cart(Vehicle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


if __name__ == "__main__":
    INF = 10**6
    n, track, travel_time = map(int, input().split())

    winner = (INF, INF)
    for i in range(n):
        char = list(map(int, input().split()))

        if char[1] == 1:
            veh = Car(char[0], char[2], char[3])
        elif char[1] == 2:
            veh = Bike(char[0], char[2], char[3])
        else:
            veh = Cart(char[0], char[2])

        if winner[0] > veh.riding(track, travel_time):
            winner = (veh.riding(track, travel_time), veh.item)
        elif winner[0] == veh.riding(track, travel_time) and veh.item < winner[1]:
            winner = (veh.riding(track, travel_time), veh.item)

    print(winner[1])
