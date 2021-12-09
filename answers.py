#%%
from PJdilly.readfile import reader
from PJdilly.graph import plot2D
import yaml

yaml_data =reader.rdyaml('./data/graph.yaml')
# %%

with open('./data/graph.yaml') as f:
    doc=yaml.safe_load(f)

#%%
def set_position(file, operator, position):
    with open(file) as f:
        doc = yaml.safe_load(f)
    doc[operator]['position']= position
    with open(file, 'w') as f:
        yaml.safe_dump(doc, f, default_flow_style=False)
# %%
set_position('./data/graph.yaml', 'OP_AP3', [100,100])
# %%
