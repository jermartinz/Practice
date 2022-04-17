


guest_list = ["Fanny", "Ruben", "Irina"]

print(f"Hi {guest_list[0]} i would like to invite you to dinner")
print(f"Hi {guest_list[1]} i would like to invite you to dinner")
print(f"Hi {guest_list[2]} i would like to invite you to dinner")

#3.5 
no_invite = guest_list.remove("Ruben")
print(f"Hi {no_invite} i won't be able to invite you to dinner")


new_guest = guest_list.append("Hector")
print(guest_list)
print(f"Hi {guest_list[0]} i would like to invite you to dinner")
print(f"Hi {guest_list[1]} i would like to invite you to dinner")
print(f"Hi {guest_list[2]} i would like to invite you to dinner")

print(f"Hi {guest_list[0]}, {guest_list[1]} and {guest_list[2]} i found a bigger dinner table")

new_guest2 = guest_list.insert(0, "Isabel")
new_guest3 = guest_list.insert(2, "Ruben")
new_guest4 = guest_list.append("Chris")
print(guest_list)
print(f"Hi {guest_list[0]}, {guest_list[1]}, {guest_list[2]}, {guest_list[3]}, {guest_list[4]} and {guest_list[5]} i found a bigger dinner table!")

print("Sorry, i only can invite two persons")

cant_invite = guest_list.pop(2)
cant_invite1 = guest_list.pop(4)

print(f"Sorry {cant_invite} i can't invite you to dinner")
print(f"Sorry {cant_invite1} i can't invite you to dinner")

print(f"{guest_list.pop(0)} you are not invited yet")
print(f"{guest_list.pop(1)} you are not invited yet")

print(guest_list)
del guest_list[0]
del guest_list[0]


print(guest_list)
