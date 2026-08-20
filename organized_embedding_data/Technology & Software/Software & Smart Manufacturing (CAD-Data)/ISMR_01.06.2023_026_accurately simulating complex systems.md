# Accurately simulating complex systems

[TARİH: 01.06.2023 ISMR]

Researchers often use simulations when designing new algorithms, since testing ideas in the real world can be both costly and risky. But since it's impossible to capture every detail of a complex system in a simulation, they typically collect a small amount of real data that they replay while simulating the components they want to study.

Known as trace-driven simulation (the small pieces of real data are called traces), this method sometimes results in biased outcomes. This means researchers might unknowingly choose an algorithm that is not the best one they evaluated, and which will perform worse on real data than the simulation predicted that it should.

MIT (Massachusetts' Institute of Technology) researchers have developed a new method that eliminates this source of bias in trace-driven simulation. By enabling unbiased trace-driven simulations, the new technique could help researchers design better algorithms for a variety of applications, including improving video quality on the internet and increasing the performance of data processing systems.

The researchers' machine-learning algorithm draws on the principles of causality to learn how the data traces were affected by the behaviour of the system. In this way, they can replay the correct, unbiased version of the trace during the simulation.

When compared to a previously developed trace-driven simulator, the researchers' simulation method correctly predicted which newly designed algorithm would be best for video streaming — meaning the one that led to less rebuffering and higher visual quality. Existing simulators that do not account for bias would have pointed researchers to a worse-performing algorithm.

"Data are not the only thing that matter. The story behind how the data are generated and collected is also important. If you want to answer a counterfactual question, you need to know the underlying data generation story so you only intervene on those things that you really want to simulate," said Arash Nasr-Esfahany, an electrical engineering and computer science (EECS) graduate student and co-lead author of a paper on this new technique.

He is joined on the paper by co-lead authors and fellow EECS graduate students Abdullah Alomar and Pouya Hamadanian; recent graduate student Anish Agarwal PhD '21; and senior authors Mohammad Alizadeh, an associate professor of electrical engineering and computer science, and Devavrat Shah, the Andrew and Erna Viterbi Professor in EECS and a member of the Institute for Data, Systems and Society and of the Laboratory for Information and Decision Systems.

The new tool/algorithm they developed, dubbed CausalSim, can learn the underlying characteristics of a system using only the trace data. CausalSim takes trace data that were collected through a randomised control trial and estimates the underlying functions that produced those data. The model tells the researchers, under the exact same underlying conditions that a user experienced, how a new algorithm would change the outcome.

Using a typical trace-driven simulator, bias might lead a researcher to select a worse-performing algorithm, even though the simulation indicates it should be better. CausalSim helps researchers select the best algorithm that was tested.

During a ten-month experiment, CausalSim consistently improved simulation accuracy "resulting in algorithms that made about half as many errors as those designed using baseline methods."
