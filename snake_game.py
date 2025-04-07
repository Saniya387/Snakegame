import turtle as t
import random

# Game settings
w = 500  # Width of window
h = 500  # Height of window
food_size = 10  # Size of food
delay = 100  # milliseconds

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

SCORE = 0

def reset():
    global snake, snake_dir, food_position, SCORE
    SCORE = 0
    snake.clear()
    snake.extend([[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]])
    snake_dir = "up"
    food_position = get_random_food_position()
    food.goto(food_position)
    move_snake()

def move_snake():
    global SCORE

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_dir][0]
    new_head[1] += offsets[snake_dir][1]

    # Collision with itself
    if new_head in snake[:-1]:
        print(f"Game Over! Final Score: {SCORE}")
        reset()
        return

    snake.append(new_head)

    if not food_collision():
        snake.pop(0)

    # Wall wrap-around
    if new_head[0] > w // 2:
        new_head[0] -= w
    elif new_head[0] < -w // 2:
        new_head[0] += w
    elif new_head[1] > h // 2:
        new_head[1] -= h
    elif new_head[1] < -h // 2:
        new_head[1] += h

    pen.clearstamps()

    for segment in snake:
        pen.goto(segment[0], segment[1])
        pen.stamp()

    screen.update()
    t.ontimer(move_snake, delay)

def food_collision():
    global food_position, SCORE
    if get_distance(snake[-1], food_position) < 20:
        SCORE += 10
        food_position = get_random_food_position()
        food.goto(food_position)
        return True
    return False

def get_random_food_position():
    max_x = (w // 2 - food_size) // 20
    max_y = (h // 2 - food_size) // 20
    x = random.randint(-max_x, max_x) * 20
    y = random.randint(-max_y, max_y) * 20
    return (x, y)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5

# Controls
def go_up():
    global snake_dir
    if snake_dir != "down":
        snake_dir = "up"

def go_down():
    global snake_dir
    if snake_dir != "up":
        snake_dir = "down"

def go_left():
    global snake_dir
    if snake_dir != "right":
        snake_dir = "left"

def go_right():
    global snake_dir
    if snake_dir != "left":
        snake_dir = "right"

# Setup screen
screen = t.Screen()
screen.setup(w, h)
screen.title("Snake Game")
screen.bgcolor("lightgrey")
screen.tracer(0)

# Create turtle for snake
pen = t.Turtle("square")
pen.penup()
pen.speed(0)  # fastest

# Create turtle for food
food = t.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(food_size / 20)
food.penup()
food.speed(0)

# Input bindings
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

# Start game
snake = []
snake_dir = "up"
reset()
t.done()
# Create turtle for displaying score
score_pen = t.Turtle()
score_pen.hideturtle()
score_pen.penup()
score_pen.color("black")
score_pen.goto(0, h//2 - 40)  # Position near top center
def update_score():
    score_pen.clear()
    score_pen.write(f"Score: {SCORE}", align="center", font=("Arial", 16, "bold"))
update_score()
