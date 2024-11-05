import os
import pprint
import json
import sqlite3

PATH_TO_INPUT = "open-api.tools.prettyprint.json"

DATABASE = 'awesome_openapi_tools.sqlite3'
TABLE_NAME = 'openapi_tool' 

def populate_database(dic_tools):
    '''
    The assumption here is that the DATABASE in use
    is one that's been created by table_creator.py
    '''

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            for tool_name, list_of_tools in dic_tools.items():
                #
                if len(list_of_tools) > 1:
                    print(f'''{tool_name} is used more than once, only processing the first''')
                #
                dic_tool = list_of_tools[0]
                #
                columns = ', '.join(dic_tool.keys())
                placeholders = ':'+', :'.join(dic_tool.keys())
                query = f'INSERT INTO {TABLE_NAME} (%s) VALUES (%s)' % (columns, placeholders)
                print(query)
                cursor.execute(query, dic_tool)
                conn.commit()
    except sqlite3.OperationalError as e:
        print(e)



def analyse_json():
    with open(PATH_TO_INPUT, 'r') as file:
        data = file.read()
        parsed_data = json.loads(data)
    #
    dic_schema = {}
    d={}
    i=0
    for elem in parsed_data:
        #Iterate over each attribute so that we end up with a list
        #of all attribute name seen through the JSON and, for each one
        #a list of types seen under that name
        for attribute_name, attribute_value in elem.items():
            if attribute_name not in dic_schema:
                dic_schema[attribute_name] = []
            #
            if elem[attribute_name] is None:
                pass
            else:
                if type(elem[attribute_name]) in dic_schema[attribute_name]:
                    pass
                else:
                    dic_schema[attribute_name].append(type(elem[attribute_name]))
                    if len(dic_schema[attribute_name]) > 1:
                        print(elem)
                        print(attribute_name)
                        breakpoint()
        #
        name_proxy = ""
        if "name" in elem:
            name_proxy = elem['name']
        else:
            name_proxy = os.path.split(elem['github'])[-1]
        #
        if name_proxy in d:
            pass
        else:
            d[name_proxy] = [] 

        d[name_proxy].append(elem)
        #
    return d, dic_schema


def main():
    dict_tools, dict_schema = analyse_json()
    populate_database(dict_tools)
    pprint.pprint(dict_tools)




if __name__ == "__main__":
    main()
