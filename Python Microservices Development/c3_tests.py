import requests

def query_url(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def get_hero_names(filter=None):
    url = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json"
    json_body = query_url(url)
    for member in json_body.get('members',[]):
        if filter(member):
            yield member['name']

def get_hero_namesz_v2(hero_data,filter=None):

    for member in hero_data.get('members',[]):
        if filter is None or filter(member):
            yield member

def render_hero_message(heroes,age):
    formatted_text = ""
    for hero in heroes:
        formatted_text += f"{hero['name']} is over {age}\n"
    return formatted_text

def format_heros_over(age=0):
    hero_names = get_hero_names(filter=lambda hero:hero.get('age',0)>age)
    formatted_text = ''
    for hero in hero_names:
        formatted_text += f"{hero} is over {age}\n"
    return formatted_text

def format_heros_over_v2(age=0):
    url = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json"
    json_body = query_url(url)
    relevant_heroes = get_hero_namesz_v2(
        json_body,filter=lambda hero:hero.get('age',0)>age
    )
    return render_hero_message(relevant_heroes,age)

if __name__=='__main__':
    print(format_heros_over(age=10))
    print("-----")
    print(format_heros_over_v2(age=10))

    