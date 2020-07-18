function output = blur(img,w)
    %row = height , col = width
    imgD = double(img);
    [row, col] = size(img);
    output = zeros(row, col);
    for i = 1 : row
        for j = 1:col
            r1 = i - w; r2 = i + w; c1 = j - w; c2 = j + w;
            if r1 < 1
                r1 = 1;
            end
            if r2 > row
                r2 = row;
            end
            if c1 < 1
                c1 = 1;
            end
            if c2 > col
                c2 = col;
            end
            m = imgD(r1 : r2, c1 : c2);
            output(i, j) = mean(m(:));
        end
    end
    output = uint8(output);
end