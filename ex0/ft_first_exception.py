#!/usr/bin/env python3

def input_tempereture(temp_str):
    return int(temp_str)


def test_temperature():
    print("=== Garden Temperature ===")
    print()
    valid_input = "25"
    print(f"Input data is '{valid_input}'")
    try:
        temperature = input_tempereture(valid_input)
        print(f"Temperature is now {temperature}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print()
    invalid_input = "abc"
    print(f"Input data is '{invalid_input}'")
    try:
        temperature = input_tempereture(invalid_input)
        print(f"Temperature is now {temperature}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
