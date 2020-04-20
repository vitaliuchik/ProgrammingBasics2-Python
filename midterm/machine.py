class TextMachine:

    def __init__(self, pr1, pr2):
        self.pr1 = list(pr1)
        self.pr2 = list(pr2)
        self.texts = [pr1, pr2]
        self.change = 0
        self.price = [self.pr1[1], self.pr2[1]]

    def __str__(self):
        string = "Text Machine:"
        for s in self.texts:

            if self.texts[0] == s:
                string += f"<{s[0]} texts; ₴{str(s[1])[0] + '.' + str(s[1])[1:]} each>"
            else:
                string += f"; <{s[0]} texts; ₴{str(s[1])[0] + '.' + str(s[1])[1:]} each>"
        return string

    def is_empty(self):
        return self.pr1[0] == 0 or self.pr2[0] == 0

    def get_text_count(self):
        return (self.pr1[0], self.pr2[0])

    def still_owe(self):
        return (self.pr1[1], self.pr2[1])

    def insert_money(self, money):
        if money[1] == 'short':
            self.change += money[0]
            self.pr1[1] -= money[0]
            print(self.change)
            if self.pr1[1] > 0: 
                return ("Still owe ₴{}".format(self.pr1[1]/100), self.change)
            elif self.pr1[1] == 0:
                change = self.change
                self.change = 0
                self.pr1[0] -= 1
                self.pr1[1] = self.price[0]
                return ("Got a text!", change)
            else:
                self.pr1[0] -= 1
                change = self.change
                self.change = 0
                self.pr1[1] = self.price[0]
                return ("Got a text!", abs(self.pr1[1]))
        elif money[1] == 'long':
            self.change += money[0]
            self.pr2[1] -= money[0]
            if self.pr2[1] > 0: 
                return ("Still owe ₴{}".format(self.pr2[1]/100), self.change)
            elif self.pr2[1] == 0:
                change = self.change
                self.change = 0
                self.pr2[0] -= 1
                self.pr2[1] = self.price[0]
                return ("Got a text!", change)
            else:
                self.pr2[0] -= 1
                change = self.change
                self.change = 0
                self.pr2[1] = self.price[0]
                return ("Got a text!", abs(self.pr2[1]))


        def __eq__(self, other):
            return self.pr1 == other.pr1 \
                and self.pr2 == other.pr2

        def __ne__(self, other):
            return self.pr1 != other.pr1 or\
                 self.pr2 != other.pr2