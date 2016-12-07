img = imread('C:\Users\Lucia\Desktop\image6.jpg');
[height, width, dim] = size(img);
edgeImg = zeros(height,width); 

% Primeiro passo
for i=1:3 
  img = bilateralFilter(img,0.1,3,1);    
end
img = uint8(img);

% Segundo passo
if(dim == 3)
    imgGray= 0.299*img(:,:,1) + 0.587*img(:,:,2) + 0.114*img(:,:,3); % mascara precisa estar em tons de cinza
else
    imgGray = img;
end

% Terceiro passo
imgGray = medianFilter(imgGray,3);  
imgGray = uint8(imgGray);

% Quarto passo
% Filtro Sobel horizontal + vertical 
ph = [-1 0 1; -2 0 2 ; -1 0 1];
pv = [-1 -2 -1; 0 0 0; 1 2 1];    
imgPh = uint8(conv2(double(imgGray),double(ph),'same')); % same dimension of image
imgPv = uint8(conv2(double(imgGray),double(pv),'same')); % same dimension of image
imgPh = double(imgPh);
imgPv = double(imgPv);
imgConv = uint8(sqrt((imgPh.*imgPh)  +  (imgPv.*imgPv)));
% detector de bordas usando o filtro Sobel final
edgeImg = edgeDetector(imgConv,edgeImg);

% Quinto passo
edgeImg = 255 * repmat(uint8(edgeImg), 1, 1, 3); % image binary to 3 channels rgb
cartoon = bitand(img,uint8(edgeImg));

% Grava resultado e mostra na tela
imwrite(cartoon,'C:\Users\Lucia\Desktop\Resultados\9.jpg'); 
subplot(1,2,1), imshow(img);
subplot(1,2,2), imshow(cartoon); 

