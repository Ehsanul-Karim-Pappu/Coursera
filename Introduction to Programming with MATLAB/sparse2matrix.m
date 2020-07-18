function m = sparse2matrix(cell)
    m(1 : cell{1}(1), 1 : cell{1}(2)) = cell{2};
    for i = 3 : length(cell)
        m(cell{i}(1), cell{i}(2)) = cell{i}(3);
    end
end