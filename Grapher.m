%% Program to graph connect 4 alpha-beta simulation data
clear
clc

totalPruning = readmatrix('SimulationData/TotalSimData.txt');
totalNoPruning = readmatrix('SimulationData/NoPruningTotalSimData.txt');

subplot(2, 1, 1)
plot(totalNoPruning(:,1), totalNoPruning(:,3), '-x');
hold on
plot(totalPruning(:,1), totalPruning(:,3), '-x');
title('Time Taken / Move'); 
xlabel('Turn Number');
ylabel('Time Taken');
axis([1, 19, 0, 4]);
legend('No Pruning', 'Pruning')

subplot(2, 1, 2)
plot(totalNoPruning(:,1), totalNoPruning(:,4), '-x');
hold on
plot(totalPruning(:,1), totalPruning(:,4), '-x');
title('Nodes Visited / Move'); 
xlabel('Turn Number');
ylabel('Nodes Visited');
axis([1, 19, 0, 3000]);
legend('No Pruning', 'Pruning')