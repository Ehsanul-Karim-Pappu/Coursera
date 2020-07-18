A = [1:5; 6:10; 11:15; 16:20];
r(1:length(A(:,3))) = 1;
c(1:length(A(3,:)),:) = 1;
result = r * A * c;