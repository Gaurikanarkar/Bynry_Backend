from flask import request
from decimal import Decimal
from sqlalchemy.exc import IntegrityError
from your_app import app, db
from your_app.models import Product, Inventory

@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.get_json()

    # Basic validation
    if not data:
        return {"error": "Request body is required"}, 400

    if 'name' not in data or 'sku' not in data or 'price' not in data:
        return {"error": "Name, SKU and price are mandatory"}, 400

    try:
        # Create product (warehouse-independent)
        product = Product(
            name=data['name'],
            sku=data['sku'],
            price=Decimal(str(data['price']))
        )

        db.session.add(product)
        db.session.flush()  # generates product.id

        # Create inventory only if warehouse info is provided
        if data.get('warehouse_id') and data.get('initial_quantity') is not None:
            inventory = Inventory(
                product_id=product.id,
                warehouse_id=data['warehouse_id'],
                quantity=data['initial_quantity']
            )
            db.session.add(inventory)

        db.session.commit()

        return {
            "message": "Product created successfully",
            "product_id": product.id
        }, 201

    except IntegrityError:
        db.session.rollback()
        return {"error": "Duplicate SKU not allowed"}, 409

    except Exception:
        db.session.rollback()
        return {"error": "Unable to create product"}, 500
