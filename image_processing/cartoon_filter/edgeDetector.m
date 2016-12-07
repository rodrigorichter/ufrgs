function [edgeImg] = edgeDetector(imgL,edgeImg)
    [height, width] = size(imgL);
    for r = 1 : height
        for c = 1 : width
               if (imgL(r,c) < 50) % pixels mais escuros na imagem sobel são brancos na mascara
                   edgeImg(r,c) = 255;
               else                % pixels mais claros são bordas na imagem sobel e preto na mascara
                   edgeImg(r,c) = 0; 
               end
        end
    end
end