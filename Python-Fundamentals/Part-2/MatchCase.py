color = input("Enter a Color 🚥 : ")

match color:
    case "Red" | "red":
        print("STOP⛔")
    case "Green" | "green":
        print("GO💨")
    case "Yellow" | "yellow":
        print("Look👀")
    case _:
        print("Die💀")