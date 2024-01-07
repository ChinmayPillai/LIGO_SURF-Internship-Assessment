min = 999;
for i=1:50
    for j=1:3
        if (min >= MSE(i,j))
            i
            j
            min(1,1) = MSE(i,j);
            min(1,2) = i;
            min(1,3) = j;
        end
    end
end