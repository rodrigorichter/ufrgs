function [value] = normalizeKernel(kSize,kernel)
    sum = 0;
    value = zeros(kSize,kSize);
    
    for i = 1:kSize
        for j = 1:kSize
            sum = sum+kernel(i,j);
        end
    end
    %renormaliza os valores do kernel para a soma dos valores ser 1
    for i = 1:kSize
        for j = 1:kSize
            value(i,j) = kernel(i,j)/sum;
        end
    end
end