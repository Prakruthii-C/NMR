import numpy as np

def lorentzian(x,x0,gamma,amplitude):
    return amplitude*(gamma**2)/((x-x0)**2+gamma**2) # lorentzian peak profile

def generate_mock_spectrum(num_points=1000):
    x=np.linspace(0,10,num_points)  # array of chemical shifts

    baseline_noise=np.random.normal(0,0.02,num_points) # random noise
    spectrum=baseline_noise # y-axis

    # mock peaks: (peak_centre_ppm, peak_width_gamma, peak_amplitude) or (x0,gamma,amp)
    mock_peaks=[
        (1.2,0.05,1.0),
        (3.5,0.08,0.7),
        (7.2,0.12,0.4)
    ]

    for x0,gamma,amp in mock_peaks:
        spectrum+=lorentzian(x,x0,gamma,amp)

    return x,spectrum # returns 2 arrays of 1000 x and y axis vals

if __name__=="__main__":
    shifts,intensity=generate_mock_spectrum()
    print(f'no. of data points: {len(intensity)}')
    print(f'min value: {intensity.min():.4f}, max value: {intensity.max():.4f}')




