import dropbox
d = dropbox.Dropbox(
    "Q1mV76AIRhIAAAAAAABG356f2z2RQX_7mgd7OQ92Jbtny8DfoI-XlyZelSEuKf88")
data = d.files_list_folder(path="/csv_bags")
for item in data.entries:
        _, res = d.files_download(
            path="/csv_bags/"+item.name+"/current_ticker_info.csv")
        f = open(item.name)
        f.write(res.content)
        f.close()