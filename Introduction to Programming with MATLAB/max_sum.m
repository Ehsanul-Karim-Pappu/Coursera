function [summa, index] = max_sum(v, n)
    if length(v) < n
        summa = 0; index = -1;
    else
        summa = -999999999999999; index = 1;
        for i = 1 : length(v) - n + 1
            s = sum(v(i : i + n - 1));
            if s > summa
                summa = s;
                index = i;
            end
        end
    end
end
