#%%
from PJdilly.readfile import reader
FILE='./data/sandbox.db'
# %%

        
pd_file=reader.rd_sql(FILE,f"SELECT * FROM 'DF109BFD_Exits' where module='AP1_PLI1ILOT1'")   
pd_file.sort_values('timestamp',inplace=True)
duration=pd_file.timestamp.shift(-1)-pd_file.timestamp
mean_duration=duration.mean()
#for i in range(len(pd_file)-1):
for i in range(10):
    event=reader.rd_sql(FILE,f"SELECT * FROM 'DF109BFD_Events' where module='AP1_PLI1ILOT1' and timestamp_ini>{pd_file.timestamp[i]} and timestamp_end<{pd_file.timestamp[i+1]} ") 
    team=reader.rd_sql(FILE,f"SELECT * FROM 'DF109BFD_Teams' where module='AP1_PLI1ILOT1' and timestamp_ini>{pd_file.timestamp[i]} and timestamp_end<{pd_file.timestamp[i+1]} ") 
    sum_event=event.duration.sum()
    sum_team=team['break'].sum()
    if duration[i]>sum_event+sum_team+mean_duration*2:
        print(f"something maybe wrong for module {'DF109BFD_Exits'} at timestamp of {pd_file.timestamp[i]}" )
    




# %%

# %%
