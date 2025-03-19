import numpy as np
from functions import prepare_stock_data
from dqn_model import create_dqn_model

csv_path = "dataset/individual_companies/AAPL_data.csv"
df_raw, df_state, state_columns, scaler = prepare_stock_data(csv_path)

state_size = len(state_columns)  
action_size = 3  # Buy, Sell, Hold
model = create_dqn_model(state_size, action_size)

sample_state = np.array(df_state.iloc[0]).reshape(1, -1)  
q_values = model.predict(sample_state)
print("Q-values for sample state:", q_values)