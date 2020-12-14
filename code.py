import pandas as pd;
import csv;
import statistics;
import random;
import plotly.figure_factory as ff;
import plotly.graph_objects as go;

df = pd.read_csv('data.csv')
data = df['temp'].tolist()
population_mean = statistics.mean(data)
std_dev = statistics.stdev(data)

print('mean is ',population_mean)
print('stantard deviation is ',std_dev)
def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([data], ['temp'], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean, 'mean'], y = [0, 1], mode = 'lines', name = 'mean'))
    fig.show()
dataset = []
for i in range(0, 100):
    random_index = random.randint(0, len(data))
    value = data[random_index]
    dataset.append(value)
mean = statistics.mean(dataset)
std_devi = statistics.stdev(dataset)
print('mean of random 100 points is',mean)
print('standard deviation of random 100 points is',std_devi)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_ind = random.randint(0, len(data) - 1)
        value = data[random_ind]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ['temp'], show_hist=False)
    fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 1], mode = 'lines', name = 'mean'))
    fig.show()
def setup():
    mean_list = []
    for i in range(0, 1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print(mean)
setup()
population_mean = statistics.mean(data)
print(population_mean)

def std_dev():
    mean_list = []
    for i in range(0, 1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    std_deviation = statistics.stdev(mean_list)
    print(std_deviation)

std_dev()