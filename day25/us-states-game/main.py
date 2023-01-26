import turtle
import pandas 

FONT = ('Arial', 8, 'normal')

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
list_of_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    guess = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
                            prompt="What's another state's name").title()

    if guess == "Exit":
        missing_states = []
        for state in list_of_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if guess in list_of_states:
        guessed_states.append(guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == guess]                  # This code allows you to pull the row ie Alabama  139 -77 
        t.goto(int(state_data.x), int(state_data.y))
        t.write(guess)


# states_to_learn.csv








# Code to figure out the x, y coordinates in 50_states.csv enable to tweak coordinates

# def get_mouse_click_coor(x, y):
#     '''generate the coordinates for our 50 states.csv data'''
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

