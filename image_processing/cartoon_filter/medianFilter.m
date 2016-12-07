function [resultImg] = medianFilter(img,wSize)
    [height, width] = size(img);
    resultImg = zeros(height,width);

    for i = ((wSize-1)/2)+1:height-((wSize-1)/2)
        for j = ((wSize-1)/2)+1:width-((wSize-1)/2)
            %gera array com os valores da janela
            arrWindow = zeros(wSize^2);
            idx = 1;
            for k = 1:wSize
                for l = 1:wSize
                    arrWindow(idx) = img(i-((wSize-1)/2)+k-1,j-((wSize-1)/2)+l-1);
                    idx=idx+1;
                end
            end
            
            arrWindow = sort(arrWindow);
            median = arrWindow((wSize^2-1)/2); 
            resultImg(i,j) = median;
        end
    end         
end
