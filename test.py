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

neighborhood_list = []
neighborhood_list.append(avg('Neighborhood', 'Blmngtn'))
neighborhood_list.append(avg('Neighborhood', 'Blueste'))
neighborhood_list.append(avg('Neighborhood', 'BrDale'))
neighborhood_list.append(avg('Neighborhood', 'BrkSide'))
neighborhood_list.append(avg('Neighborhood', 'ClearCr'))
neighborhood_list.append(avg('Neighborhood', 'CollgCr'))
neighborhood_list.append(avg('Neighborhood', 'Crawfor'))
neighborhood_list.append(avg('Neighborhood', 'Edwards'))
neighborhood_list.append(avg('Neighborhood', 'Gilbert'))
neighborhood_list.append(avg('Neighborhood', 'IDOTRR'))
neighborhood_list.append(avg('Neighborhood', 'MeadowV'))
neighborhood_list.append(avg('Neighborhood', 'Mitchel'))
neighborhood_list.append(avg('Neighborhood', 'NAmes'))
neighborhood_list.append(avg('Neighborhood', 'NoRidge'))
neighborhood_list.append(avg('Neighborhood', 'NPkVill'))
neighborhood_list.append(avg('Neighborhood', 'NridgHt'))
neighborhood_list.append(avg('Neighborhood', 'NWAmes'))
neighborhood_list.append(avg('Neighborhood', 'OldTown'))
neighborhood_list.append(avg('Neighborhood', 'SWISU'))
neighborhood_list.append(avg('Neighborhood', 'Sawyer'))
neighborhood_list.append(avg('Neighborhood', 'SawyerW'))
neighborhood_list.append(avg('Neighborhood', 'Somerst'))
neighborhood_list.append(avg('Neighborhood', 'StoneBr'))
neighborhood_list.append(avg('Neighborhood', 'Timber'))
neighborhood_list.append(avg('Neighborhood', 'Veenker'))

rank = (np.asarray(neighborhood_list, dtype=object))

BldgType_list = []
BldgType_list.append(avg('BldgType', '1Fam'))
BldgType_list.append(avg('BldgType', '2fmCon'))
BldgType_list.append(avg('BldgType', 'Duplex'))
BldgType_list.append(avg('BldgType', 'TwnhsE'))
BldgType_list.append(avg('BldgType', 'Twnhs'))

BldgType = np.asarray(BldgType_list, dtype=object)

HouseStyle_list = []
HouseStyle_list.append(avg('HouseStyle', '1Story'))
HouseStyle_list.append(avg('HouseStyle', '1.5Fin'))
HouseStyle_list.append(avg('HouseStyle', '1.5Unf'))
HouseStyle_list.append(avg('HouseStyle', '2Story'))
HouseStyle_list.append(avg('HouseStyle', '2.5Fin'))
HouseStyle_list.append(avg('HouseStyle', '2.5Unf'))
HouseStyle_list.append(avg('HouseStyle', 'SFoyer'))
HouseStyle_list.append(avg('HouseStyle', 'SLvl'))

HouseStyle = np.asarray(HouseStyle_list, dtype=object)

CentralAir_list = []
CentralAir_list.append(avg('CentralAir', 'Y'))
CentralAir_list.append(avg('CentralAir', 'N'))

CentralAir = np.asarray(CentralAir_list, dtype=object)

GarageType_list = []
GarageType_list.append(avg('GarageType', '2Types'))
GarageType_list.append(avg('GarageType', 'Attchd'))
GarageType_list.append(avg('GarageType', 'Basment'))
GarageType_list.append(avg('GarageType', 'BuiltIn'))
GarageType_list.append(avg('GarageType', 'CarPort'))
GarageType_list.append(avg('GarageType', 'Detchd'))

GarageType = np.asarray(GarageType_list, dtype=object)

SaleType_list = []
SaleType_list.append(avg('SaleType', 'WD'))
SaleType_list.append(avg('SaleType', 'CWD'))
SaleType_list.append(avg('SaleType', 'VWD'))
SaleType_list.append(avg('SaleType', 'New'))
SaleType_list.append(avg('SaleType', 'COD'))
SaleType_list.append(avg('SaleType', 'Con'))
SaleType_list.append(avg('SaleType', 'ConLw'))
SaleType_list.append(avg('SaleType', 'ConLI'))
SaleType_list.append(avg('SaleType', 'ConLD'))
SaleType_list.append(avg('SaleType', 'Oth'))

SaleType = np.asarray(SaleType_list, dtype=object)

SaleCondition_list = []
SaleCondition_list.append(avg('SaleCondition', 'Normal'))
SaleCondition_list.append(avg('SaleCondition', 'Abnorml'))
SaleCondition_list.append(avg('SaleCondition', 'AdjLand'))
SaleCondition_list.append(avg('SaleCondition', 'Alloca'))
SaleCondition_list.append(avg('SaleCondition', 'Family'))
SaleCondition_list.append(avg('SaleCondition', 'Partial'))

SaleCondition = np.asarray(SaleCondition_list, dtype=object)

LotShape_list = []
LotShape_list.append(avg('LotShape', 'Reg'))
LotShape_list.append(avg('LotShape', 'IR1'))
LotShape_list.append(avg('LotShape', 'IR2'))
LotShape_list.append(avg('LotShape', 'IR3'))

LotShape = np.asarray(LotShape_list, dtype=object)
