img = imread('D:\Pictures\house.jpg');

%resultImg = bilateralFilter(img,0.1,8,5);
resultImg = medianFilter(img,9);

imshow(uint8(resultImg));
