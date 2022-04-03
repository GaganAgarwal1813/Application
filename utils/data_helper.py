import json

def get_last_index():
    #open data.json
    f = open('data.json', 'r')
    data = json.load(f)
    last_index = data['last-index']
    f.close()
    #update last-index
    last_index += 1
    #save data.json
    f = open('data.json', 'w')
    data['last-index'] = last_index
    json.dump(data, f)
    f.close()
    return last_index

    