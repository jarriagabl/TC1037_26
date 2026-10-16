def battery_check(battery_level):
    if battery_level < 20:
        print("Low battery")
        print("Charge your device now!")
    else:
        print("High battery")
        print("No need to charge your device")
    print("Check complete")

bat = int(input("Current battery level: "))
battery_check(bat)