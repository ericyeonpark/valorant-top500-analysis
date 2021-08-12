import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.tasks import repeat_every

# scraping functions from scraper.py
from scraper.py import scrape
from scraper.py import scrape_kor, scrape_eu, scrape_na, scrape_ap, scrape_br, scrape_la




description = """
App to scrape DAK.GG for Top 500 Valorant player stats from the NA, EU, KOR, AP, BR, LA 

To use these interactive docs:
- Click on an endpoint below
- Click the **Try it out** button
- Edit the user_input field to predict whether text input contains police violence
- Click the **Execute** button
- Scroll down to see the Server response Code & Details
"""

app = FastAPI(
    title='Valorant Scraping App',
    description=description,
    docs_url='/',
)


@app.get("/frankenbert/{user_input}")
async def frankenbert(user_input):
    return get_rank_of_force(user_input)


@app.on_event('startup')
@repeat_every(seconds=60*60*24)  # set to run function below every 24 hours 60*60*24
async def run_update() -> None:
    #Add to scraper.log when scraper is called
    logging.info('is when the scraper was called')
    #updates possible incidents from twitter
    update_twitter_data()
    # Add to scraper log when scraper has finished
    logging.info('is when the scraper finished')


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)
