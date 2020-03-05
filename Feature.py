import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile


class fft:
    def __init__(self, filename):
        self.desiredF = 20000
        self.sampling, data = wavfile.read(filename)  # Read the wav file
        # self.x = data[:, 1]  # we only need data from one channel
        self.x = data
        self.xf = np.fft.fft(self.x)  # Fourier Transform
        self.faxis = np.linspace(0, self.sampling, len(self.xf))

    # plot the data in frequency domain with axis in log

    def plotFreqLog(self):
        # compare the data before and after processing
        plt.semilogy(self.faxis, abs(self.xf))
        plt.xlabel('Frequency/Hz')
        plt.ylabel('Amplitude')
        plt.title('Frequency Spectrum')
        plt.show()
    # transform the data back to time domain and plot

    def plotFreq(self):
        # compare the data before and after processing
        plt.plot(self.faxis, abs(self.xf))
        plt.xlabel('Frequency/Hz')
        plt.ylabel('Amplitude')
        plt.title('Frequency Spectrum')
        plt.show()
    # transform the data back to time domain and plot

    def plotWave(self):
        axis = np.linspace(0, len(self.x)/44100, len(self.x))
        plt.plot(axis, self.x)
        plt.xlabel('Time/s')
        plt.ylabel('Amplitude')
        plt.title('Data in time domain')
        plt.show()

    # output the data after processing in wav file
    def writefile(self, outputname):
        wavfile.write(outputname, self.sampling, self.x_clean)

    def getFFT(self):
        rangeLow = 0
        rangeHigh = 10000
        step = 0.5
        size = int((rangeHigh-rangeLow) / step)
        freqs = np.zeros(size)
        for i in range(len(freqs)):
            desiredIdx = int(
                len(self.xf) * (rangeLow + step * i) / self.sampling)
            freqs[i] = abs(self.xf[desiredIdx])
        return freqs


# a = fft("./ppig/label0/8.wav")
# print(len(a.getFFT()))
# plt.figure(1)
# plt.plot((a.getFFT()))
# plt.show()

# a.plotWave()
# plt.show()
# plt.figure(2)
# a.plotFreq()
# plt.figure(3)
# a.plotFreqLog()
