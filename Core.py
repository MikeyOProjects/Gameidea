max_health = 100

current_health = 100

stab = 10

current_health = current_health - stab

print("You have been stabbed! You lost " + str(stab) + " health points.")
print(f"Your current health is {current_health}")
print("heal yourself.")

potion = 25
elixir = 50
bandage = 10

items = ["potion", "elixir", "bandage"]

print("You have the following items in your inventory: " + ", ".join(items))
print("Choose an item to heal yourself.")
x = input()

if x == "potion":
    current_health += potion
    if current_health > max_health:
        current_health = max_health
    print(f"You used a potion and healed {potion} health points. Your current health is {current_health}.")
elif x == "elixir":
    current_health += elixir
    if current_health > max_health:
        current_health = max_health
    print(f"You used an elixir and healed {elixir} health points. Your current health is {current_health}.")
elif x == "bandage":    
    current_health += bandage
    if current_health > max_health:
        current_health = max_health
    print(f"You used a bandage and healed {bandage} health points. Your current health is {current_health}.")
else:
    print("Invalid item. You cannot heal yourself.")