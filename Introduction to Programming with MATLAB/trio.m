function ans = trio(n, m)
ans(1 : n, 1 : m) = 1;
ans(n + 1 : 2 * n, 1 : m) = 2;
ans(2 * n + 1 : 3 * n, 1 : m) = 3;
