"""HW_3"""

# pylint: disable=C0103

guest_absent = 'Ivan'

guest_list = []
guest_list.append('Alex')
guest_list.append('Natali')
guest_list.append('Ivan')

for guest in guest_list:
    message = f"I would like you - {guest}, to be my guest tonight."
    print(message)

guest_absent = 'Ivan'
message = f"{guest_absent} will be absent tonight"
print(message)

guest_list.remove(guest_absent)
guest_list.append('Jonny')

for guest in guest_list:
    message = f"I would like you - {guest}, to be my guest tonight."
    print(message)
    print(f"{guest} we bought a bigger table")

guest_list.insert(0, 'Olga')
guest_list.insert(2, 'Joy')
guest_list.append('Mila')

for guest in guest_list:
    message = f"I would like you - {guest}, to be my guest tonight."
    print(message)

guest_len = len(guest_list)

while guest_len > 2:
    popped_guest = guest_list.pop()
    message = f"{popped_guest}, I will not can invite you, tonight!"
    print(message)
    guest_len = len(guest_list)

for guest in guest_list:
    message = f"I would like you - {guest}, to be my guest tonight."
    print(message)

del guest_list[:]
print(guest_list)
