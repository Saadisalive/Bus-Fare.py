class Vehicle:
    def __init__(self, capacity=100):
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def __init__(self, capacity=50):
        super().__init__(capacity)

    def fare(self):
        base_fare = super().fare()
        maintenance_charge = base_fare * 0.10
        return base_fare + maintenance_charge

# Example usage:
bus = Bus()
print("Total Bus fare is:", bus.fare())  # Output: Total Bus fare is: 5500.0