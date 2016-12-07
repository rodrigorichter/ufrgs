function [value] = distancefromPoints(x1,y1,x2,y2)
    value = sqrt((x2-x1)^2+(y2-y1)^2);
end