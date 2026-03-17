class Person:
    people = {}

    def __init__(self, name : str, age : int) -> None:
        self.name = name
        self.age = age
        self.people.update({name : self})
    wife : str
    husband : str


def create_person_list(people: list) -> list:
    result_list = []
    for i in people:
        result_list.append(Person(i["name"], i["age"]))
    for person in people:
        for partner in result_list:
            if partner.name == person["name"]:
                if "wife" in person.keys() and person["wife"] is not None:
                    for key_name in result_list:
                        if person["wife"] == key_name.name:
                            partner.wife = key_name
                if "husband" in person.keys():
                    if person["husband"] is not None:
                        for key_name in result_list:
                            if person["husband"] == key_name.name:
                                partner.husband = key_name
    return result_list
