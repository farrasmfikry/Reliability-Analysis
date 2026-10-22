import numpy as np
import pandas as pd

np.random.seed(42)
n_turbines = 20

# Generate Synthetic Turbine Component Failure Data (for Weibull & RCA)
components = ['Gearbox', 'Generator', 'Pitch System', 'Main Bearing', 'Converter']
data = []

for turbine_id in range(1, n_turbines + 1):
    for comp in components:
        # Assign realistic shape (beta) and scale (eta) parameters per component
        beta_val = 2.5 if comp in ['Gearbox', 'Main Bearing'] else 1.5
        eta_val = 12000 if comp == 'Gearbox' else 20000
        
        ttf = np.random.weibull(a=beta_val) * eta_val
        downtime = np.random.exponential(scale=48) if ttf < 50000 else 0
        
        data.append({
            'Turbine_ID': f'WTG-{turbine_id:02d}',
            'Component': comp,
            'Time_To_Failure_Hours': round(ttf, 2),
            'Downtime_Hours': round(downtime, 2),
            'Failure_Event': 1 if ttf < 40000 else 0 # Censored vs un-censored
        })

df_failure = pd.DataFrame(data)
df_failure.to_csv('component_failures.csv', index=False)
print("Successfully generated synthetic component_failures.csv!")