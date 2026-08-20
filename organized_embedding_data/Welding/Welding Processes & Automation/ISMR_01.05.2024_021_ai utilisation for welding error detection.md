# AI utilisation for welding error detection

[TARİH: 01.05.2024 ISMR]

Saving raw materials and energy in production processes is key. The same goes for welding. Artificial intelligence (AI) can help with this task but the relevant data is needed to train AI systems. However, this is data that many customers don't wish to give away. Federated learning can help to solve this dilemma and Fraunhofer IPA has developed a corresponding AI concept for welding specialist, Lorch.

"We train the artificial intelligence with the customers' data without the data leaving the respective company," explained Can Kaymakci, a scientist at Fraunhofer IPA. Each customer trains their own AI model with their data: it is not the data that is exchanged, only the AI models. These are combined into a single, better optimised overall model.

Researchers at Fraunhofer IPA had to select a suitable AI model for energy anomaly detection (a model that detects user errors primarily through energy consumption data). To do this, they collected data in the Lorch laboratory about the welding process being observed, including the intentional inclusion of “user errors". They carried out around 200 welding tests. A lot, but not enough to train an artificial intelligence system.

"We therefore duplicated the data; the original 200 data sets became 2,200," explained Kaymakci. The team also investigated how many measurements per second are necessary to reliably detect user errors.

"In this way, we can reduce the required storage capacity, simplify communication and process less data which, in turn, saves time, costs and energy," summarised Kaymakci. The researchers implemented the model they created on a welding power source from Lorch. The recognition rate of a model that was trained using federated learning was 0.81 and is therefore comparable to that of a system for which all customer data was available for training. Here, the recognition rate is 0.86.

"In contrast, systems that were trained with only one customer's data only detect errors at a rate of 0.45," confirmed Kaymakci. For welding machine manufacturer Lorch, this means that it will be able to offer its customers added value via the AI system without having to store the data centrally at Lorch. For customers, in turn, there is the advantage of being able to identify errors more quickly and benefit from the "knowledge" of all customers.■
