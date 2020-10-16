"""
##Implement a group_by_owners function that:

Accepts a dictionary containing the file owner name for each file name.
Returns a dictionary containing a list of file names for each owner name, in any order.
For example, for dictionary {'Input.txt': 'Randy',
                            'Code.py': 'Stan',
                            'Output.txt': 'Randy'}
the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'],
                                            'Stan': ['Code.py']}.

"""

def group_by_owners(files):
    result = {} #new dictionary
    for key,value in files.items():
        if value in result.keys():
            data = result.get(value)
            data.append(key)
        else:
            result[value] = [key]
    return result



files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}

print(group_by_owners(files))
