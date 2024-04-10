from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from parser.parse_any_topic import get_html, get_content, URL
from parser.parse_all import parse_all

templates = Jinja2Templates(directory="templates")

app = FastAPI()

app.mount("/static",StaticFiles(directory="static",html=True),name="static")

@app.get("/")
def get_home_page(request : Request):
    all_articles = parse_all()
    response = {"request" : request, "articles" : all_articles["articles"], "sports" : all_articles["sports"], "relevants" : all_articles["relevants"], "travels" : all_articles["travels"], "mains" : all_articles["mains"], "edus" : all_articles["edus"]}
    return templates.TemplateResponse('main.html', response)

