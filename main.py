import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

'''
def get_mouse_click_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
'''



df = pd.read_csv("50_states.csv")

all_states = df.state.to_list()
guessed_states = []

while len(guessed_states) < len(all_states):

    answer_state = screen.textinput(title=f'{len(guessed_states)}/{len(all_states)}',
                                    prompt="What's another states' name?").title()
    #Convert to title case
    title_answer_state = answer_state.title()

    if answer_state == "exit":
        missed_states = []
        for state in all_states:
            if state not in guessed_states:
                missed_states.append(state)
        new_data = pd.DataFrame(missed_states)
        new_data.to_csv('states_to_learn.csv')
        break

    if title_answer_state in all_states:
        guessed_states.append(title_answer_state)
        print('good')
        state = turtle.Turtle()
        state.penup()
        state.hideturtle()
        state_row = df[df.state == title_answer_state]
        state.goto(int(state_row.x), int(state_row.y))
        state.write(title_answer_state)





screen.exitonclick()