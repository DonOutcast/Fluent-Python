def handle_command(message):
    match message:
        case "BEEPER":
            print("BEEPER")
        case "NECK":
            print("NECK")
        case "LED":
            print("LED")

handle_command("BEEPER")