filename = '1880.csv';
M = csvread(filename, 5,0);
year = M(:,1);
value = M(:,2);
%Convert to farehneit
value = 1.8.*value + 32;
bar(year, value)
ylim([30 34]);
xlabel('Year (1880 - 2017)')
ylabel('Degree F +/-')
title('Bar Plot depicting temperature changes through years 1880 - 2017 ')

