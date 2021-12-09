#%% draw graph
from PJdilly.readfile import reader
from PJdilly.graph import plot2D 
from PJdilly.time import calc_time 
YAML_FILE='./data/graph.yaml'
DB_FILE='./data/sandbox.db'
#%%
plot2D.plot_items(YAML_FILE)

# %%
calc_time.circle(DB_FILE,'module','AP1_PLI1ILOT1')
#%%
calc_time.circle(DB_FILE,'buffer','AP4_PLTFTAC0432_F')
# %%
calc_time.MTTR(DB_FILE,'AP1_PLI1ILOT1')
#%%
calc_time.MTTF(DB_FILE,'AP1_PLI1ILOT1')
# %%

calc_time.Anomaly(DB_FILE,'AP1_PLI1ILOT1',weight=2)


# %%
