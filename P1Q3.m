a = 1;
b = 100;
r = (b-a).*rand(1, 100) + a;
array = 1:1:100;
f = fopen('myfile.bin', 'w');
fwrite(f, r, 'float');
fclose(f);
plot(array,r)
xlabel('Instances ranging from 1 - 100')
ylabel('Values of random variables')
title('Line plot of 100 random numbers with value between 1 to 100')