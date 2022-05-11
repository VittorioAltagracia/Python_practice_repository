class language:
    def __init__(self, name, coolness, parola_preferita):
        self.name = name
        self.num_of_speakers = 60000000
        self.coolness = coolness
        self.parola_preferita = parola_preferita

    def tempo(self):
        test1 = (input("Da quando impari questa lingua?: "))
        # this function asks us since when we are learning this language

        try:
            ftest1 = float(test1)
        except:
            print("Error, please enter numeric input")
            quit()
        # if user enters something other than integer or float
        # error message will be displayed and program will QUIT

class Italiano(language):
    def __init__(self, name):
        super(Italiano, self).__init__(name, coolness="it depends"
                    " on your perception and preferences", parola_preferita="Spacciatore")

# figo means cool in Italian, the value returned by this
# tells us how cool this specific language is

    def figo(self):

        print("Too cool to be true")

    def alfabeto(self):

        print("latino")


italiano = Italiano("Italiano")
print(italiano.name)
italiano.tempo()
italiano.alfabeto()
italiano.figo()
print(italiano.num_of_speakers)
print(italiano.coolness)
print(italiano.parola_preferita)


class Deutsch(language):
    def __init__(self, name):
        super(Deutsch, self).__init__(name, coolness="richtig Geil!", parola_preferita="Scheiße")

    def Zeit(self):
        test2 = (input("Seit wann lerst du Deutsch?: "))

        try:
            ftest2 = float(test2)
        except:
            print("Du sprichst gar kein Deutsch, Alter")
            quit()

    def dialects(self):
        print("German has too many dialects")


deutsch = Deutsch("Deutsch")
print(deutsch.name)
deutsch.Zeit()
print(deutsch.coolness)
print(deutsch.parola_preferita)
print(deutsch.num_of_speakers)
deutsch.dialects()