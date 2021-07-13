import pandas as pd
import numpy as np

train = pd.read_csv('/Users/willzumbolo/PycharmProjects/machinelearning/train.csv')


def avg(col, elem):
    elem = train.query('%(column)s == %(element)s' %{'column': col, 'element': elem})
    price = []
    price.append(elem['SalePrice'])
    price = np.asarray(price)
    numerator = price.sum(axis=1)
    df = pd.DataFrame(price)
    denominator = len(df.columns)
    avg = numerator // denominator
    print(str(elem), avg)


print(avg('Neighborhood', 'Blmngtn'))
