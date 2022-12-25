import requests
from pprint import pprint
from wp_funcs import meal_image, list_html_list, dict_list, wp_headers, wp_heading_two, openai_intro

api_url = "http://www.themealdb.com/api/json/v1/1/search.php?f=a"
r = requests.get(api_url)
datar=r.json()
meals = datar.get('meals')

single_meals =meals[0]
meal_area = single_meals.get('strArea')
meal_name =single_meals.get('strMeal')
meal_instraction = single_meals.get('strInstructions')
meal_image_src = single_meals.get('strMealThumb')
youtube_video = single_meals.get('strYoutube')
# print(youtube_video)

i = 1

ingredient = {}

while i < 21:
    key_ingredient =f'strIngredient{i}'
    key_measure = f'strMeasure{i}'
    if (single_meals.get(key_ingredient) != None) and (single_meals.get(key_ingredient) != " "):
        ingredient[single_meals.get(key_ingredient)]= single_meals.get(key_measure)
        
    i+=1

instraction_list = meal_instraction.split('\r\n')

title =f'{meal_name} Recipe'
intro = openai_intro(f'write an introduction about {meal_area} {meal_name}')
image = meal_image(meal_image_src, title)
heading_one = wp_heading_two("Ingredient")
ingredient_list = dict_list(ingredient)
heading_two = wp_heading_two("Step by Step Descriptions")
instraction_step = list_html_list(instraction_list)
heading_three = wp_heading_two("Conclusion")
conclusion = openai_intro(f'write an conclution about {meal_area} {meal_name}')
content = f'{intro}{image}{heading_one}{ingredient_list}{heading_two}{instraction_step}{heading_three}{conclusion}'

data_fi = {

    'title': title,
    'content': content,
    'categories': 17,

}

headers= wp_headers('nahid', 'cTpW a426 rwwn qWwt 7P2V y8Vf')
post_url = 'https://birds.local/wp-json/wp/v2/posts'
response=requests.post(post_url, data=data_fi, headers=headers, verify=False)
print(response)






