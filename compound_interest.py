import read

principle = read.Read(float, 'Principle Amount')
time = read.Read(float, 'Time')
rate = read.Read(float, 'Rate of Interest')

ci = round(principle * (1 + rate / 100) ** time, 2) #equation to find compound interest

print('\nCompound interest for principle amount {}, for {} time, at an interest rate of {} is {}'.format(principle, time, rate, ci))
