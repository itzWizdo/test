from bs4 import BeautifulSoup
import requests
import json
import models

def scrape_foodNetwork(url: str):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }

    resp = requests.get(url=url, headers=headers)
    if resp.status_code != 200:
        return "failed to fetch recipe"
    
    soup = BeautifulSoup(resp.content, "html.parser")
    scripts = soup.find_all('script')
    dataScript = scripts[len(scripts) - 2]

    try:
        data = json.loads(dataScript.text)
        recipeData = data[0]
        instructions = []

        for instruction in recipeData['recipeInstructions']:
            instructions.append(instruction['text'])


        recipe = models.create_recipe(
            recipeData['name'],
            recipeData['image'][0]['url'],
            recipeData['url'],
            recipeData['aggregateRating']['ratingValue'],
            recipeData['totalTime'],
            recipeData['recipeIngredient'],
            instructions
        ) 
        return recipe
    except Exception as err:
        return "error getting recipe"