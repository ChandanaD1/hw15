# z-test

import random
import plotly.express as px
import plotly.figure_factory as ff 
import pandas as pd
import csv
import statistics
import plotly.graph_objects as go

df = pd.read_csv("hw14.csv")
claps = df["claps"].tolist()

pop_mean = statistics.mean(claps)
print("Population Mean: " + str(pop_mean))

mean_list=[]
for x in range (1,100):
    dataset=[]

    for y in range(1,30):
        rand = random.randint(0,len(claps)-1)
        value = claps[rand]
        dataset.append(value)
    
    mean = statistics.mean(dataset)
    mean_list.append(mean)

sample_mean = statistics.mean(mean_list)
print("Sample Mean: " + str(sample_mean))
deviation = statistics.stdev(mean_list)

std1_start1, std1_end1 = sample_mean - deviation, sample_mean + deviation
std2_start1, std2_end1 = sample_mean - 2*deviation, sample_mean + 2*deviation
std3_start1, std3_end1 = sample_mean - 3*deviation, sample_mean + 3*deviation

graph = ff.create_distplot([mean_list],["sample data"],show_hist=False)

graph.add_trace(go.Scatter(x=[std1_start1,std1_start1],y=[0,0.004],mode="lines",name="1"))
graph.add_trace(go.Scatter(x=[std1_end1,std1_end1],y=[0,0.004],mode="lines",name="2"))
graph.add_trace(go.Scatter(x=[std2_start1,std2_start1],y=[0,0.004],mode="lines",name="3"))
graph.add_trace(go.Scatter(x=[std2_end1,std2_end1],y=[0,0.004],mode="lines",name="4"))
graph.add_trace(go.Scatter(x=[std3_start1,std3_start1],y=[0,0.004],mode="lines",name="5"))
graph.add_trace(go.Scatter(x=[std3_end1,std3_end1],y=[0,0.004],mode="lines",name="6"))

graph.add_trace(go.Scatter(x = [sample_mean,sample_mean],y = [0,0.004], mode="lines",name="Sample Mean"))
graph.add_trace(go.Scatter(x = [pop_mean,pop_mean],y = [0,0.004], mode="lines",name="Population Mean"))
  
zTest = (pop_mean - sample_mean)/deviation
print("Z Test: "+ str(zTest))

graph.show()





