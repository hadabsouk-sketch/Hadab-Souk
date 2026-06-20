import os
import requests

STORE = os.environ.get("SHOPIFY_STORE")
TOKEN = os.environ.get("SHOPIFY_TOKEN")

def get_products():
    return {
        "store": STORE,
        "token_exists": TOKEN is not None,
        "token_length": len(TOKEN) if TOKEN else 0
    }

    response = requests.post(
        f"https://jdfd0q-2v.myshopify.com/api/2024-10/graphql.json",
        headers={
            "Content-Type": "application/json",
            "X-Shopify-Storefront-Access-Token": TOKEN
        },
        json={"query": query}
    )

    return response.json()
