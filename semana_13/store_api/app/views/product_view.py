def render_product_list(products):
    return [render_product(product) for product in products]
def render_product(product):
    return {
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "stock": product.stock,
    }