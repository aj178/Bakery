class Cost:

    def vegemite_scroll(self, packs):
        """
        Calculates the to price of the order based on fixed base price for each kind of package.
        :param packs: Number of packs.
        :return: Total amount for the ordered vegemitte scrolls.
        """
        base_price_3 = 6.99
        base_price_5 = 8.99
        price = 0
        for i in packs:
            if i == 3:
                price += base_price_3
            else:
                price += base_price_5
        return "{0:.2f}".format(price, 2)

    def blueberry_muffin(self, packs):
        """
        Calculates the to price of the order based on fixed base price for each kind of package.
        :param packs: Number of packs.
        :return: Total amount for the ordered Blueberry Muffins.
        """
        base_price_2 = 6.95
        base_price_5 = 16.95
        base_price_8 = 24.95
        price = 0
        for i in packs:
            if i == 2:
                price += base_price_2
            elif i == 5:
                price += base_price_5
            else:
                price += base_price_8
        return "{0:.2f}".format(price, 2)

    def croissant(self, packs):
        """
        Calculates the to price of the order based on fixed base price for each kind of package.
        :param packs: Number of packs.
        :return: Total amount for the ordered croissants.
        """
        base_price_3 = 5.95
        base_price_5 = 9.95
        base_price_9 = 16.99
        price = 0
        for i in packs:
            if i == 3:
                price += base_price_3
            elif i == 5:
                price += base_price_5
            else:
                price += base_price_9
        return "{0:.2f}".format(price, 2)