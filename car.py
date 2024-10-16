
class Car:
    def __init__(self, make, model, year):
        self.make = input("Input make: ")
        self.model = input("Input model: ")
        self.year = input("Input year: ")
        self.is_running = False
    
    def start(self):   
        
        if not self.is_running:
            self.is_running = True
            print(f"{self.year} {self.make} {self.model} has started.")
        else:
            print(f"{self.year} {self.make} {self.model} is already running.")

    def stop(self):
        
        if self.is_running:
            self.is_running = False
            print(f"{self.year} {self.make} {self.model} has stopped.")
        else:
            print(f"{self.year} {self.make} {self.model} is not running.")

    def display_state(self):
        
        state = "running" if self.is_running else "stopped"
        print(f"{self.year} {self.make} {self.model} is currently {state}.")