import json
import requests

def get_animal(animal_name):
    is_pycharm = True
    if is_pycharm == True:
        headers = {'X-Api-Key': 'ZEbrw0aF3CQFx6iimrGSTg5XuRmOOVap4TdaFW6O'}
    else:
        headers = {'X-Api-Key': '7/sfRmTW99U9mqNPilIZiQ==dmwnYbbSH5FYz9y5'}

    params = {'name': animal_name}
    response = requests.get('https://api.api-ninjas.com/v1/animals', params, headers=headers)

    data = response.json()
    return data


def print_data(animals):
    """Prints Name, Diet, Location, Type of each animal and return list of animal based on that information"""
    list_animals = []
    for animal in animals:
        print_dict = {}
        print_dict['Name'] = animal['name']
        print_dict['Diet'] = animal["characteristics"]["diet"]
        print_dict['Location'] = animal["locations"][0]
        if "type" in animal["characteristics"]:
            print_dict['Type'] = animal["characteristics"]["type"]

        for item in print_dict:
            print(f"{item}: {print_dict[item]}")
        print('\n')

        list_animals.append(print_dict)

    return list_animals


def write_html(list_animals, animal_name):
    """Creates the html formatting of the animal information. Writes these information into the existing html file."""

    if list_animals != []:
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

    else:
        repl_strg = f'<h2 > The animal "{animal_name}" doesn''t exist.</h2>'


    with open('animals_template.html', 'r') as html_file:
        html_data = html_file.read()

    html_data = html_data.replace("__REPLACE_ANIMALS_INFO__", repl_strg)

    with open('animals_template.html', 'w') as html_file:
        html_file.write(html_data)


def main():
    animal_name = input("Enter a name of an animal: ")
    raw_data = get_animal(animal_name)
    list_animals = print_data(raw_data)
    write_html(list_animals, animal_name)


if __name__ == "__main__":
    main()

