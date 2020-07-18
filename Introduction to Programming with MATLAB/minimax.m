function [mmr, mmm] = minimax(M)
M = M.'
mmr = abs(max(M) - min(M))
mmm = abs(max(max(M)) - min(min(M)))
