from exceptions import DuplicateValue, ValueNotFound

class Cars:
    __cars = []

    def get_cars(self):
        return self.__cars

    def get_car(self, id):
        return next(iter(car for car in self.__cars if car.get('id') == id), None)

    def add_car(self, car):
        if self.get_car(id):
            raise DuplicateValue
        self.__cars.append(car)
        return car

    def delete_car(self, id):
        deleted = False
        for car in self.__cars:
            if car.get('id') == id:
                deleted = True
                self.__cars.remove(car)
                return car
        if not deleted:
            raise ValueNotFound

    def update_car(self, car):
        updated = False
        for i in range(len(self.__cars)):
            if self.__cars[i].get('id') == car.get('id'):
                update = True
                self.__cars[i] = car
                return car
        if not updated:
            raise ValueNotFound
