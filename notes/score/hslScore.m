clear all;
n=100000;
p1 = randi(4, n, 1);
p2 = randi(4, n, 1);

W = [0.5000 0.2667 0.2143 0.1875
0.7333 0.5000 0.1667 0.3333
0.7857 0.8333 0.5000 0.4375
0.8125 0.6667 0.5625 0.5000];

ENew = [1.00 1.50 2.00 2.50
0.75 1.00 1.25 1.50
0.70 0.80 1.00 1.20
0.65 0.75 0.85 1.00 ];

EReal = [1.0000 1.8750 2.3333 2.6667
0.6818 1.0000 3.0000 1.5000
0.6364 0.6000 1.0000 1.1429
0.6154 0.7500 0.8889 1.0000];

ENew2 = [1.00 1.75 2.25 2.50
0.75 1.00 1.50 1.75
0.60 0.70 1.00 1.10
0.60 0.75 0.90 1.00 ];

ENew3 = [1.00 1.75 2.25 2.50
0.75 1.00 1.50 1.75
0.70 0.80 1.00 1.10
0.60 0.75 0.90 1.00 ];

EOld = ones(4,4);

%E = EReal;
E = EOld;

M = zeros(4,1);
for i=1:n
    w = rand(1,1, 'like', W(p1(i),p2(i)));
    if w <= W(p1(i), p2(i))
        M(p1(i)) = M(p1(i)) + E(p1(i),p2(i));
    else
        M(p2(i)) = M(p2(i)) + E(p2(i),p1(i));
    end
end

disp('League 1')
M/max(M)

E = ENew;
%E = EOld;

M = zeros(4,1);
for i=1:n
    w = rand(1,1, 'like', W(p1(i),p2(i)));
    if w <= W(p1(i), p2(i))
        M(p1(i)) = M(p1(i)) + E(p1(i),p2(i));
    else
        M(p2(i)) = M(p2(i)) + E(p2(i),p1(i));
    end
end

disp('League 2')
M/max(M)

E = EReal;

M = zeros(4,1);
for i=1:n
    w = rand(1,1, 'like', W(p1(i),p2(i)));
    if w <= W(p1(i), p2(i))
        M(p1(i)) = M(p1(i)) + E(p1(i),p2(i));
    else
        M(p2(i)) = M(p2(i)) + E(p2(i),p1(i));
    end
end

disp('Real Data')
M/max(M)

E=ENew2;

M = zeros(4,1);
for i=1:n
    w = rand(1,1, 'like', W(p1(i),p2(i)));
    if w <= W(p1(i), p2(i))
        M(p1(i)) = M(p1(i)) + E(p1(i),p2(i));
    else
        M(p2(i)) = M(p2(i)) + E(p2(i),p1(i));
    end
end

disp('ENew2')
M/max(M)


E=ENew3;

M = zeros(4,1);
for i=1:n
    w = rand(1,1, 'like', W(p1(i),p2(i)));
    if w <= W(p1(i), p2(i))
        M(p1(i)) = M(p1(i)) + E(p1(i),p2(i));
    else
        M(p2(i)) = M(p2(i)) + E(p2(i),p1(i));
    end
end

disp('ENew3')
M/max(M)


