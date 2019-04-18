

def parse(file_name, int_cols):
    """
    Parses the CSV file specified by file_name and returns the data as a list
    of dictionaries where each row is represented by a dictionary that
    has keys for each column and value which is the entry for that column
    at that row.

    Also takes a list of column names that should have the data for that column
    converted to integers. All other data will be str.
    """
    data = []
    with open(file_name) as f:
        headers = f.readline().strip().split(',')
        num_cols = len(headers)

        for line in f.readlines():
            row_data = line.strip().split(',')
            row = {}
            for i in range(num_cols):
                if headers[i] in int_cols:
                    row[headers[i]] = int(row_data[i])
                else:
                    row[headers[i]] = row_data[i]
            data.append(row)
    return data


# Write your solutions here!
def species_count(data):
    '''
    This function returns the number of unique Pokemon
    species (determined by the name attribute) found in the dataset.
    '''
    result = set()
    for i in data:
        result.add(i['name'])
    return len(result)


def max_level(data):
    '''
    This funciton return the max_level pokemon with its name and level.
    '''
    level = 0
    name = ''
    for i in data:
        if i['level'] > level:
            level = i['level']
            name = i['name']
    return (name, level)


def filter_range(data, min, max):
    '''
    This funciton smallest (inclusive) and largest (exclusive) level value
    and returns a list of Pokemon names having a level within that range
    '''
    result = []
    for i in data:
        if i['level'] in range(min, max):
            result.append(i['name'])
    return result


def mean_attack_for_type(data, p_type):
    '''
    This function takes a Pokemon type (string) as an argument
    and that returns the average attack stat for all the Pokemon
    in the dataset with that type.
    '''
    total = 0
    count = 0
    for i in data:
        if i['type'] == p_type:
            total += i['atk']
            count += 1
    return total / count


def count_types(data):
    '''
    This function returns a dictionary with keys that are Pokemon
    types and values that are the number of times that type appears
    in the dataset.
    '''
    result = {}
    for i in data:
        p_type = i['type']
        if p_type in result.keys():
            result[p_type] += 1
        else:
            result[p_type] = 1
    return result


def highest_stage_per_type(data):
    '''
    This function  dictionary that has keys that are the Pokemon types
    and values that are the highest value of stage column for that type
    of Pokemon.
    '''
    result = {}
    for i in data:
        p_type = i['type']
        if p_type in result.keys():
            if result[p_type] < i['stage']:
                result[p_type] = i['stage']
        else:
            result[p_type] = i['stage']
    return result


def mean(values):
    '''
    Take list like datastructure and return its mean.
    '''
    return sum(values) / len(values)


def mean_attack_per_type(data):
    '''
    This function return a dictionary that has keys that are
    the Pokemon types and values that are the average attack
    for that Pokemon type.
    '''
    result = {}
    for i in data:
        p_type = i['type']
        if p_type in result.keys():
            result[p_type].append(i['atk'])
        else:
            result[p_type] = [i['atk']]
    result_mean = {k: round(mean(v), 2) for k, v in result.items()}
    return result_mean
