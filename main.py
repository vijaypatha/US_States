import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title="Guess the State", prompt="Guess the next state").title()
    data = pd.read_csv("50_states.csv")

    for state in data["state"]:
        if answer_state == "Exit":
            break

        if answer_state == state:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state)

screen.exitonclick()

#import pandas as pd
# data = pd.read_csv("weather_data.csv")
# print(data.temp)
# print(data["temp"])
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# print(data[data.condition == "Sunny"])
#
# print(f"temp column: {data.temp}")
# print(data[data.temp > 20])
# print(data[data.condition == "Sunny"])
# print(data[data.temp == data.temp.max()])
# print(f"temp greater than mean: {data[data.temp < data.temp.mean()]}")

# data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# tar = data["Primary Fur Color"].value_counts()
# final = pd.DataFrame(tar)
# print(final)
#
# black_squirrel = (len(data[data["Primary Fur Color"] == "Black"]))
# Gray_squirrel = (len(data[data["Primary Fur Color"] == "Gray"]))
# Cinnamon_squirrel = (len(data[data["Primary Fur Color"] == "Cinnamon"]))
#
# data_dict = {
#     "Fur Color": ["Gray","Cinnamon", "Black"],
#     "Count":[Gray_squirrel,Cinnamon_squirrel, black_squirrel]
# }
#
# print(data_dict)
# final2= pd.DataFrame(data_dict)
# print(final2)


