import heapsort

class Poker:
    def __init__(self):
        self.Joker_number = 0
        self.card_list = []
        self.max_combination = 0

    def sort_and_unify(self,list_to_sort):
        heapsort.heapsort(list_to_sort, "asc")
        print(list_to_sort)
        self.Joker_number=self.count_jokers(list_to_sort)
        i=0
        while (i < len(list_to_sort)):
            try:
                if (list_to_sort[i] == list_to_sort[i+1]):
                    del list_to_sort[i]
                    i -= 1
            except IndexError:
                break
            i += 1
        if self.Joker_number > 0:
            del list_to_sort[0]
        return list_to_sort

    def count_jokers(self,list_to_check):
        Joker_number = 0
        for i in list_to_check:
            if i == 0:
                Joker_number+=1
            else:
                break
        return Joker_number

    def search_longest_combination(self):
        max_combination = 0

        for j in range(len(self.card_list)):
            left_Jockers= self.Joker_number
            card_value = self.card_list[j]
            combination_number = 1
            i = j
            while True:
                try:
                    if self.card_list[i+1] == card_value + 1:
                        combination_number+=1
                        i+=1
                        card_value+=1
                    else:
                        if left_Jockers > 0:
                            left_Jockers-=1
                            combination_number+=1
                            card_value+=1
                        else:
                            if combination_number > max_combination:
                                max_combination = combination_number
                                break
                            else:
                                break
                except IndexError:
                    if left_Jockers>0:
                        combination_number+= left_Jockers
                    if combination_number > max_combination:
                        max_combination = combination_number
                        break
                    else:
                        break
        print(max_combination)
        self.max_combination = max_combination


if __name__ == '__main__':
    poker = Poker()
    text_file = open("pokerIn.txt", "r")
    poker_In_list = text_file.read().split(" ")
    poker_In_list = list(map(float, poker_In_list))
    poker_In_list = list(map(int, poker_In_list))
    text_file.close()
    poker.card_list = poker.sort_and_unify(poker_In_list)
    print(poker.card_list)
    print(poker.Joker_number)
    poker.search_longest_combination()
    text_file2 = open("pokerOut.txt", "w")
    text_file2.write(f"{poker.max_combination}")
    text_file2.close()

    with open("pokerOut.txt", "w") as f:
        f.write(f"{poker.max_combination}")