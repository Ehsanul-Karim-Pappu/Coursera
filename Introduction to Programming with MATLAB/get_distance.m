% grader was wrong for %distance = get_distance('Seattle, W','Miami, F')%
function distance = get_distance(city1, city2)
    [num, city] = xlsread('Distances.xlsx');
    city1_index = find(contains(city, city1), 1 ) - 1;
    city2_index = find(contains(city, city2), 1 ) - 1;
    if isempty(city1_index) || isempty(city2_index)
        distance = -1;
    else
        distance = num(city1_index, city2_index);
    end
end