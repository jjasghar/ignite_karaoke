from json import load
from jinja2 import Environment, FileSystemLoader
from lib.corporate_buzz import create_buzz_title
import argparse
import os
import random
import webbrowser

template_env = Environment(loader=FileSystemLoader(searchpath='templates'))

def delete_files():
    import glob
    files = glob.glob('volunteers/*.html')
    for f in files:
        os.remove(f)
    os.remove('main.html')

def get_random_image_files():
    return random.sample(os.listdir('imgs/'), 3)


def main():
    with open('config.json') as config_file:
        config = load(config_file)

    parser = argparse.ArgumentParser(description="Create some ignite karaoke decks automagicaly!")
    parser.add_argument('-d', '--delete', action="store_true", help="Delete the volunteer's decks")
    parser.add_argument('-c', '--create', action="store_true", help="Create the decks")
    parser.add_argument('-n', '--names', nargs="+", type=str, help="The list of names you want to create")
    parser.add_argument('-o', '--open', action="store_true", help="Open the web browser too")


    args = parser.parse_args()

    if args.delete:
        delete_files()
        exit(0)
    try:
        list_of_names = list(args.names)
        number_of_volunteers = len(list_of_names)
    except:
        print("No volunteers, you should add some with -n")
        exit(1)

    if args.create:
        # main deck creation
        template = template_env.get_template('main.html.j2')

        for _ in range(number_of_volunteers):
            with open('main.html', 'w') as f:
                f.write(template.render(title=config['title'],
                                        names=list_of_names,
                                        final_clapping=config['final_clapping']
                                        )
                )

        # volunteer deck creation

        template = template_env.get_template('volunteer_deck.html.j2')

        list_of_titles = []
        list_of_pictures = []

        for _ in range(number_of_volunteers):
            list_of_titles.append(create_buzz_title())

        for _ in range(number_of_volunteers):
            list_of_pictures.append(get_random_image_files())

        number = 0
        for name, title in zip(list_of_names, list_of_titles):

            with open(f'volunteers/{name}_deck.html', 'w') as f:
                clapping = random.randint(1, len(config['random_clapping'][0]))
                f.write(template.render(volunteer_title=title,
                                        name=name,
                                        pictures=list_of_pictures[number],
                                        random_clapping=config['random_clapping'][clapping-1]
                                        )
                        )
            number = number + 1

    if args.open:
        filename = "main.html"
        webbrowser.open('file://' + os.path.realpath(filename))


if __name__ == '__main__':
    main()
