%% wrapping

%% my solution
function coded = caesar(v, shift)
    coded(1 : length(shift)) = 0;
    j = 1;
    %double(v)
    for i = v
        coded(j) = i + shift;
        while not(coded(j) <= 126 && coded(j) >= 32)
            if coded(j) > 126
                coded(j) = coded(j) - 95;
            elseif coded(j) < 32
                coded(j) = coded(j) + 95;
            end
        end
        j = j + 1;
    end
    coded = char(coded);
end
%% using mod
% function txt = caesar(txt,key)
%     txt = double(txt) + key;
%     first = double(' ');
%     last = double('~');
%     txt = char(mod(txt - first,last - first + 1) + first);
% end
%% using circshift (didn't understand)
% function y = caesar(ch, key)
%     v = ' ' : '~';
%     [~, loc] = ismember(ch, v);
%     v2 = circshift(v, -key);
%     y = v2(loc);
% end