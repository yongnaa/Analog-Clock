import pygame 

center = (Width / 2, Height / 2) 
clock_radius = 400

Width, Height = 800, 800

pygame.init()

screen = pygame.display.set_mode((Width, Height)) 
pygame.display.set_caption("Digital Clock")
clock = pygame.time.Clock()
FPS = 60 

White = (255, 255, 255) 
Black = (0, 0, 0) 
Red = (255, 0, 0) 

def numbers(number, size, position): 
    font = pygame.font.SysFont("Arial", size, True, False)
    text = font.render(number, True, White) 
    text_rect = text.get_rect(center=(position))

def polar_to_cartesian(r, theta): 
    x = r * sin(pi * theta / 180) 
    y = r * cos(pi * theta / 180) 
    return x + Width / 2, -(y - Height / 2) 

def main(): 
  run = True 
  while run: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False 

    current time = datatime.datatime.now()
    second = current_time.second
    minute = current_time.minute 
    hour = current_time.hour 

    day = current_time.day 
    month = current_time.month 
    year = current_time.year 
    weekday = current_time.today().isoweekday()
    calendar = current_time.today().isocalendar()

    weekdays_abbr = (1: "mo", 2: "Tu", 3: "We", 4: "Th", 5: "Fr", 6: "Sa", 7: "Su")
    weekdays_abbr = weekdays_abbr.get(weekday)

    months_abbr = (1: "JAN", 2: "FEB", 3: "MAR", 4: "APR", 5: "MAY", 6: "JUN", 7: "JUL", 8: "AUG", 9: "SEP", 10: "OCT", 11: "NOV", 12: "DEC") 
    months_abbr = months_abbr.get(month) 

    screen.fill(Black)  
    pygame.draw.circle(screen, White, center, clock_radius - 10, 10)
    pygame.draw.circle(screen, White, center, 12) 
    pygame.draw.rect(screen, White [Width / 2 - 260, Height / 2 - 30, 80, 60], 1)
    pygame.draw.rect(screen, White [Width / 2 - 180, Height / 2 - 30, 80, 60], 1)
    pygame.draw.rect(screen, White [Width / 2 + 100, Height / 2 - 30, 80, 60], 1)
    pygame.draw.rect(screen, White [Width / 2 + 180, Height / 2 - 30, 80, 60], 1)
    pygame.draw.rect(screen, White [Width / 2 - 50, Height / 2 - 30 + 160, 100, 60], 1)

    numbers(str(weekday), 40, (Width / 2 - 330, Height / 2))
    numbers(str(calendar[1], 40, (Width / 2 - 140, Height / 2))
    numbers(str(month), 40, (Width / 2 + 140, Height / 2))
    numbers(str(day), 40, (Width / 2), Height / 2))
    numbers(str(year), 40, (Width / 2, Height / 2 + 160))

    for number in range (1, 13): 
        numbers (str(number), 80, polar_to_cartesian(clock_radius - 80, number * 30))
    for number in range (0, 360, 6):
        if number % 5:
            pygame.draw.line(screen, White, polar_to_cartesian(clock_radius - 80, number * 30), polar_to_cartesian(clock_radius - 30, number), 2)
        else: 
            pygame.draw.line(screen, White, polar_to_cartesian(clock_radius, - 15, number), polar_to_cartesian(clock_radius - 35, number), 6) 

    r = 250 
    theta = (hour + minute / 60 + second / 3600) * (360 / 12)
    pygame.draw.line(screen, White, center, polar_to_cartesian(r, theta), 14) 

    r = 280 
    theta = (minute + second / 60) * (360 / 60) 
    pygame.draw.line(screen, White, center, polar_to_cartesian(r, theta), 10) 

    r = 340 
    theta = second * (360 / 60) 
    pygame.draw.line(screen, Red, center, polar_to_cartesian(r, theta), 4) 

    pygame.display.update()

    clock.tick(FPS)

  pygame.quit()

main()
