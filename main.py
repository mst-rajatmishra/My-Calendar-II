class MyCalendarTwo:
    def __init__(self):
        self.bookings = []  # To keep track of booked intervals
        self.doubles = []   # To keep track of double bookings

    def book(self, start: int, end: int) -> bool:
        # Check for double bookings
        for s, e in self.doubles:
            if max(s, start) < min(e, end):  # There's an overlap
                return False
        
        # Check for triple bookings
        for s, e in self.bookings:
            if max(s, start) < min(e, end):  # There's an overlap
                self.doubles.append((max(s, start), min(e, end)))

        # If we reach here, we can book the event
        self.bookings.append((start, end))
        return True

# Example usage:
obj = MyCalendarTwo()
print(obj.book(10, 20))  # Expected: True
print(obj.book(50, 60))  # Expected: True
print(obj.book(10, 40))  # Expected: True
print(obj.book(5, 15))   # Expected: False
print(obj.book(5, 10))   # Expected: True
print(obj.book(25, 55))  # Expected: True
