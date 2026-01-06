# Part 1: Code Review & Debugging

## 1. Issues Identified

- Request data is not validated, causing failures when fields are missing.
- No mechanism to prevent or handle duplicate SKUs.
- Product model is incorrectly linked to a single warehouse.
- Separate database commits can result in partial data saves.
- No exception handling to recover from database errors.

## 2. Production Impact

- Invalid requests may crash the API.
- Duplicate SKUs lead to incorrect inventory tracking.
- Products cannot be managed across multiple warehouses.
- Incomplete records may exist if one operation fails.
- Clients receive unclear error responses.

## 3. Fixes Applied

- Removed warehouse dependency from Product so products can exist independently of warehouses.
- Used a single database transaction (flush() followed by one commit()) to ensure atomic operations.
- Added validation for required and optional fields and return proper 400-level error responses.
- Handled duplicate SKU cases by catching database integrity errors and responding with a 409 status.
- Created inventory records only when warehouse information is supplied, allowing flexible product creation.
