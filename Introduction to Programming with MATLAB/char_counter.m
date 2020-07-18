function charnum = char_counter(frame,character)
    fid = fopen(frame,'r');
    if not(ischar(character)) || fid < 0
        charnum = -1;
        return
    end
    text = fscanf (fid, '%c');
    charnum = count(text,character);
end