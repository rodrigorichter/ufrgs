function [kernel] = generateSpatialGaussianKernel(kSize,sigma)
    kernel = zeros(kSize,kSize);
    middlePoint = [((kSize-1)/2)+1 ((kSize-1)/2)+1];
    sum = 0;
    
    %gera o kernel gaussiano de distancia dos pixels
    for i = 1:kSize
        for j = 1:kSize
            d = distancefromPoints(middlePoint(1),middlePoint(2),i,j);
            kernel(i,j) = gaussianDistribution(sigma,d);
            sum = sum + kernel(i,j);
        end
    end
end