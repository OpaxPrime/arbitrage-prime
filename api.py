from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List
from business_logic import search_products, generate_listings  # Assuming you saved business logic in a separate file

app = FastAPI()

# Pydantic model for the POST request
class ListingRequest(BaseModel):
    product_name: str
    description: str
    platforms: List[str]

# Example: Endpoint to search for arbitrage opportunities
@app.get("/search")
def search_products_endpoint(
    category: str,
    min_profit: float = Query(0.0, description="Minimum profit margin"),
    max_price: float = Query(None, description="Maximum price"),
):
    return search_products(category, min_profit, max_price)

@app.post("/generate-listing")
def generate_listing(data: ListingRequest):
    product_name = data.product_name
    description = data.description
    platforms = data.platforms
    return generate_listings(product_name, description, platforms)
