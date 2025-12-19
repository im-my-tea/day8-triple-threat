
def format_name(name):
    final = ""
    for i in name:
        if i != "": final += i.title() + " "
    return final

# name = input("Enter your name: ").strip().lower().split(" ")
# print(f"Hello, {format_name(name)}")


player_health = 10
def drink_potion(player_health):
    player_health += 5
    return player_health


print("Player health:", drink_potion(player_health))