
from Elements import Pizza, Drink, Dessert


class CartePizzeria:
    pass


class CartePizzeria:
    def __init__(self):
        self._contains = None
        self.__pizzas = []
        self.__drinks = []
        self.__desserts = []


    def pizzas(self):
        return self.__pizzas

    def is_empty(self):
        return len(self.__pizzas) == 0

    def nb_pizzas(self, pizzas):
        return len(self.__pizzas)

    def add_pizza(self, pizzas):
        self.pizzas().append()

    def remove_pizza(self, name):
        found = False
        for pos, inner_pizza in enumerate(self.pizzas):
            if inner_pizza.name == name:
                found = True
                break
        if not found:
            raise CartePizzeria(f"pizza {name} is not registered")
        del self.pizzas[pos]

    def nb_drinks(self, drink):
        return len(self._drinks)

    def nb_desserts(self, dessert):
        return len(self._desserts)

    def add(self, element):
        if self.__contains._name(element.name):
            raise CartePizzeria(f"element {element.name} is already registered")
        if isinstance(element, Pizza):
            if self.__contains_pizza_ingredients(element.ingredients):
                raise CartePizzeria(f"element {element.name} is already registered with another name")
            self.pizzas.append(element)
        elif isinstance(element, Drink):
            self.drinks.append(element)
        else:
            self.desserts.append(element)

    def __contains_name(self, name):
        all_elements = self.pizzas + self.desserts + self.drinks
        for element in all_elements:
            if element.name == name:
                return True
        return False

    def remove(self, name):
        found = False
        elements_type = [self.__pizzas, self.__desserts, self.__drinks]
        for elements in elements_type:
            for pos, inner_pizza in enumerate(elements):
                if inner_pizza.name == name:
                    found = True
                    break
            if not found:
                raise CartePizzeria(f"pizza {name} is not registered")
            del self.pizzas[pos]


