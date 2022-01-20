class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device: {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnected")


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print_pages(self, pages):
        if not self.connected:
            print("You are not connected!")
            return
        print(f"Printing {pages} pages")
        self.remaining_pages -= pages


printer = Device("printer", "USB")
print(printer)
printer.disconnect()

new_printer = Printer("printer2", "serial", 500)
new_printer.print_pages(25)
print(new_printer)
new_printer.disconnect()
new_printer.print_pages(10)
