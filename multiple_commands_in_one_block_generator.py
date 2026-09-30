final_command = "/summon minecraft:falling_block "

final_command += input("Enter the position (eg. ~ ~ ~): ").strip().lower() + " {BlockState:{Name:"

end_string = "air}"

more_commands = True
while more_commands:

    command_type = input("Enter command type (n = normal, r = repeating, c = chain): ").strip().lower()
    if command_type == "r":
        command_type = "repeating_"
    elif command_type == "c":
        command_type = "chain_"
    else:
        command_type = ""

    final_command += command_type + 'command_block,Properties:{facing:"'

    direction = input("Enter the command block's facing direction (north, east, south, west, up, down): ").strip().lower()

    final_command += direction + '",conditional:"'

    conditional = input("Is the command block conditional? (y/n): ").strip().lower()
    if conditional == "y":
        conditional = "true"
    else:
        conditional = "false"

    final_command += conditional + '"}},TileEntityData:{auto:'

    always_active = input("Is the command block always active? (y/n): ").strip().lower()
    if always_active == "y":
        always_active = "1"
    else:
        always_active = "0"

    final_command += always_active + ',Command:"'

    command = input("Enter the command: ").strip().lower()

    final_command += command + '"},Passengers:[{id:armor_stand,Health:0,Passengers:[{id:falling_block,BlockState:{Name:'

    end_string += "}]}]"

    if input("Add another command? (y/n): ").strip().lower() == "n":
        more_commands = False

final_command += end_string + "}"
print(final_command)

input("Press Enter to exit...")
