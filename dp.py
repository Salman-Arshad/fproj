# import dropbox
# import jsonpickle
# d = dropbox.Dropbox("Q1mV76AIRhIAAAAAAABG356f2z2RQX_7mgd7OQ92Jbtny8DfoI-XlyZelSEuKf88")
# data = d.files_list_folder(path="/csv_bags")
# item = data.entries[0]
# print(item.name)
# #print(jsonpickle.encode(item))



from datetime import datetime
a=datetime.strptime("06-28-2018","%M-%d-%Y").date()
b=datetime.strptime("06-27-2019","%M-%d-%Y").date()
print(a-b)