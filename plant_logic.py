class Soil:
    def __init__(self, within_mositure_range=True, moisture_level=0,grams_of_soil=100):
        self.moisture_level = moisture_level  # Represents the moisture level of the soil
        self.within_mositure_range = within_mositure_range # bool to check if it's within range
        self.grams_of_soil = grams_of_soil

    def is_too_much_water(self):
        if self.moisture_level > 60:
            self.within_mositure_range = False
            return True
        else:
            self.within_mositure_range = True
            return False

    def is_too_little_water(self):
        if self.moisture_level < 30:
            self.within_mositure_range = False
            return True
        else:
            self.within_mositure_range = True
            return False

    def is_perfect_water(self):
        if self.is_too_little_water() or self.is_too_much_water():
            self.within_mositure_range = False
            return False
        else:
            self.within_mositure_range = True
            return True

    def increase_water(self, amount):
        # 
        self.moisture_level += amount
        

    def dry_out(self, amount):
        self.moisture_level = max(0, self.moisture_level - amount) # Decrease moisture level, ensuring it doesn't go below 0


class Plant:
    def __init__(self, min_water_requirement=30, max_water_requirement=50, health=100):
        self.min_water_requirement = min_water_requirement  # Water required by the plant
        self.max_water_requirement=max_water_requirement
        self.health = health  # Health of the plant, 0-100%

    def update_health(self, soil_moisture):
        if soil_moisture < self.min_water_requirement or soil_moisture> self.max_water_requirement:
            self.health -= 5 
        else:
            self.health = min(100, self.health + 2)  # Increase health if conditions are good, max 100%


class MoistureSensor:
    def __init__(self, soil):
        self.soil = soil  # Reference to the soil object

    def read_moisture(self):
        return self.soil.moisture_level  # Return the current moisture level of the soil
