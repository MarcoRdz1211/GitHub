def Calc_mean(data):
    data_sum = 0
    count = 0

    for i in range(len(data)):
        data_sum += data[i]
        count += 1

    prom = data_sum/count
    print("El promedio de los datos {} es: \n {:.3f}".format(data,prom))

data=[1,2,456,1,745,145,1532,1,51]
Calc_mean(data)


def prom(data):
    data_sum = 0

    for i in data:
        data_sum += i

    prom = data_sum/len(data)
    print("El promedio de los datos {} es: \n {:.3f}".format(data,prom))


data=[1,2,456,1,745,145,1532,1,51]
Calc_mean(data)
