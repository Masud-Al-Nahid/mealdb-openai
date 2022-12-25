
#python list to html list
def list_html_list(any_list):
    """
    python list to html list
    """
    start = '<!-- wp:list --><ul>'
    for eliment in any_list:
        start+= f'<!-- wp:list-item --><li>{eliment}</li><!-- /wp:list-item -->'
        
    ends ='</ul><!-- /wp:list -->'
    code = start+ends
    return code


def dict_list(dicts):
    start = '<!-- wp:list --><ul>'
    for key, value in dicts.items():
        start+= f'<!-- wp:list-item --><li><strong>{key.title()}</strong>: {value}</li><!-- /wp:list-item -->'
        
    ends ='</ul><!-- /wp:list -->'
    code = start+ends
    return code


def wp_headers(username, password):
    import base64
    credintial =f'{username}: {password}'
    token = base64.b64encode(credintial.encode())
    code ={'Authorization': f'Basic {token.decode("utf-8")}'}
    return code


def meal_image(src, name):
    first_line = f'<!-- wp:image {{"align":"center","width":700,"height":700,"sizeSlug":"large"}} -->'
    second_line = f'<figure class="wp-block-image aligncenter size-large"><img src="{src}" alt="{name}"/>'
    third_line =f'<figcaption class="wp-element-caption">{name}</figcaption></figure><!-- /wp:image -->'
    code =f'{first_line}{second_line}{third_line}'
    return code

def wp_heading_two(text):
    code = f'<!-- wp:heading --><h2>{text}</h2><!-- /wp:heading -->'
    return code

def openai_intro(text):
    import os
    from dotenv import load_dotenv
    load_dotenv()
    import openai
    openai.api_key = os.getenv("API_KEY")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    pdata=response.get('choices')[0].get('text').strip()
    code = f'<!-- wp:paragraph --><p>{pdata}</p><!-- /wp:paragraph -->'
    return code
