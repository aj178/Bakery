from lib.Bill_printing import *
from lib.cost_calculation import *



class Bakery:
    """
    A Bakery class parse the orders and categorize it based on the item code.
    Based on the quantity quoted in the order, the items are packed in bunches.
    """

    def __init__(self):
        self.total_cost = []

    def place_order(self, target):
        if target is '':
            return "order empty"
        else:
            orders = target.splitlines()
            for order in orders:
                order = order.split()
                try:
                    quantity = int(order[0])
                    code = order[1]
                    if "VS5" == code:
                        pack_vegemitte = [3, 5]
                        package_vegemitte = self.packing(pack_vegemitte, quantity)
                        cost_vegemite = Cost().vegemite_scroll(package_vegemitte)
                        self.total_cost.append(cost_vegemite)
                        print_bill().bill_print(quantity, code, cost_vegemite, package_vegemitte)
                    elif "MB11" == code:
                        pack_blueberry = [2, 5, 8]
                        package_blueberry = self.packing(pack_blueberry, quantity)
                        cost_blueberry = Cost().blueberry_muffin(package_blueberry)
                        self.total_cost.append(cost_blueberry)
                        print_bill().bill_print(quantity, code, cost_blueberry, package_blueberry)
                    elif "CF" == code:
                        pack_croissant = [3, 5, 9]
                        package_croissant = self.packing(pack_croissant, quantity)
                        cost_croissant = Cost().croissant(package_croissant)
                        self.total_cost.append(cost_croissant)
                        print_bill().bill_print(quantity, code, cost_croissant, package_croissant)
                    else:
                        print("Invalid code")
                        return "Invalid code"
                except:
                    print("Invalid quantity")
                    return "Invalid quantity"
        return self.total_cost

    def packing(self, packs, quantity):
        """

        :param packs: Number of items that are allowed to be packed as single pack.
        :param quantity: quantity quoted in the order.
        :return: Minimum number of packs.
        """
        result = set()  # set is used to remove the redundant combinations
        intermediate = []
        self.package_breakdown(packs, quantity, result, intermediate)
        result = [list(i) for i in result]
        package = result[0]
        for pack in result:
            if len(pack) < len(package):
                package = pack
        return package

    def package_breakdown(self, packs, target, result, intermediate):
        """
        Recursive function to create the combination of packs.
        :param packs: Number of items that are allowed to be packed as single pack.
        :param target: quantity quoted in the order.
        :return: combination of packs that satisfies the quantity.
        """
        for number in packs:
            if target == number:
                temp = intermediate + [number]
                temp.sort()
                if temp is not None:
                    result.add(tuple(temp))
                return
            elif target > number:
                self.package_breakdown(packs, target - number, result, intermediate + [number])
            else:
                return
