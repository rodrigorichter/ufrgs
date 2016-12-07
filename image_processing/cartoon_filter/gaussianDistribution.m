function [value] = gaussianDistribution(sigma,distance)
    value = (1/(sqrt(2*3.1415*sigma^2)))*exp(-(distance^2/2*sigma^2));
end