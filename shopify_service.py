import os
import requests

STORE = os.environ.get("SHOPIFY_STORE")
TOKEN = os.environ.get("SHOPIFY_TOKEN")

def get_products():
    query = """
    {
      products(first: 20) {
        edges {
          node {
            id
            title
            handle
            featuredImage {
              url
            }
            priceRange {
              minVariantPrice {
                amount
              }
            }
          }
        }
      }
    }
    """

    response = requests.post(
        f"https://{STORE}/api/2025-01/graphql.json",
        headers={
            "Content-Type": "application/json",
            "Shopify-Storefront-Private-Token": TOKEN
        },
        json={"query": query}
    )

    return response.json()
