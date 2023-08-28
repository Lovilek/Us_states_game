import turtle
import pandas
from state import State

screen = turtle.Screen()
screen.title("U.S.A States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []
data = pandas.read_csv("50_states.csv")
list_states = data["state"].to_list()
score = 0
game = True

while game:
    answer = (screen.textinput(title=f"{score}/50 States Correct", prompt="What's the name of the state?")).title()
    check_state = data[data["state"] == answer]

    if answer == "Exit":
        game = False
        not_guessed_list = [item for item in list_states if item not in guessed_states]
        turtle.write("Check your not guessed states in file 'not_guessed.csv'", font=("Courier", 15, "normal"),
                     align="center")
        new_data = pandas.DataFrame(not_guessed_list)
        new_data.to_csv("not_guessed.csv")

    if not check_state.empty:
        state = State(check_state['state'].iloc[0], check_state['x'].iloc[0], check_state['y'].iloc[0])
        guessed_states.append(answer)
        score += 1

    if score == 50:
        turtle.write("You win", align="center", font=("Courier", 50, "normal"))
        game = False

screen.exitonclick()
