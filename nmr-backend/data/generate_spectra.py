import numpy as np
import pandas as pd
import os

def lorentzian(x,x0,gamma,amplitude):
    return amplitude*(gamma**2)/((x-x0)**2+gamma**2) # lorentzian peak profile

def generate_mock_spectrum(mock_peaks,num_points=1000):
    x=np.linspace(0,10,num_points)  # array of chemical shifts

    baseline_noise=np.random.normal(0,0.02,num_points) # random noise
    spectrum=baseline_noise # y-axis

    for x0,gamma,amp in mock_peaks:
        spectrum+=lorentzian(x,x0,gamma,amp)

    return spectrum # returns y-axis array (intensity)

if __name__=="__main__":
    num_samples=500
    all_spectra=[]

    for i in range(num_samples):
        # slightly randomise peak configurations
        peak1_pos=np.random.uniform(1.1,1.3)
        peak2_pos=np.random.uniform(3.4,3.6)
        peak3_pos=np.random.uniform(7.0,7.4)

        amp1=np.random.uniform(0.8,1.2)
        amp2=np.random.uniform(0.5,0.8)
        amp3=np.random.uniform(0.3,0.6)

        current_peaks=[
            (peak1_pos,0.05,amp1),
            (peak2_pos,0.08,amp2),
            (peak3_pos,0.12,amp3)
            ]
        intensity=generate_mock_spectrum(current_peaks)
        all_spectra.append(intensity)
    
    columns=[f'point_{j}' for j in range(1000)]
    df=pd.DataFrame(all_spectra,columns=columns)

    output_dir="nmr-backend/data"
    os.makedirs(output_dir,exist_ok=True)
    output_path = os.path.join(output_dir, "simulated_spectra.csv")
    df.to_csv(output_path, index=False)

    



