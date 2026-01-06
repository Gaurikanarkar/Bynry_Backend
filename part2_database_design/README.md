# Part 2: Database Design

## Design Approach

The database schema is designed using a normalized structure to support the following business needs:

- A single company owning multiple warehouses
- The same product being stored across different warehouses with separate quantities
- Maintaining a history of inventory changes for auditing and tracking
- Managing supplier-to-product relationships
- Supporting bundle products made up of multiple individual products

## Key Constraints

- (company_id, sku) is enforced as unique in the products table to avoid duplicate SKUs within the same company.
- (product_id, warehouse_id) is unique in the inventory table to ensure only one inventory record per product per warehouse.
- Foreign key relationships use cascading deletes to automatically clean up dependent records when a parent entity is removed.

## Missing Requirements – Questions for Product Team

- Should SKU uniqueness apply globally or only within a company?
- Can suppliers work with multiple companies or are they company-specific?
- Which events should be recorded in inventory history (sales, returns, manual updates, transfers)?
- Are product bundles allowed to contain other bundles, or only simple products?
- Do we need to record who performed an inventory change (user, admin, or system)?
- How should “recent activity” be defined for stock alerts or reporting purposes?
