#1
# data = {

# "markers": [

# {

# "name": "Rixos The Palm Dubai",

# "location": [25.1212, 55.1535],

# },

# {

# "name": "Shangri-La Hotel",

# "location": [25.2084, 55.2719]

# },

# {

# "name": "Grand Hyatt",

# "location": [25.2285, 55.3273]

# }

# ]

# }
# class Hotel:

#     def __init__(self,d):
#         self.d = d
        
#     def give_names(self):
#         hotel_names = []
#         for i in self.d['markers']:
#             hotel_names.append(i['name'])
#         return hotel_names

#     def give_dict(self):
#         names = tuple((i['name'] for i in self.d['markers']))
#         location = tuple((i['location'] for i in self.d['markers']))
#         all_data = {
#             'name':names,
#             'location':location
#         }
#         return all_data

#     def add_status_id(self):
#         for i in self.d['markers']:
#             i['status_id'] = 1
#         return 'Sicessfully added!!!'

# sheraton = Hotel(data)

# print(sheraton.give_names())

# print(sheraton.give_dict())

# print(sheraton.add_status_id())



#2
# class Factory:

#     def engine(self):
#         return 'Двигатель создан'
    
#     def bridge(self):
#         return "Ходовая часть создана"

# class Toyota(Factory):
    
#     def wheels(self):
#         return "Колема готовы"

#     def windows(self):
#         return "Окна готовы"

# camry = Toyota()
# print(camry.engine())
# print(camry.bridge())
# print(camry.windows())
# print(camry.wheels())

# l = [camry.engine(),camry.windows(),camry.bridge(),camry.wheels()]



