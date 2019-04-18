
import pandas as pd


# Write your functions here!
def parse(file_name):
    '''
    This function takes .csv file and return pandas dataframe.
    '''
    return pd.read_csv(file_name, header=0)


def species_count(df):
    '''
    This function returns the number of unique Pokemon
    species (determined by the name attribute) found in the dataset.
    '''
    return len(pd.unique(df.loc[:, 'name']))


def max_level(df):
    '''
    This funciton return the max_level pokemon with its name and level.
    '''
    result = df[df['level'] == max(df['level'])].iloc[0, :]
    return (result['name'], result['level'])


def filter_range(df, min, max):
    '''
    This funciton smallest (inclusive) and largest (exclusive) level value
    and returns a list of Pokemon names having a level within that range
    '''
    return df[(df['level'] >= min) & (df['level'] < max)]['name'].tolist()


def mean_attack_for_type(df, type):
    '''
    This function takes a Pokemon type (string) as an argument
    and that returns the average attack stat for all the Pokemon
    in the dataset with that type.
    '''
    atk = df[df['type'] == type]['atk']
    return atk.mean()


def count_types(df):
    '''
    This function returns a dictionary with keys that are Pokemon
    types and values that are the number of times that type appears
    in the dataset.
    '''
    type_df = df.groupby(by='type').apply(len)
    result = {}
    for type, num in type_df.items():
        result[type] = num
    return result


def highest_stage_per_type(df):
    '''
    This function  dictionary that has keys that are the Pokemon types
    and values that are the highest value of stage column for that type
    of Pokemon.
    '''
    stage_df = df.groupby('type')['stage'].apply(max)
    result = {}
    for type, stage in stage_df.items():
        result[type] = stage
    return result


def mean(values):
    '''
    Return mean
    '''
    return sum(values) / len(values)


def mean_attack_per_type(df):
    '''
    This function return a dictionary that has keys that are
    the Pokemon types and values that are the average attack
    for that Pokemon type.
    '''
    df = df.groupby('type')['atk'].apply(mean)
    result = {}
    for key, value in df.items():
        result[key] = round(value, 2)
    return result
