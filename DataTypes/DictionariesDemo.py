'''
Dictionary ==>
Example => s = {Key1: Value1, Key1: Value1,...}
1) Insertion order NOT preserved
2) Duplicates are NOT Allowed
3) Represent {Key1: Value1,}
4) Slicing & Indexing NOT Allowed
5) Mutable - Can be updated
6) Heterogeneous Elements Allowed
'''

d = {'k1':'Value1','k2':'Value2','k3':'Value3','k4':[1,2,3],'k5':{'inside1':'InsideValue1','inside2':'InsideValue2'}}

print(d['k1'])
print(d['k4'])
print(d['k5'])

all_dictionary_keys = d.keys()
all_dictionary_values = d.values()
print(all_dictionary_keys)
print(all_dictionary_values)

all_dictionary_items = d.items()
print(all_dictionary_items)

d['new_key'] = 'new_item'
print(d)

d.pop('new_key')
print(d)

