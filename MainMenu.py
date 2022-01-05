from DataAnalysis import VotesOutcome


class MainMenu:

    def __init__(self):
        pass

    def option_number(self):
        options = "\n************************************************************************************" + \
                  "\n****************** U.S Elections 2020 Data (Last update Dec 2020) ******************" + \
                  "\n************************************************************************************\n\n" \
                  "[1] For every state, display democratic counties that won both presidential and governors ordered " \
                  "by name of county in ascending order\n" \
                  "[2] For every state, display republican counties that won both presidential and governors ordered " \
                  "by name of county in ascending order\n" \
                  "Presidential Elections options\n" \
                  "[3] For every state, display top 10 democratic counties ordered by count in descending order\n" \
                  "[4] For every state, display top 10 republican counties ordered by count in descending order\n" \
                  "Governor Election options\n" \
                  "[5] For every state, display top 10 republican counties ordered by count in descending order\n" \
                  "[6] For every state, display top 10 republican counties ordered by count in descending order\n" \
                  "[7] To exit!\n"
        print(options)
        number = input("Please choose an option: ")

        default = "Please enter a number between 1 and 6"
        return getattr(self, 'case_' + number, lambda: default)()

    def case_1(self):
        VotesOutcome().top_10_in_both_files("DEM")

    def case_2(self):
        VotesOutcome().top_10_in_both_files("REP")

    def case_3(self):
        VotesOutcome().top_10_president("president.csv", "DEM")

    def case_4(self):
        VotesOutcome().top_10_president("president.csv", "REP")

    def case_5(self):
        VotesOutcome().top_10_president("governor.csv", "DEM")

    def case_6(self):
        VotesOutcome().top_10_president("governor.csv", "REP")

    def case_7(self):
        return 7
