max_health = 100

current_health = 100

current_health <= max_health

stab = 10

attack = current_health - stab

print("You have been stabbed! You lost " + str(stab) + " health points.")

print(f"Your current health is {attack}")

print("heal yourself.")