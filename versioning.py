database = {}
version = 1


def get_version(key, _version):
    """
    :param key: key that is being searched.
    :param _version: the version of the value for a particular key that user wants.
    :return: a dictionary of key, value and version i.e, {'key': 1, 'value': 1, 'version': 2}
    This function returns the user requested version of the value for the provided key.
    if the version is not available it returns the nearest version available.
    if the key is not available, it returns {'key': 'key5', 'value': '<NULL>', 'version': 'Not Available'}
    Ex: if version 3 is requested and 3 is not available it will return 2 if exists or 1 if exists.
    """
    if database.get(key) is not None:
        value = sorted(database.get(key).items(), key=lambda x: (x[0], x[1]), reverse=True)
        if _version in database.get(key).keys():
            return {'key': key, 'value': database.get(key)[_version], 'version': _version}
        else:
            for i in value:
                if _version > i[0]:
                    return {'key': key, 'value': i[1], 'version': i[0]}
                if i == value[-1]:
                    return {'key': key, 'value': "<NULL>", 'version': "Not Available"}
    else:
        print("No Key present in database")


def get(key):
    """
    :param key: key for which we are searching for in the dictionary.
    :return: returns the latest version of the value for the requested key.
    If key is not available, it returns {'key': 'key2', 'value': '<NULL>', 'version': 'Not Available'}
    """
    if database.get(key) is not None:
        value = sorted(database.get(key).items(), key=lambda x: (x[0], x[1]), reverse=True)
        return {'key': key, 'value': value[0][1], 'version': value[0][0]}
    else:
        return {'key': key, 'value': "<NULL>", 'version': "Not Available"}


def put(key, value):
    """
    :param key: key of the pair that we are trying to insert.
    :param value: value for the key that we are trying to insert.
    :return: does not returns anything.
    """
    global version
    existing_value = database.get(key)
    if existing_value is None:
        database[key] = {version: value}
    else:
        existing_value[version] = value
        database[key] = existing_value
    version += 1


put('key1', 5)
put('key2', 6)
print(get('key1'))
print(get_version('key1', 1))
print(get_version('key2', 2))
put('key1', 7)
print(get_version('key1', 1))
print(get_version('key1', 2))
print(get_version('key1', 3))
print(get('key4'))
print(get_version('key1', 4))
print(get_version('key2', 1))
