import pandas as pd
import numpy as np

train = pd.read_csv('/Users/willzumbolo/PycharmProjects/machinelearning/train.csv')


def avg(col, elem):
    search = train.query('%(column)s == "%(element)s"' % {'column': col, 'element': elem})
    price = []
    price.append(search['SalePrice'])
    price = np.asarray(price)
    numerator = price.sum(axis=1)
    df = pd.DataFrame(price)
    denominator = len(df.columns)
    avg = numerator // denominator
    return elem, avg


def percent(arr):
    x, y = arr.T
    col = y
    largest = np.amax(col, axis=0)
    per = [n / largest for n in col]
    x = x.reshape(len(per), 1)
    np.reshape(per, (len(per), 1))
    per = np.asarray(per)
    print(per.shape)
    ans = np.concatenate((x, per), axis=1)
    return ans

neighborhood_list = []
neighborhoods = train.Neighborhood.unique()
[neighborhood_list.append(avg('Neighborhood', neighborhood_name)) for neighborhood_name in neighborhoods]
neighborhood_list = np.asarray(neighborhood_list, dtype=object)
print(percent(neighborhood_list))

BldgType_list = []
BldgType = train.BldgType.unique()
[BldgType_list.append(avg('BldgType', BldgType_name)) for BldgType_name in BldgType]
BldgType_list = np.asarray(BldgType_list, dtype=object)
print(percent(BldgType_list))

HouseStyle_list = []
HouseStyle = train.HouseStyle.unique()
[HouseStyle_list.append(avg('HouseStyle', HouseStyle_name)) for HouseStyle_name in HouseStyle]
HouseStyle_list = np.asarray(HouseStyle_list, dtype=object)
print(percent(HouseStyle_list))

CentralAir_list = []
CentralAir = train.CentralAir.unique()
[CentralAir_list.append(avg('CentralAir', CentralAir_name)) for CentralAir_name in CentralAir]
CentralAir_list = np.asarray(CentralAir_list, dtype=object)
print(percent(CentralAir_list))

GarageType_list = []
GarageType = train.GarageType.unique()
[GarageType_list.append(avg('GarageType', GarageType_name)) for GarageType_name in GarageType]
GarageType_list = np.asarray(GarageType_list, dtype=object)
print(percent(GarageType_list)

SaleType_list = []
SaleType = train.SaleType.unique()
[SaleType_list.append(avg('SaleType', SaleType_name)) for SaleType_name in SaleType]
SaleType_list = np.asarray(SaleType_list, dtype=object)
print(percent(SaleType_list))

SaleCondition_list = []
SaleCondition = train.SaleCondition.unique()
[SaleCondition_list.append(avg('SaleCondition', SaleCondition_name)) for SaleCondition_name in SaleCondition]
SaleCondition_list = np.asarray(SaleCondition_list, dtype=object)
print(percent(SaleCondition_list))

LotShape_list = []
LotShape = train.LotShape.unique()
[LotShape_list.append(avg('LotShape', LotShape_name)) for LotShape_name in LotShape]
LotShape_list = np.asarray(LotShape_list, dtype=object)
print(percent(LotShape_list))
