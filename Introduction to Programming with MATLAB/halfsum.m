function summa = halfsum(M)
    summa = 0;
    for i = 1 : size(M, 1)
        for j = 1 : size(M, 2)
            if i * j > size(M, 1) * size(M, 2)
                break;
            end
            if j >= i
                summa = summa + M(i, j);
            end
        end
    end
end
