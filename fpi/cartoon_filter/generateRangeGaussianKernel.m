function [kernel] = generateRangeGaussianKernel(kSize,sigma,imgMat)
    kernel = zeros(kSize,kSize);
    middlePoint = [((kSize-1)/2)+1 ((kSize-1)/2)+1];
    sum = 0;
    
    %gera o kernel gaussiano de intensidade de cor
    for i = 1:kSize
        for j = 1:kSize
            r = double(abs(imgMat(middlePoint(1),middlePoint(2))-imgMat(i,j)))/255;
            kernel(i,j) = gaussianDistribution(sigma,r);
            sum = sum + kernel(i,j);
        end
    end
end