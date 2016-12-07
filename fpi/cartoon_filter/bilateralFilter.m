function [resultImg] = bilateralFilter(img,sigmaSpatial,sigmaRange,kSize)
    G = generateSpatialGaussianKernel(kSize,sigmaSpatial);
    [height, width, dim] = size(img);
    resultImg = zeros(height,width,dim);

    for i = ((kSize-1)/2)+1:height-((kSize-1)/2)
        for j = ((kSize-1)/2)+1:width-((kSize-1)/2)
            %gera submatriz do tamanho do kernel
            submatrix = zeros(kSize,kSize,dim);
            for k = 1:kSize
                for l = 1:kSize
                    submatrix(k,l,:) = img(i-((kSize-1)/2)+k-1,j-((kSize-1)/2)+l-1,:);
                end
            end
        
            %aplica o filtro na imagem,
            for m = 1:3
                pixelValue = 0;
            %usa a submatriz pra gerar o kernel de intensidade de cor nos
            %canais
                R = generateRangeGaussianKernel(kSize,sigmaRange,submatrix(:,:,m));
                kernel = R .* G;
                kernel = normalizeKernel(kSize,kernel);

                for k = 1:kSize
                    for l = 1:kSize
                        pixelValue = pixelValue + double(img(i-((kSize-1)/2)+k-1,j-((kSize-1)/2)+l-1,m))*kernel(k,l);
                    end
                end
                resultImg(i,j,m) = pixelValue;
            end
        end
    end
end
