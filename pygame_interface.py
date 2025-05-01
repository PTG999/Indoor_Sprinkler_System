# pygame_interface.py
from plant_logic import Soil, Plant, MoistureSensor
import pygame

class PygameInterface:
    def __init__(self, width=800, height = 600):
        pygame.init()  #starting the pygame engine
        
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Plant Watering Simulation")

        # Colors
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 128, 0)
        self.BROWN = (139, 69, 19)
        self.BLUE = (115, 163, 240)
        self.GOLD = (252, 219, 3)

        # Plant and Pot dimensions and positions
        self.plant_pos = (width // 2, height // 2)
        self.pot_width = 100
        self.pot_height = 50

    def draw_plant_pot(self):
        # Draw plant pot
        pot_rect = pygame.Rect(300,350,100,120)
        pygame.draw.rect(self.screen, self.BROWN, pot_rect)
    
    def draw_plant_stem(self):
        # Draw plant stem
        pygame.draw.line(self.screen, self.GREEN,(350,350),(350,225),7)
    
    def draw_middle(self):
        #Draw middle circle of plant
        pygame.draw.circle(self.screen,self.BROWN,(350,225),15)

    def draw_plant(self, health):
        # Draw plant based on health
        if health > 70:
            color = self.GOLD
        else:
            color = (health * 2, 128, 0)  # Weaker plants are less green

        # Simple representation of a plant
        pygame.draw.circle(self.screen, color,(375, 225), 18)
        pygame.draw.circle(self.screen, color,(325, 225), 18)
        pygame.draw.circle(self.screen, color,(350, 200), 18)
        pygame.draw.circle(self.screen, color,(350, 250), 18)

    def screen_color(self):
        self.screen.fill(self.BLUE)

    def draw_moisture_level(self, moisture_level):
        # Draw moisture level indicator
        font = pygame.font.SysFont(None, 36)
        text = font.render(f'Moisture Level: {moisture_level}%', True, self.BLACK)
        self.screen.blit(text, (10, 10))
    
    def draw_health_level(self, health_level):
        # Draw health level indicator
        font = pygame.font.SysFont(None, 36)
        text = font.render(f'Healthy level: {health_level}%', True, self.BLACK)
        self.screen.blit(text, (10, 40))

    def update_display(self, plant_health, moisture_level, health_level):
        self.screen.fill((255, 255, 255))  # Clear screen

        self.screen_color()
        self.draw_plant_pot()
        self.draw_plant_stem()
        self.draw_plant(plant_health)
        self.draw_moisture_level(moisture_level)
        self.draw_health_level(health_level)
        self.draw_middle()

        pygame.display.flip()  # Update the full display

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
        return True