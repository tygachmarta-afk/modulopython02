#!/usr/bin/env python3

def input_temperature(data):
    temperature = int(data)
    if temperature > 40:
        raise Exception(f"{temperature}°C is too hot for plants (max 40°C)")
    if temperature < 0:
        raise Exception(f"{temperature}°C is too cold for plants (min 0°C)")
    return temperature


def test_temperature():
    print("=== Garden Temperature Checker ===")
    test_values = ["25", "abc", "100", "-50"]
    print()
    for value in test_values:
        print(f"Input data is '{value}'")
        try:
            tempereture = input_temperature(value)
            print(f"Temperature is now {tempereture}°C\n")
        except Exception as e:
            print(f"Caught input_temperature error: {e}\n")
    
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()