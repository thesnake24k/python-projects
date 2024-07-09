import turtle
import pandas

# setup our turtle
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.setup(725, 491)
screen.addshape(image)
turtle.shape(image)


# get our states from external file and convert it to a list
state_data = pandas.read_csv("50_states.csv")
states_names = state_data["state"]
list_states = states_names.to_list()

score = 0
answer_list = []
states_to_learn = []
while score < 50:
    answer = screen.textinput(title=f" {score} out of 50. what is your answer",
                              prompt="what's another state's name?").title()
    if answer == "Exit":
        # for states in list_states:
        #     if states not in answer_list:
        #         states_to_learn.append(states)
        # new_data = pandas.DataFrame(states_to_learn)
        # new_data.to_csv("states_to_lrean.csv")
        # break
        states_to_learn = [states for states in list_states if states not in answer_list]
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_lrean.csv")
        break

    if answer in list_states and (answer in answer_list) == False:
        sc = turtle.Turtle()
        sc.hideturtle()
        sc.penup()
        state_row = state_data[state_data["state"] == answer]
        sc.goto(int(state_row.x), int(state_row.y))
        print(state_row.x, state_row.y)
        sc.write(answer)
        score += 1
        answer_list.append(answer)