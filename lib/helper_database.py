from pandas import DataFrame
import psycopg2
from psycopg2.extras import RealDictCursor
import random

this_host = '54.200.77.93'
this_user = 'postgres'
this_password = 'postgres'
COUNT = 220000
seed = 42


def _con_cur_query(query):
    con = psycopg2.connect(host=this_host,
                           user=this_user,
                           password=this_password)
    cur = con.cursor(cursor_factory=RealDictCursor)    
    cur.execute(query)
    results = DataFrame(cur.fetchall())
    con.close()
    return results


def _generate_random_yodas_string(count, n, seed):
    
    if seed:
        random.seed(seed)
    my_list = random.sample(range(count),n)
    my_string_list = [str(i) for i in my_list]

    return ','.join(my_string_list)

def _generate_table_group(table_group):
    table_groups = {
        'A' : ('madelon_data_1', 'madelon_data_2'),
        'B' : ('madelon_data_3', 'madelon_data_4'),
        'C' : ('madelon_data_5', 'madelon_data_6'),
        'D' : ('madelon_data_7', 'madelon_data_8'),
    }
    return table_groups[table_group]

def make_dataframes(count=COUNT, n=220, seed=None):
    these_yodas = _generate_random_yodas_string(count=count, n=n, seed=seed)
    
    feature_A = _query_tables(these_yodas, 'A')
    feature_B = _query_tables(these_yodas, 'B')
    feature_C = _query_tables(these_yodas, 'C')
    feature_D = _query_tables(these_yodas, 'D')
    target = _query_target_table(these_yodas)

    feature = (feature_A.merge(feature_B, on='yoda')
                        .merge(feature_C, on='yoda')
                        .merge(feature_D, on='yoda'))
    
    target.set_index('yoda', inplace=True)
    feature.set_index('yoda', inplace=True)

    return feature, target

def _query_tables(yodas, table_group):
        
    table_1, table_2 = _generate_table_group(table_group)
    
    query = """
        select * 
        from {} as table_1
        join {} as table_2
        on table_1.yoda = table_2.yoda
        where table_1.yoda in ({});
    """.format(table_1, table_2, yodas)
    
    results = _con_cur_query(query)
    return results


def _query_target_table(yoda):

        
    query = """
        select * 
        from madelon_target
        where yoda in ({});

    """.format(yoda)
    
    target = _con_cur_query(query)
    return target

def query_verification():
   
    query = ("select * from madelon_data_1 limit 1;")
    
    return _con_cur_query(query)

