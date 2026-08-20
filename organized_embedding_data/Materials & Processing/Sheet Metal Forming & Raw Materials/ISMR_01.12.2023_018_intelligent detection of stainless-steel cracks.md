# Intelligent detection of stainless-steel cracks

[TARİH: 01.01.2023 ISMR]

The Austrian Institute of Technology GmbH (AIT) and voestalpine BÖHLER Edelstahl have developed an intelligent testing method that automatically finds defects in high-performance steel products, increasing resource efficiency in production and reducing employee workload.

Voestalpine BÖHLER Edelstahl GmbH & Co KG produces high-performance steels and nickel-based alloys for the international aerospace, automotive and oil & gas industries. An intermediate product in the production of stainless-steel products is called a “billet"; these have a square cross-section and are rolled for further processing. It is crucial for the quality of the end products that these rolled billets do not have any defects on their surface, such as slag inclusions or cracks. These would enlarge during rolling and impair the properties of the end products.

“If such a defect is detected on the surface, the billet is ground further until the surface is flawless. The optimum grinding treatment and the number of grinding passes required are currently decided by employees who visually scan the surface for defects," explained AIT.

To do this, the researchers borrowed from the way a person inspects an object.

"Most of the time, you can only see defects in the sub-millimetre range under a certain viewing or illumination angle. Therefore, when a person inspects an object, they look at it from different directions," explained Petra Thanner, who conducts research at the AIT Centre for Vision, Automation & Control (VAC) and is in charge of the project at AIT.

This is mimicked by the “Inline Computational Imaging (ICI) technology" developed at AIT. Here, a camera is permanently installed above an inspection object, which moves underneath. The scene is illuminated from four different directions; these are selected in such a way that the difference between cracks and normal grinding marks stands out as clearly as possible.

The raw camera images, on which the defects each have different shadow effects, are further processed in the next step using photometric methods. In this process, in addition to detailed and high-contrast 2D images, an exact 3D model of the surface is also calculated in which surface defects become even more clearly visible.

Artificial intelligence (AI) methods are used to classify these structures either as normal grinding grooves or as defects. An artificial neural network was trained with countless camera images that had previously been manually labelled as to which type of surface structure they were. The AI system learned to reliably detect unwanted defects and to colourcode them in the camera images.

The inspection system developed by AIT has now been implemented as a pilot system at voestalpine BÖHLER Edelstahl. In a compact housing that protects the sensors and electronics from the harsh environmental conditions, it inspects the surfaces of the four billet sides directly next to the grinding chamber with an accuracy of 50 micrometres at a speed of 24 metres per minute.

“The results are clearly displayed on a screen. With the help of this assistance system, employees no longer need to leave the test stand for the time-consuming visual inspection. This not only makes work easier for the people concerned, but also enables better utilisation of the machines as it is no longer necessary to shut down the grinding system during the inspection," commented AIT.
