function [F] = bansol(NN,NBW,S,F) 
% Band Solver 
 
N = NN; 
%----- Forward Elimination ----- 
for K=1:N-1 
   NBK = N - K + 1; 
   if (N - K + 1) > NBW 
      NBK = NBW; 
   end 
   for I=K+1:NBK+K-1 
      I1 = I - K + 1; 
      C = S(K, I1) / S(K, 1); 
      for J=I: NBK+K-1 
         J1 = J - I + 1; 
         J2 = J - K + 1; 
         S(I, J1) = S(I, J1) - C * S(K, J2); 
      end 
      F(I) = F(I) - C * F(K); 
   end             
end 
%----- Back Substitution ----- 
F(N) = F(N) / S(N, 1); 
for II=1:N-1 
   I = N - II; 
   NBI = N - I + 1; 
   if (N - I + 1) > NBW 
      NBI = NBW; 
   end 
   SUM = 0.; 
   for J=2:NBI 
      SUM = SUM + S(I, J) * F(I + J - 1); 
   end 
   F(I) = (F(I) - SUM) / S(I, 1); 
end