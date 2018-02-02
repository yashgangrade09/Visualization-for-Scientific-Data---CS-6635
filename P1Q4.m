input_file = fopen('myfile.bin');
r = fread(input_file, 'float');
histogram(r, [0,14,28,42,56,70,84,100])
xticks([0,14,28,42,56,70,84,100])
ylabel('Frquency')
xlabel('Bins')
title('Histogram of data read from file with 7 bins')