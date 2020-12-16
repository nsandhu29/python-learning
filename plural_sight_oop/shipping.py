class ShippingContainer:
    # Defining class attributes
    next_serial = 1337

    # Defining Static method, we can use classmethod and staticmethod decorators
    # @staticmethod
    # def _generate_serial():
    #     result = ShippingContainer.next_serial
    #     ShippingContainer.next_serial += 1
    #     return result
    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=[])

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._generate_serial()
        # Referring to class attributes
        # self.serial = ShippingContainer.next_serial
        # ShippingContainer.next_serial += 1
        # Although we can read class attribute using self statement but it is avoided
        # Instance attribute takes precedence over class attributes when accessed with self
        # self.serial = self.next_serial
        # self.next_serial += 1

c1 = ShippingContainer("YML", ["books"])
c2 = ShippingContainer("COSCO", ["clothes"])
c3 = ShippingContainer("MAE", ["tools"])
c4 = ShippingContainer("YML", ["Coffee"])
c5 = ShippingContainer.create_empty("YML")
c6 = ShippingContainer.create_with_items("MAE", {"food", "textiles", "minerals"})
print(c1.serial)
print(c2.serial)
print(c4.serial)
print(ShippingContainer.next_serial)
print(c5)
print(c5.contents)
print(c6.contents)

