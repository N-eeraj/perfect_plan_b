import read

principle = read.Read(float, 'Principle Amount')
time = read.Read(float, 'Time')
rate = read.Read(float, 'Rate of Interest')

si = (principle * time * rate) / 100 #equation to find simple interest

print('\nSimple interest for principle amount {}, for {} time, at an interest rate of {} is {}'.format(principle, time, rate, si))
