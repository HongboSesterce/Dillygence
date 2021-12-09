# Add parent dir
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from readfile import reader


    
def MTTR(FILE,module):
    print(f"MTTR of module='{module}' from 'DF109BFD_Exits'")
    pd_file=reader.rd_sql(FILE,f"SELECT * FROM 'DF109BFD_Events' where module='{module}'")
    return pd_file.duration.mean()

def MTTF(FILE,module):
    print(f"MTTF of module='{module}' from 'DF109BFD_Exits' and 'DF109BFD_Events'")
    pd_file_exit=reader.rd_sql(FILE,f"SELECT * FROM 'DF109BFD_Exits' where module='{module}'")
    num_product=len(pd_file_exit)-1
    pd_file_exit.sort_values('timestamp',inplace=True)
    duration=pd_file_exit.timestamp.shift(-1)-pd_file_exit.timestamp
    circle=duration.mean()
    pd_file_event=reader.rd_sql(FILE,f"SELECT * FROM 'DF109BFD_Events' where module='{module}'")
    num_event=len(pd_file_event)
    return (circle*num_product)/(num_event-1)
    
def circle(FILE,type,module):
    if type=='buffer':
        print(f"Circle of time of module='{module}' from 'DF109BFD_Buffers'")
        pd_file=reader.rd_sql(FILE,f"SELECT * FROM 'DF109BFD_Buffers' where module='{module}'")
    else:
        print(f"Circle of time of module='{module}' from 'DF109BFD_Exits'")
        pd_file=reader.rd_sql(FILE,f"SELECT * FROM 'DF109BFD_Exits' where module='{module}'")
        
    pd_file.sort_values('timestamp',inplace=True)
    duration=pd_file.timestamp.shift(-1)-pd_file.timestamp
    return duration.mean()

def Anomaly(FILE,module,weight):       
    pd_file=reader.rd_sql(FILE,f"SELECT * FROM 'DF109BFD_Exits' where module='{module}'")   
    pd_file.sort_values('timestamp',inplace=True)
    duration=pd_file.timestamp.shift(-1)-pd_file.timestamp
    mean_duration=duration.mean()
    #for i in range(len(pd_file)-1):
    for i in range(len(pd_file)-1):
        event=reader.rd_sql(FILE,f"SELECT * FROM 'DF109BFD_Events' where module='{module}' and timestamp_ini>{pd_file.timestamp[i]} and timestamp_end<{pd_file.timestamp[i+1]} ") 
        team=reader.rd_sql(FILE,f"SELECT * FROM 'DF109BFD_Teams' where module='AP1_PLI1ILOT1' and timestamp_ini>{pd_file.timestamp[i]} and timestamp_end<{pd_file.timestamp[i+1]} ") 
        sum_event=event.duration.sum()
        sum_team=team['break'].sum()
        if duration[i]>sum_event+sum_team+mean_duration*weight:
            print(f"something maybe wrong for module '{module}'' at timestamp of {pd_file.timestamp[i]}" )


# %%
