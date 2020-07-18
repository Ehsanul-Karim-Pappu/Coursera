function valid = valid_date(year, month, day)
    if isscalar(month) && isscalar(year) && isscalar(day)
        if day > 31 || month > 12 || year < 1 || month < 1 || day < 1
            valid = false;
        elseif month == 2
            if ((rem(year, 4) == 0 && rem(year, 100) ~= 0) || rem(year, 400) == 0) && day < 30
                valid = true;
            elseif not((rem(year, 4) == 0 && rem(year, 100) ~= 0) || rem(year, 400) == 0) && day < 29
                valid = true;
            else
                valid = false;
            end
        elseif ((month <= 7 && rem(month, 2)) || (month > 7 && not(rem(month,2)))) && day <= 31
            valid = true;
        elseif ((month <= 7 && not(rem(month,2)) || (month > 7 && rem(month, 2)))) && day <= 30
            valid = true;
        else
            valid = false;
        end
    else
        valid = false;
    end
end
