class Person:
    people = {}

    def __init__(self, name : str, age : int) -> None:
        self.name = name
        self.age = age
        self.people.update({name : self})


def create_person_list(people: list) -> list:

    result_list = [Person(p["name"], p["age"]) for p in people]
    name_to_person = {p.name: p for p in result_list}
    for partner in people:
        person = name_to_person[partner["name"]]

        if partner.get("wife") is not None:
            person.wife = name_to_person[partner["wife"]]

        if partner.get("husband") is not None:
            person.husband = name_to_person[partner["husband"]]

    return result_list
