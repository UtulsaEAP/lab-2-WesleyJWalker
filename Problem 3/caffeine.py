
def caffeine():
    caffeine_mg = float(input())
    after6 = float(caffeine_mg / 2)
    after12 = float(after6 / 2)
    after24 = float(after12 / 4)
    print("After 6 hours: " + (f'{after6:.2f}') + " mg\nAfter 12 hours: " + (f'{after12:.2f}') + " mg\nAfter 24 hours: " + (f'{after24:.2f}') + " mg")
    
if __name__ == "__main__":
    caffeine()