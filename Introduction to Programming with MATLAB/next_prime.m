function k = next_prime(n)
    k = n + 1;
    while not(isprime(k))
        k = k + 1;
    end
end