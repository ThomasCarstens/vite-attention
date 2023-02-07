import plotly.express as px
import pandas as pd
import numpy as np


# SHOULD HAVE DROPPED THIS: ANIMATES TWO DIFFERENT, ONE AFTER THE OTHER.


dfa = pd.DataFrame({
    "Frames": range(100),
    # "Vals": [np.random.randn(1000) for _ in range(100)],
    "Vals": np.linspace(0, 15, 100),
    
})
# print(len([1 for _ in range(100)]))
# d = {'increasing': [np.linspace(0, 15, 100), np.linspace(0, 15, 100)] 'names': ['a', 'b']}

# df = pd.DataFrame(d, dtype="category")

max_val = 100
print(len(range(max_val*2)), len(['Manually' for _ in range(max_val)] + ['Digitally' for _ in range(max_val)]), len(np.hstack((np.linspace(0, 15, max_val), np.linspace(0, 10, max_val)))))

M_timeA = 15
M_timeB = 65
M_timeC = 80
M_timeD = 120

D_timeA = 15
D_timeB = 45
D_timeC = 70
D_timeD = 75


dataA = {'Frames': np.hstack((range(max_val), range(max_val))),  
        'Name': ['No app' for _ in range(max_val)] + ['With app' for _ in range(max_val)], 
        'Values': np.hstack((np.linspace(0, M_timeA, max_val), np.linspace(0, D_timeA, max_val)))    
        }

dataB = {'Frames': np.hstack((range(max_val), range(max_val))),  
        'Name': ['No app' for _ in range(max_val)] + ['With app' for _ in range(max_val)], 
        'Values': np.hstack((np.linspace(M_timeA, M_timeB, max_val), np.linspace(D_timeA, D_timeB, max_val)))    
        }

dataC = {'Frames': np.hstack((range(max_val), range(max_val))),  
        'Name': ['No app' for _ in range(max_val)] + ['With app' for _ in range(max_val)], 
        'Values': np.hstack((np.linspace(M_timeB, M_timeC, max_val), np.linspace(D_timeB, D_timeC, max_val)))    
        }
dataD = {'Frames': np.hstack((range(max_val), range(max_val))),  
        'Name': ['No app' for _ in range(max_val)] + ['With app' for _ in range(max_val)], 
        'Values': np.hstack((np.linspace(M_timeC, M_timeD, max_val), np.linspace(D_timeC, D_timeD, max_val)))    
        }

# data= dataA
# data = dataB
# data = dataC
data = dataD
fig = px.bar(data, title="Estimated Time per Receipt", text="Values", y="Values", x='Name', animation_frame=data["Frames"], range_y=[0, 200], animation_group = 'Name')


fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 10
fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 5
fig.update_layout(
    height=600,
    width=1200,
    font=dict(
        family="Courier New, monospace",
        size=20,  # Set the font size here
        color="RebeccaPurple",
        
    ),
    annotations=dict(
        font_size=60,
    )
)
# fig.update_annotations(
#     font_size=60,  # Set the font size here
# )
fig.show()



# import plotly.express as px

# df = px.data.gapminder()

# fig = px.bar(df, x="continent", y="pop", color="continent",
#   animation_frame="year", animation_group="country", range_y=[0,4000000000])
# fig.show()
