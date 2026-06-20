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
git add .
git commit -m "Fix Shopify product fields"
git push

    return response.json()
