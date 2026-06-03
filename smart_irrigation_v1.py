def calculate_water(soil, crop, temperature):
    water = 0

    if soil == "sandy":
        water = 8
    elif soil == "clay":
        water = 5
    elif soil == "loamy":
        water = 7

    if crop == "rice":
        water += 3
    elif crop == "wheat":
        water += 2
    elif crop == "cotton":
        water += 1
    elif crop == "maize":
        water += 4

    if temperature > 35:
        water += 2

    return water


history = []

while True:
    print("\n===== SMART IRRIGATION SYSTEM =====")
    print("1. New Prediction")
    print("2. View History")
    print("3. About Project")
    print("4. Exit")
    print("5. Clear History")

    choice = input("Enter your choice: ")

    if choice == "1":
        soil = input("Enter soil type: ").lower()
        crop = input("Enter crop type: ").lower()
        temperature = int(input("Enter temperature: "))

        if soil not in ["sandy", "clay", "loamy"]:
            print("Invalid soil type!")
        elif crop not in ["rice", "wheat", "cotton", "maize"]:
            print("Invalid crop type!")
        else:
            result = calculate_water(soil, crop, temperature)
            print("Recommended water:", result, "litres")

            history.append(
                f"Soil: {soil}, Crop: {crop}, Temp: {temperature}, Water: {result} litres"
            )

    elif choice == "2":
        print("\nPrediction History")

        if len(history) == 0:
            print("No records found.")
        else:
            for item in history:
                print(item)

    elif choice == "3":
        print("Smart Irrigation System")
        print("Developed using Python")
        print("Helps farmers estimate water requirements.")

    elif choice == "4":
        print("Thank you for using Smart Irrigation System!")
        break
    elif choice == "5":
        history.clear()
        print("History cleared successfully!")

    else:
        print("Invalid choice! Please enter 1, 2, 3, 4, or 5.")