class average:
    def __init__(self,data):
        self.data = data

    def calc_average(self):
        data = self.data
        if len(self.data)!=0:
            print("The average of the data is: {:.2f}".format(sum(data)/len(data)))

        else:
            print("The average of the data is: 0")
