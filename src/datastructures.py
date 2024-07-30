
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

"""
John Jackson
33 Years old
Lucky Numbers: 7, 13, 22

Jane Jackson
35 Years old
Lucky Numbers: 10, 14, 3

Jimmy Jackson
5 Years old
Lucky Numbers: 1
"""


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
            "id": self._generate_id(),
            "first_name": "John",
            "last_name": self.last_name,
            "age": 33,
            "lucky_numbers": [self._generate_lucky_number(),
            self._generate_lucky_number(),
            self._generate_lucky_number()]
        },
        {
            "id": self._generate_id(),
            "first_name": "Jane",
            "last_name": self.last_name,
            "age": 35,
            "lucky_numbers": [self._generate_lucky_number(),
            self._generate_lucky_number(),
            self._generate_lucky_number()]
        },
        {
            "id": self._generate_id(),
            "first_name": "Jimmy",
            "last_name": self.last_name,
            "age": 5,
            "lucky_numbers": [self._generate_lucky_number()]
        }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generate_id(self):
        return randint(0, 99999999)
    
    def _generate_lucky_number(self):
        return randint(0, 99)

    def add_member(self, member):
        member.update({
            "id": member.get('id', self._generate_id()),
            "last_name": self.last_name
        })
        self._members.append(member)
        return member

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return True
        return False

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return False

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

