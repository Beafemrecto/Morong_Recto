class Bag:
    def __init__(self, brand, material, color, waterproof, lockable_zippers):
        self.brand = brand
        self.material = material
        self.color = color
        self.waterproof = waterproof
        self.lockable_zippers = lockable_zippers
        
    
    def open(self):
        print("The bag is now open.")
    
    def close(self):
        print("The bag is now closed.")
    
    def adjust_strap(self):
        print("The strap has been adjusted.")
    
    def add_item(self, item):
        self.items = []
        self.items.append(item)
        print(f"{item} has been added to the bag.")
    
    def lock(self):
        print("The bag has been locked.")

our_bag = Bag("Dior", "jacquard", "Black", True, True)

class Cellphone:
    def __init__(self, brand, model, screen_size, camera_quality, sound_quality):
        self.brand = brand
        self.model = model
        self.screen_size = screen_size
        self.camera_quality = camera_quality
        self.sound_quality = sound_quality

    
    def turn_on(self):
        self.is_on = True
        print("Cellphone is now on.")
    
    def turn_off(self):
        self.is_on = False
        print("Cellphone is now off.")
    
    def camera_on(self):
        if self.is_on:
            print("Camera is now on.")
        else:
            print("Cellphone is off. Cannot turn on camera.")
    
    def volume_up(self):
        if self.is_on:
            self.volume = 50
            self.volume += 50
            print("Volume increased to", self.volume)
        else:
            print("Cannot increase volume. Cellphone is off.")
    
    def volume_down(self):
        if self.is_on:
            self.volume -= 50
            print("Volume decreased to", self.volume)
        else:
            print("Cannot decrease volume. Cellphone is off.")

my_phone = Cellphone("Samsung", "Galaxy A51", "6.5 inches", "12 MP", "Stereo speakers")


class Lamp:
    def __init__(self, brand, color, bulb_type, adjustable_neck, touch_control):
        self.brand = brand
        self.color = color
        self.bulb_type = bulb_type
        self.adjustable_neck = adjustable_neck
        self.touch_control = touch_control
        
    
    def turn_on(self):
        self.is_on = True
        print("Lamp is now on.")
    
    def turn_off(self):
        self.is_on = False
        print("Lamp is now off.")
    
    def dim(self):
        if self.is_on:
            self.brightness -= 50
            print("Brightness decreased to", self.brightness)
        else:
            print("Cannot dim lamp. It is off.")
    
    def brighten(self):
        if self.is_on:
            self.brightness = 50
            self.brightness += 50
            print("Brightness increased to", self.brightness)
        else:
            print("Cannot brighten lamp. It is off.")
    
    def adjust_neck(self):
        print("Neck adjusted.")


my_lamp = Lamp("Lontor", "White", "LED", True, True)


class Refrigerator:
    def __init__(self, brand, style, color, capacity, temperature):
        self.brand = brand
        self.style = style
        self.color = color
        self.capacity = capacity
        self.temperature = temperature
    
    def open(self):
        print("The refrigerator door is now open.")
    
    def turn_on(self):
        print("The refrigerator is now turned on.")
    
    def set_temperature(self, new_temperature):
        if new_temperature < -30 or new_temperature > 30:
            print("Invalid temperature setting.")
        else:
            self.temperature = new_temperature
            print(f"The temperature has been set to {new_temperature} degrees celsius.")
    
    def defrost(self):
        print("The refrigerator is now defrosting.")
    
    def set_child_lock(self):
        print("You activated the child lock.")


our_ref = Refrigerator("Panasonic", "Side-by-Side", "Red", 25, -18)


our_bag.open()
our_bag.add_item("Wallet")
our_bag.adjust_strap()
our_bag.close()
our_bag.lock()

my_phone.turn_on()
my_phone.turn_off()
my_phone.camera_on()
my_phone.turn_on()
my_phone.camera_on()
my_phone.volume_up()
my_phone.volume_down()

my_lamp.turn_on()
my_lamp.brighten()
my_lamp.dim()
my_lamp.adjust_neck()
my_lamp.turn_off()

our_ref.open()
our_ref.turn_on()
our_ref.set_temperature(-18)
our_ref.defrost()
our_ref.set_child_lock()
