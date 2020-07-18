function [top_left, top_right, bottom_left, bottom_right] = corners(arr)
top_left = arr(1, 1);
top_right = arr(1, end);
bottom_left = arr(end, 1);
bottom_right = arr(end, end);
