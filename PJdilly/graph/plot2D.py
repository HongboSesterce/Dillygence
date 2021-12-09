#%%
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation, writers
import matplotlib.pyplot as plt
import matplotlib.patches as pts
from PJdilly.readfile import reader
import matplotlib.patches as mpatches
def plot_items(file):
    yaml_data =reader.rdyaml(file)
    objs=yaml_data.items()
    #position_op=[1400, 1400]
    fig, ax=plt.subplots(figsize=(14, 10.5))
    ax.set_xlim(-10,3000)
    ax.set_ylim(-10,1500)
    fig.suptitle('Plan2D', fontsize=20)
    plt.xlabel('x(m)', fontsize=18)
    plt.ylabel('y(m)', fontsize=16)
    for item_name, properties in objs:
        display=properties['display']
        key=properties['key']
        position=properties['position']
        type=properties['type']
        if type=='module':
            rect=pts.Rectangle(tuple(position), 80, 30,color='orange')
        elif type=='artifact':
            rect=pts.Rectangle(tuple(position), 80, 30,color='g')
        elif type=='buffer':
            rect=pts.Rectangle(tuple(position), 80, 30,color='pink')
        else:
          #  position=position_op
          #  position_op[0]+=100
          #  reader.set_position(file,item_name, position)
            rect=pts.Rectangle(tuple(position), 80, 30,color='grey')      
        ax.text(position[0], position[1]+10, item_name, fontsize=5)
        ax.add_patch(rect)
        if type=='artifact' or type=='buffer':
            upstream=properties['upstream']
            downstream=properties['downstream']
            up_stream_position=yaml_data[upstream]['position']
            down_stream_position=yaml_data[downstream]['position']
            
            arrow = mpatches.FancyArrowPatch(tuple(up_stream_position), tuple(position),
                                 mutation_scale=8,color='blue')
            ax.add_patch(arrow)
            arrow = mpatches.FancyArrowPatch(tuple(position), tuple(down_stream_position),
                                 mutation_scale=8, color='blue')
            ax.add_patch(arrow)   
       #legend
        rect=pts.Rectangle(tuple([2800, 1400]), 150, 50,color='orange')
        ax.add_patch(rect)
        ax.text(2800+20, 1400+20, 'module', fontsize=10)
        
        rect=pts.Rectangle(tuple([2800, 1350]), 150, 50,color='g')
        ax.add_patch(rect)
        ax.text(2800+20, 1350+20, 'artifact', fontsize=10)

        rect=pts.Rectangle(tuple([2800, 1300]), 150, 50,color='pink')
        ax.add_patch(rect)
        ax.text(2800+20, 1300+20, 'buffer', fontsize=10)

        rect=pts.Rectangle(tuple([2800, 1250]), 150, 50,color='grey')
        ax.add_patch(rect)
        ax.text(2800+20, 1250+20, 'operator', fontsize=10)
        

    plt.show()




# %%
