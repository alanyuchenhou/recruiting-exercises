import unittest
from src.inventoryallocator import InventoryAllocator


class TestInventoryAllocator(unittest.TestCase):
    def test_when_order_is_empty_then_return_empty_shipment(self):
        allocation = {
            'order': {},
            'warehouses': [{}, {'apple': 1, }, ],
            'optimal_shipment': [{}, {}, ],
        }
        self.assertEqual(
            InventoryAllocator.compute_optimal_shipment(allocation['order'], allocation['warehouses']),
            allocation['optimal_shipment']
        )

    def test_when_order_is_unfulfillable_then_return_no_shipment(self):
        allocation = {
            'order': {'apple': 3, },
            'warehouses': [{'apple': 1, }, {'apple': 1, }, ],
            'optimal_shipment': [],
        }
        self.assertEqual(
            InventoryAllocator.compute_optimal_shipment(allocation['order'], allocation['warehouses']),
            allocation['optimal_shipment']
        )

    def test_when_order_can_be_fulfilled_by_only_one_warehouse_then_ship_with_one_warehouse(self):
        allocation = {
            'order': {'apple': 3, },
            'warehouses': [{'orange': 1, }, {'apple': 4, }, ],
            'optimal_shipment': [{}, {'apple': 3, }, ],
        }
        self.assertEqual(
            InventoryAllocator.compute_optimal_shipment(allocation['order'], allocation['warehouses']),
            allocation['optimal_shipment']
        )

    def test_when_order_can_be_fulfilled_by_multiple_warehouses_then_prioritize_closer_warehouses(self):
        allocation = {
            'order': {'apple': 3, },
            'warehouses': [{'apple': 2, }, {'apple': 4, 'banana': 2, }, {'orange': 3, }, ],
            'optimal_shipment': [{'apple': 2}, {'apple': 1}, {}],
        }
        self.assertEqual(
            InventoryAllocator.compute_optimal_shipment(allocation['order'], allocation['warehouses']),
            allocation['optimal_shipment']
        )

    def test_when_order_has_multiple_item_types_then_fulfill_each_type_independently(self):
        allocation = {
            'order': {'apple': 5, 'banana': 5, 'orange': 5, },
            'warehouses': [{'banana': 5, 'orange': 10, 'pear': 20}, {'apple': 5, 'orange': 20, }, ],
            'optimal_shipment': [{'banana': 5, 'orange': 5, }, {'apple': 5, }, ],
        }
        self.assertEqual(
            InventoryAllocator.compute_optimal_shipment(allocation['order'], allocation['warehouses']),
            allocation['optimal_shipment']
        )


if __name__ == '__main__':
    unittest.main()
