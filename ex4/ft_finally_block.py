#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message="Unknown garden error"):
        self.message = message
        super().__init__(message)


def water_plant(plant_name):
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_sistem(plants):
    print("Opening watering system")
    try:
        for plant_name in plants:
            water_plant(plant_name)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


def main():
    print("=== Garden Watering System ===\n")

    print("Testing valid plants...")
    test_watering_sistem(["Tomato", "Lettuce", "Carrots"])

    print("\nTesting invalid plants...")
    test_watering_sistem(["Tomato", "lettuce", "Carrots"])

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
