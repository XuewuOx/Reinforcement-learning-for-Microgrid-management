import sys
import os
import pickle

import numpy as np
import pandas as pd

project_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_path)


with open(file=project_path + f'/common.pickle', mode='rb') as file:
    params_and_log = pickle.load(file=file)


print(params_and_log.keys())  # 打印字典的健值
print(params_and_log)  # 打印字典



training_cumulative_reward = params_and_log['training_cumulative_reward']
training_cumulative_reward = pd.DataFrame({'training_cumulative_reward': training_cumulative_reward})
print(training_cumulative_reward)
training_cumulative_reward.to_csv('training_cumulative_reward.csv')


# read electric.pickle
with open(project_path + '/simulation_environment/data/electric.pickle', 'rb') as file:
  # (3, 96, 4), ((chance of coming, parking_time, volume), timestep, (max, min, mean, std))
  electricData = pickle.load(file)
  print(electricData.tolist())
  print(electricData)

  training_cumulative_reward = pd.DataFrame({'training_cumulative_reward': training_cumulative_reward})
print(training_cumulative_reward)
training_cumulative_reward.to_csv('training_cumulative_reward.csv')