from fastapi import FastAPI
from schemas.product import Product
from models.text_gen import generate_listing
from models.attribute_mapper import map_attributes
from models.forecasting import forecast_stockout
from models.pricing import reprice

app = FastAPI(title="AI Commerce Demo (HF Models)")

@app.post("/listing")
def listing(product: Product):
    return {
        "listing": generate_listing(product.title, product.description)
    }

@app.post("/attributes")
def attributes(product: Product):
    text = product.title + " " + product.description
    return map_attributes(text)

@app.post("/forecast")
def forecast(sales_history: list, inventory: int):
    return {
        "days_until_stockout": forecast_stockout(sales_history, inventory)
    }

@app.post("/pricing")
def pricing(cost: float, competitor_prices: list):
    return {
        "new_price": reprice(cost, competitor_prices)
    }
