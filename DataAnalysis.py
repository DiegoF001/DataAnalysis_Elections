
class VotesOutcome:

    def __init__(self):
        pass

    def dict_creator(self, csv_file, party):
        dict_to_return = {}
        with open(csv_file, 'r') as data:
            next(data)
            for lines in data:
                lines = lines.strip()
                comm = lines.split(",")
                if len(comm) == 6 and comm[5] == "True" and comm[3] == party:
                    dict_to_return.setdefault(comm[0], [])
                    dict_to_return[comm[0]].append(comm[1:5])
        return dict_to_return

    def top_10_in_both_files( self, party):
        dict_gover = self.dict_creator("governor.csv", party)
        dict_presi = self.dict_creator("president.csv", party)
        trimed_dict = self.check_key_and_remove(dict_gover,dict_presi)
        dict_gover = trimed_dict[0]
        dict_presi = trimed_dict[1]
        self.printer(dict_gover)
        return [dict_gover, dict_presi]

    def top_10_president(self, csv_file , party):
        top_10_dict = self.dict_creator(csv_file, party)
        top_10_dict = self.sorter_by_count(top_10_dict)
        self.printer(top_10_dict, True)
        return top_10_dict

        # Father Function that will call __trimmer, then pass that to __iterator, which will then call __county_dict
    def check_key_and_remove(self, state_gov, state_pres):
        holder = self.__trimmer(state_gov, state_pres)
        holder = self.__iterator(holder[0], holder[1])
        holder[0] = self.__capper(holder[0])
        holder[1] = self.__capper(holder[1])
        return [holder[0], holder[1]]

    def __iterator(self, gov_dict, pres_dict):
        for keys in gov_dict:
            holder = self.__county_dict(gov_dict[keys], pres_dict[keys])
            gov_dict[keys] = holder[0]
            pres_dict[keys] = holder[1]
        return [gov_dict, pres_dict]

    # Function will simply check for intersections in counties for both files, will take values for each state as parameter
    def __county_dict(self, gov_values =[], pres_values=[]):
        gov_temp = {}
        county = ""
        temp1, temp2 = [], []
        # Creating a dictionary with counties as keys and saving their respective index as a value
        for index_of_counties in range(len(gov_values)):
            gov_temp[gov_values[index_of_counties][0]] = index_of_counties
        for index_of_counties in range(len(pres_values)):
            county = pres_values[index_of_counties][0]
            if county in gov_temp.keys():
                temp1.append(gov_values[gov_temp[county]]) # gov_temp[county] = the index in the list of values
                temp2.append(pres_values[index_of_counties])
        return [temp1, temp2]


# Will sort based on # of votes
    def sorter_by_count(self, dict_to_sort):
        by_county = lambda data_fields: int(data_fields[3])
        for keys in dict_to_sort.keys():
            list_to_sort = dict_to_sort[keys]
            list_to_sort.sort(key=by_county, reverse = True)
            dict_to_sort[keys] = list_to_sort
        dict_to_sort = self.__capper(dict_to_sort)

        return dict_to_sort

# Will simply cap the # of values for each state to 10
    def __capper(self, dict_to_cap):
        for keys in dict_to_cap.keys():
            list_to_cap = dict_to_cap[keys]
            if len(list_to_cap) >= 10:
                list_to_cap = list_to_cap[:10]
            dict_to_cap[keys] = list_to_cap
        return dict_to_cap

        # Iterator and __county_dict share inheritance, iterator will simply iterate through each state and pass their values to __county_dict to find intersections
        # of counties

    # The following function will be reused to trim down intersections (States
    def __trimmer(self, gov_dict, pres_dict):
        for keys in pres_dict.copy():
            if keys not in gov_dict.keys():
                pres_dict.pop(keys)
        for keys in gov_dict.copy():
            if keys not in pres_dict.keys():
                gov_dict.pop(keys)
        return [gov_dict, pres_dict]


    # def will simply print the dictionaries
    def printer (self, dict_to_print = {}, if_three_and_4 = bool):
        temp = []
        for keys in dict_to_print.keys():
            temp = dict_to_print[keys]
            print("{}{}".format("\n", keys))
            for i in range(len(temp)):
                if if_three_and_4 is True:
                    print("{}. {}: {}".format(i + 1, temp[i][0], temp[i][3]))
                else:
                    print("{}. {}".format(i+1, temp[i][0]))







