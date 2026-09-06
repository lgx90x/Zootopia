import json

file_path = 'animals_data.json'

def load_data(file_path):
    with open(file_path) as json_file:
        animals = json.load(json_file)
        return animals


def print_data(animals):
    print_dict = {}
    repl_strg = ''
    for animal in animals:
        for key,value in animal.items():
            if key == "name":
                print_dict['Name'] = value
            if key == "characteristics":
                characteristics_dict = value
                print_dict['Diet'] = characteristics_dict['diet']
                if "type" in characteristics_dict:
                    print_dict['Type'] = characteristics_dict['type']
                else:
                    print_dict['Type'] = None
            if key == "locations":
                    print_dict['Location'] = value[0]

        print_sequence = ["Name", "Diet", "Location", "Type"]

        for item in print_sequence:
            if print_dict[item] is not None:
                print(f"{item}: {print_dict[item]}")
                repl_strg += f"{item}: {print_dict[item]} \n"
        repl_strg += "\n"
        print("\n")

    return repl_strg


def write_html(repl_strg):
    with open('animals_template.html', 'r') as html_file:
        html_data = html_file.read()
    html_data = html_data.replace("__REPLACE_ANIMALS_INFO__", repl_strg)
    print(html_data)

    with open('animals_template.html', 'w') as html_file:
        html_file.write(html_data)



def main():
    data = load_data(file_path)
    repl_strg = print_data(data)
    write_html(repl_strg)



if __name__ == "__main__":
    main()

