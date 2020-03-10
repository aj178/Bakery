class print_bill:

    def bill_print(self, quantity, code, cost, package):
        """
        Printing the bill for the order placed.
        :param quantity: quantity quoted in the order.
        :param code: code tells which item has ordered.
        :param cost: total cost for the item that has ordered.
        :param package: package shows how the quantity is broken down different packs.
        """
        print(quantity, code, "$" + str(cost))
        if code == "VS5":
            if package.count(3):
                print("\t", str(package.count(3)) + " * 3 $6.99")
            if package.count(5):
                print("\t", str(package.count(5)) + " * 5 $8.99")
        elif code == "MB11":
            if package.count(2):
                print("\t", package.count(2), "*", 2, " $9.95")
            if package.count(5):
                print("\t", package.count(5), "*", 5, " $16.95")
            if package.count(8):
                print("\t", package.count(8), "*", 8, " $24.95")
        else:
            if package.count(3):
                print("\t", package.count(3), "*", 3, " $5.95")
            if package.count(5):
                print("\t", package.count(5), "*", 5, " $9.95")
            if package.count(9):
                print("\t", package.count(9), "*", 9, " $16.99")
