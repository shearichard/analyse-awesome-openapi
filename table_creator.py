import os
import pprint
import json
import sqlite3

def main():
    '''
{'archived': [<class 'bool'>],
 'category': [<class 'str'>],
 'demo': [<class 'str'>],
 'demoText': [<class 'str'>],
 'description': [<class 'str'>],
 'documentation': [<class 'str'>],
 'downloadStr': [<class 'str'>],
 'downloads': [<class 'int'>],
 'forks': [<class 'int'>],
 'github': [<class 'str'>],
 'issues': [<class 'int'>],
 'language': [<class 'str'>],
 'license': [<class 'str'>],
 'link': [<class 'str'>],
 'logo': [<class 'str'>],
 'name': [<class 'str'>],
 'owner': [<class 'str'>],
 'stars': [<class 'int'>],
 'unsure': [<class 'bool'>],
 'updated': [<class 'str'>],
 'uuid': [<class 'str'>],
 'v1': [<class 'bool'>],
 'v2': [<class 'bool'>],
 'v3': [<class 'bool'>],
 'v3_progress_link': [<class 'str'>],
 'watch': [<class 'int'>]}
    '''

database = 'awesome_openapi_tools.sqlite3'
create_table = ''' 
    CREATE TABLE IF NOT EXISTS openapi_tool (
            id INTEGER PRIMARY KEY, 
			archived INTEGER,
			category TEXT,
			demo TEXT,
			demoText TEXT,
			description TEXT,
			documentation TEXT,
			downloadStr TEXT,
			downloads INTEGER,
			forks INTEGER,
			github TEXT,
			issues INTEGER,
			language TEXT,
			license TEXT,
			link TEXT,
			logo TEXT,
			name TEXT,
			owner TEXT,
			stars INTEGER,
			unsure INTEGER,
			updated TEXT,
			uuid TEXT,
			v1 INTEGER,
			v2 INTEGER,
			v3 INTEGER,
			v3_progress_link TEXT,
			watch INTEGER)
'''

try:
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute(create_table)   
        conn.commit()

except sqlite3.OperationalError as e:
    print(e)





if __name__ == "__main__":
    main()
