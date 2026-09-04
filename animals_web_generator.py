import json

file_path = 'animals_data.json'

def load_data(file_path):
    with open(file_path) as json_file:
        animals = json.load(json_file)
        return animals


def print_data(animals):
    print_dict = {}

    for animal in animals:
        for key,value in animal.items():
            if key == "name":
                print_dict['Name'] = value
            if key == "characteristics":
                characteristics_dict = value
                print_dict['Diet'] = characteristics_dict['diet']
                if "type" in characteristics_dict:
                    print_dict['Type'] = characteristics_dict['type']
            if key == "locations":
                    print_dict['Location'] = value[0]

        print_sequence = ["Name", "Diet", "Location", "Type"]

        for item in print_sequence:
            if item in print_dict:
                print(f"{item}: {print_dict[item]}")

        print('')
        print_dict = {}


def main():
    data = load_data(file_path)
    read_data(data)


if __name__ == "__main__":
    main()

