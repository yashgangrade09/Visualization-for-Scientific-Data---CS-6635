array = rand(1,10000);
disp(array)
histogram(array, 20)
xlabel('Bins (20 in number)')
ylabel('Values')
title('Histogram of 10000 Random numbers from Uniform Distribution')