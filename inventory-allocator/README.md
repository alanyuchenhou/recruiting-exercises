### Problem

Inventory allocator is a class that computes the optimal shipment
given a particular inventory distribution of warehouses.
The warehouses are presorted by shipment cost (
this cost could be time cost or money cost or a weighted sum of both),
where the warehouse with lowest cost of shipment is the first warehouse.

The task is to implement InventoryAllocator class to produce the optimal shipment configuration.
The class should have one function that takes in some input.
The first input will be a map of items being ordered to the amount ordered for each item.
The second input will be a ordered list of warehouses,
where each warehouse is a map of items in stock to the inventory amount for each item.

### How to run the test
- `cd inventory-allocator`: Changes directory to the root of the project.
- `python3 -m unittest discover -s .`: Launches the test runner running all tests.
