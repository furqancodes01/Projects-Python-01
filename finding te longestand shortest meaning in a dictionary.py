dict_1 = {'piece':'portion of an object or of material , producing by cutting',
         'patch':'a piece of cloth or other material used to mend or strengthn a torn or wek point',
         'area':'a region or part of a town , a country , or the world',
         'visit':'gp to see and spend time with(someone)',
         'with':'having or possessing',
          'small':'less than normal'} 

keys = list(dict_1.keys())
values = list(dict_1.values())
lens = [len(x) for x in values]

max_lens = max(lens)
min_lens = min(lens)

max_index = lens.index(max_lens)
min_index = lens.index(min_lens)

print("Max",keys[max_index],values[max_index])
print("Min",keys[min_index],values[min_index])