"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {
                "id": 1,
                "first_name": "John",
                "age": 33,
                "lucky_numbers": [7, 13, 22],
                "last_name": last_name
            },
            {
                "id": 2,
                "first_name": "Jane",
                "age": 35,
                "lucky_numbers": [10, 14, 3],
                "last_name": last_name
            },
            {
                "id": 3,
                "first_name": "Jimmy",
                "age": 5,
                "lucky_numbers": [1],
                "last_name": last_name
            },
        ]

    def _generateId(self):
        return max([member["id"] for member in self._members], default=0) + 1

    def add_member(self, member):
        if "id" not in member:
            member["id"] = self._generateId()
        member["last_name"] = self.last_name
        self._members.append(member)
        return member

    def delete_member(self, id):
        for i, m in enumerate(self._members):
            if m["id"] == id:
                del self._members[i]
                return True
        return False

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    def get_all_members(self):
        return self._members