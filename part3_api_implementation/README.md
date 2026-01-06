# Part 3: Low-Stock Alerts API

## Assumptions

- The database structure designed in Part 2 is used.
- “Recent sales activity” means sales recorded within the past 30 days.
- Stock-out estimate is calculated as CEIL(current_stock / average_daily_sales).
- Only one supplier is returned per product (primary or first linked supplier).
- A `db.query()` method is available; auth is handled externally.

## Edge Cases Handled

- Invalid or unknown company_id → returns 400 Bad Request.
- Products without recent sales are ignored.
- If average sales is zero, days_until_stockout is returned as null.
- Products without suppliers return supplier: null.
- Any unexpected database failure results in a safe 500 error with logging.

## Approach

- Implemented as an Express GET endpoint.
- Uses a single, optimized SQL query with joins across inventory, products, warehouses, and suppliers.
- Applies low-stock and recent-sales filters at the database level for efficiency.
- Keeps the API logic simple, readable, and suitable for production use.
