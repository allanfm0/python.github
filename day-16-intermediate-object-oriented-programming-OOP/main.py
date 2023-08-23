# import another_module
# print(another_module.another_variable)

# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
#
# timmy.shape("turtle")
# timmy.forward(100)
# timmy.color("coral")
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Charmander", "Squitle"])
table.add_column("Type", ["Eletric", "Fire", "Water"])
table.align["Pokemon Name"] = "l"
table.align["Type"] = "l"
print(table)
