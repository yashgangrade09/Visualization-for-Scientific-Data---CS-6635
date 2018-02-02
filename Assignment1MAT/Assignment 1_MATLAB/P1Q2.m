array = rand(1,10000);
disp(array)
histogram(array)
xlabel('Bins (Automatic Binning)')
ylabel('Values')
title('Histogram of 10000 Random numbers from Uniform Distribution')