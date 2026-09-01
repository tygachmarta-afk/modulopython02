#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message="Unknown garden error"):
        self.message = message
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown garden error"):
        self.message = message
        super().__init__(message)


def check_plant():
    raise PlantError("The tomato plant is wilting!")


def check_water():
    raise WaterError("Not enough water in the tank!")


def  test_custom_errors():
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        check_plant()
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        check_water()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    for operation in (check_plant, check_water):
        try:
            operation()
        except GardenError as e:
            print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")

    
if __name__ == "__main__":
    test_custom_errors()