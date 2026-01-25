from scraper import *
from data_preparation import *

# urls
# Johannesburg = 'https://www.property24.com/for-sale/johannesburg/gauteng/100/p{i}'

# estimate: 93_560
Gauteng = 'https://www.property24.com/for-sale/gauteng/1/p{i}?PropertyCategory=House%2cApartmentOrFlat%2cTownhouse'
# estimates: 8_975
Eastern_Cape = 'https://www.property24.com/for-sale/eastern-cape/7/p{i}?PropertyCategory=House%2cApartmentOrFlat%2cTownhouse'
# estimated: 7_613
Free_State = 'https://www.property24.com/for-sale/free-state/3/p{i}?PropertyCategory=House%2cApartmentOrFlat%2cTownhouse'
# estimated: 31_102
KZN = 'https://www.property24.com/for-sale/kwazulu-natal/2/p{i}?PropertyCategory=House%2cApartmentOrFlat%2cTownhouse'
# estimated: 4_153
Limpopo = 'https://www.property24.com/for-sale/limpopo/14/p{i}?PropertyCategory=House%2cApartmentOrFlat%2cTownhouse'
# estimated: 7_918
Mpumalanga = 'https://www.property24.com/for-sale/mpumalanga/5/p{i}?PropertyCategory=House%2cApartmentOrFlat%2cTownhouse'
# estimated: 10_937
North_West = 'https://www.property24.com/for-sale/north-west/6/p{i}?PropertyCategory=House%2cApartmentOrFlat%2cTownhouse'
# estimated: 2_291
Northern_Cape = 'https://www.property24.com/for-sale/northern-cape/8/p{i}?PropertyCategory=House%2cApartmentOrFlat%2cTownhouse'
# estimated: 20_325
Western_Cape = 'https://www.property24.com/for-sale/western-cape/9/p{i}?PropertyCategory=House%2cApartmentOrFlat%2cTownhouse'

# last pages
g_lp = 4679
ec_lp = 449
fs_lp = 381
kzn_lp = 1566
lp_lp = 208
mp_lp = 399
nw_lp = 547
nc_lp = 115
wc_lp = 1017

# # gauteng
# gau = DataCollector(Gauteng, 1, g_lp).collect_data()
# preparator = DataPreparator(gau)
# preparator.save_to_csv('Gauteng_property_data.csv')

# # eastern cape
# ec = DataCollector(Eastern_Cape, 1, ec_lp).collect_data()
# preparator = DataPreparator(ec)
# preparator.save_to_csv('Eastern_Cape_property_data.csv')

# # free state
# fs = DataCollector(Free_State, 1, fs_lp).collect_data()
# preparator = DataPreparator(fs)
# preparator.save_to_csv('Free_State_property_data.csv')

# # kzn
# kzn = DataCollector(KZN, 1, kzn_lp).collect_data()
# preparator = DataPreparator(kzn)
# preparator.save_to_csv('KZN_property_data.csv')

# # limpopo
# lp = DataCollector(Limpopo, 1, lp_lp).collect_data()
# preparator = DataPreparator(lp)
# preparator.save_to_csv('Limpopo_property_data.csv')

# # mpumalanga
# mp = DataCollector(Mpumalanga, 1, mp_lp).collect_data()
# preparator = DataPreparator(mp)
# preparator.save_to_csv('Mpumalanga_property_data.csv')

# # north west
# nw = DataCollector(North_West, 1, nw_lp).collect_data()
# preparator = DataPreparator(nw)
# preparator.save_to_csv('North_West_property_data.csv')

# # northern cape
# nc = DataCollector(Northern_Cape, 1, nc_lp).collect_data()
# preparator = DataPreparator(nc)
# preparator.save_to_csv('Northern_Cape_property_data.csv')

# # western cape
# wc = DataCollector(Western_Cape, 1, wc_lp).collect_data()
# preparator = DataPreparator(wc)
# preparator.save_to_csv('Western_Cape_property_data.csv')