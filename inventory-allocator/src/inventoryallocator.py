class InventoryAllocator:
    def __init__(self):
        pass

    @staticmethod
    def compute_optimal_shipment(order: dict, warehouses: list) -> list:
        order = order.copy()
        optimal_shipment = []
        for warehouse in warehouses:
            warehouse_shipment = {}
            for item in order:
                if item in warehouse:
                    item_instances_to_ship = min(order[item], warehouse[item])
                    if item_instances_to_ship != 0:
                        warehouse_shipment[item] = item_instances_to_ship
                        order[item] -= item_instances_to_ship
            optimal_shipment.append(warehouse_shipment)
        enough_inventory = True
        for item in order:
            if order[item] != 0:
                enough_inventory = False
        if enough_inventory:
            return optimal_shipment
        else:
            return []
