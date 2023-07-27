from rtlsdr import RtlSdr
import sounddevice as sd
import random

# Set up the SDR
sdr = RtlSdr()

# Configure the SDR parameters
sdr.sample_rate = 2.4e6
sdr.center_freq = 89.5e6
sdr.gain = 'auto'

# Define the audio settings
sample_rate = 48000
duration = 1  # Duration of audio to play in seconds

def process_samples(samples):
    # Play the received samples directly without any processing
    sd.play(samples, sample_rate)

# Start receiving samples from the SDR
sdr.read_samples_async(process_samples, int(sample_rate * duration))

# Wait until the user interrupts the program
print('Press Ctrl+C to stop...')
try:
    while True:
        pass
except KeyboardInterrupt:
    pass

# Stop the SDR and close the device
sdr.cancel_read_async()
sdr.close()
