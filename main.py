#%% The PJdilly packages has three part, 
# readfile is for reading yaml and sqlite3 files
# graph is to draw a 2D plan of the factory
# time is to calculate all the times and detect anomalies .

from PJdilly.readfile import reader
from PJdilly.graph import plot2D 
from PJdilly.time import calc_time 
YAML_FILE='./data/graph.yaml'
DB_FILE='./data/sandbox.db'
#%% This part plot a 2D plan of the factory, different colors represent different module
plot2D.plot_items(YAML_FILE)

# %%
# This part calculte circle of time,  I select all the data from 'DF109BFD_Exits' Table, sort them by time, 
# Then I think the duration of the machine is the difference between two timestamps, finally I take the mean value of that duration
calc_time.circle(DB_FILE,'module','AP1_PLI1ILOT1')
#%%
# This function is doing the same thing ,but it is using 'DF109BFD_Buffers' table for buffers
calc_time.circle(DB_FILE,'buffer','AP4_PLTFTAC0432_F')
# %%
# This function take the mean duration of all events for selected module.
calc_time.MTTR(DB_FILE,'AP1_PLI1ILOT1')
#%
# This function calculte the MTTF by  (temps de cycle * nombre de pièces produites) / (nombre d'événements bloquants - 1)
# time of circle is using the function above, number of product is the length of the timestamps-1
calc_time.MTTF(DB_FILE,'AP1_PLI1ILOT1')
# %%
# This function detects anomalies, which is totally my thoughts, so maybe wrong..
# 1. First it calculate the circle of time for a module(mean value)
# 2. Next for a module it takes two timestamps, and calculate the duration.
# 3. Next, the function search 'DF109BFD_Events' and 'DF109BFD_Teams' table between these two timestamps
# and caculate the totol duration of events and teams.
# if the duration of step 3 is > (the time for events and teams + weight* circle time) then I think there is something wrong

calc_time.Anomaly(DB_FILE,'AP1_PLI1ILOT1',weight=5)


# %%
