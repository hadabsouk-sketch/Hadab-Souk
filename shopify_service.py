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

    variants(first: 1) {
      edges {
        node {
          id
        }
      }
    }

    featuredImage {
      url
    }

    priceRange {
      minVariantPrice {
        amount
      }
    }
}        }
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


def format_products():
    data = get_products()

    products = []

    for edge in data["data"]["products"]["edges"]:
        p = edge["node"]

        products.append({
            "id": p["id"],
            "slug": p["handle"],
            "name_en": p["title"],
            "name_ar": p["title"],
            "price": float(
                p["priceRange"]["minVariantPrice"]["amount"]
            ),
            "image": (
                p["featuredImage"]["url"]
                if p.get("featuredImage")
                else ""
            ),
            "brand": "Hadab Souk",
            "badge": "",
            "reviews": 0,
            "rating": 5,
            "old_price": None,
            "featured": True,
            "best_seller": True
        })

    return products


def get_product_by_handle(handle):
    query = f"""
    {{
      product(handle: "{handle}") {{
        id
        title
        handle
        description
        featuredImage {{
          url
        }}
        priceRange {{
          minVariantPrice {{
            amount
          }}
        }}
      }}
    }}
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
