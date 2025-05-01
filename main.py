from plant_logic import Soil, Plant, MoistureSensor
from pygame_interface import PygameInterface
import time
import random

def simulate_watering(plant, soil, sensor, days):
    # Create an instance of PygameInterface
    interface = PygameInterface()

    print("Starting simulation...")
    for day in range(days):
        print(f"\nDay {day + 1}:")
        
        # Simulate soil drying out a bit every day
        if day != 0:
            soil.dry_out(random.randint(3,4))

        # Read moisture level from the sensor
        moisture_level = sensor.read_moisture()
        print(f"Moisture level: {moisture_level}")

        # Update plant health based on current soil moisture
        plant.update_health(moisture_level)
        # Print plant health status
        print(f"Plant health: {plant.health}%")

        print(f"Is there Enough Water: {soil.is_perfect_water()}")
        # Water the plant if moisture level is below the threshold
        if not soil.is_perfect_water():
            if soil.is_too_little_water():
                print("Watering plant...")
                # moisture_level
                soil.increase_water(40-moisture_level)  # Water the plant
            else:
                print("Letting the plant dry...")
        else:
                print("The plant is perfect")

        # Pause for a bit before the next day (for simulation purposes)
        time.sleep(2)

        interface.update_display(plant.health, moisture_level, plant.health)
    
        # Handle Pygame events
        if not interface.handle_events():
            break  # Exit the loop if the Pygame window is closed

    print("\nSimulation completed.")

def main():

    # Create instances of Soil, Plant, and MoistureSensor
    soil = Soil(moisture_level=100)  # Initial soil moisture level
    plant = Plant()  # Plant requires a moisture level of 25
    sensor = MoistureSensor(soil)

    # Run the simulation for 10 days with a watering threshold of 20
    #simulate_watering(plant, soil, sensor, days=10)

    for n in range(1,5):
        print("Plant Number: " + str(n))
        a = random.randint(1,100)        
        print(f"The water level starts at {a}")
        # Create instances of Soil, Plant, and MoistureSensor
        soil = Soil(moisture_level=a)  # Initial soil moisture level
        plant = Plant() 
        sensor = MoistureSensor(soil)

        # Run the simulation for 10 days with a watering threshold of 20
        simulate_watering(plant, soil, sensor, days=10)

if __name__ == "__main__":
    main()
