# If Device as a computer is our class, let's represent anything we plugin to computer as params here in init
class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        # Let's assume device is connected to usb or so
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnected.")

# # Let's connect Printer to our computer via USB
# printer = Device("Printer", "usb")
# print(printer)
# printer.disconnect()

# demo on the inheritance
# let's create a printer and make use of above functions in device
class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        # this super will get all the functionalities of __init__ from above Device class
        # Device is the super class for this printer class
        super().__init__(name, connected_by)
        # capacity is the max amount of pages a printer can print
        self.capacity = capacity
        # remaining_pages is how may are left after printing some
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("Your Printer is not connected!")
            return
        print("Printing {pages} pages")
        self.remaining_pages -= pages

# Check point
printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)
printer.disconnect()

# This will say, our printer is not connected
printer.print(30)