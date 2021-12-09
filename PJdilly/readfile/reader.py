#%%
import yaml
import sqlite3
import pandas as pd

def rdyaml(file):
    """
    
    file is the location and name of the yaml file
    Input:
    yaml file
    OUT:
    dict
    >yamldata=rdyaml('./data/graph.yaml')
    
    """
    yaml_file=open(file)
    yaml_data=yaml.load(yaml_file, Loader=yaml.FullLoader)
    #module=yaml_data.get('AP1_ARMA1')
    return yaml_data

def set_position(file, operator, position):
    """
    add a position to a operator type, whitch will make it easier to draw a graph.
    file yaml file
    operator name> string
    positon      > list

    """
    
    with open(file) as f:
        doc = yaml.safe_load(f)
    doc[operator]['position']= position
    with open(file, 'w') as f:
        yaml.safe_dump(doc, f, default_flow_style=False)
# %%
def rd_sql(file,command):
    con=sqlite3.connect(file)
    cur=con.cursor()
    table=pd.read_sql_query(command, con)
    return table
