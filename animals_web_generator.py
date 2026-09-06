import json

file_path = 'animals_data.json'

def load_data(file_path):
    with open(file_path) as json_file:
        animals = json.load(json_file)
        return animals


def print_data(animals):
    list_animals = []
    for animal in animals:
        print_dict = {}
        print_dict['Name'] = animal['name']
        print_dict['Diet'] = animal["characteristics"]["diet"]
        print_dict['Location'] = animal["locations"][0]
        try:
            print_dict['Type'] = animal["characteristics"]["type"]
        except:
            pass

        for item in print_dict:
            print(f"{item}: {print_dict[item]}")
        print('\n')

        list_animals.append(print_dict)

    return list_animals


def write_html(list_animals):
    repl_strg = ''
    for animal in list_animals:
        repl_strg += '<li class="cards__item">\n'
        repl_strg += f'  <div class="card__title">{animal["Name"]}</div>\n'
        repl_strg += '  <p class="card__text">\n'

        if "Diet" in animal:
            repl_strg += f'    <strong>Diet:</strong> {animal["Diet"]}<br/>\n'

        if "Location" in animal:
            repl_strg += f'    <strong>Location:</strong> {animal["Location"]}<br/>\n'

        if "Type" in animal:
            repl_strg += f'    <strong>Type:</strong> {animal["Type"]}<br/>\n'

        repl_strg += '  </p>\n'
        repl_strg += '</li>\n'


    with open('animals_template.html', 'r') as html_file:
        html_data = html_file.read()

    html_data = html_data.replace("__REPLACE_ANIMALS_INFO__", repl_strg)

    with open('animals_template.html', 'w') as html_file:
        html_file.write(html_data)


def main():
    raw_data = load_data(file_path)
    list_animals = print_data(raw_data)
    write_html(list_animals)


if __name__ == "__main__":
    main()

