TvProgrammes = ["The a show", "The b race", "The c cooking show ", " The d news"]

show = input("Enter a new show: ")
position = int(input("Choose a position: "))

TvProgrammes.insert(position, show)
print(TvProgrammes)
