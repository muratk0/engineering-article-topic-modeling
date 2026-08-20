# Better Bevels With Plasma

[TARİH: 01.11.2017 The Fabricator]

Technological advances boost quality and throughput

By Madhura Mitra

A

n estimated 40 percent of parts cut on a plasma cutting table ultimately need a beveled edge, most often for weld preparation. For the most part, these edges are cut with a secondary process. Fabricators cut parts to size using plasma, then pick up and move the parts to another station to add the beveled edge. This not only adds time and labor to most jobs, but also wastes metal as the parts are cut a second time.

Using a bevel head on the plasma table itself can eliminate the need for these secondary operations and increase productivity, but one large obstacle stands in the way: The physical behavior of the plasma arc changes as the torch tilts and the consumables wear. The operator needs to compensate constantly by adjusting the settings. Though not exactly difficult, this task consumes a large amount of time and material as it is very iterative, requiring quite a bit of trial and error. For many, this impedes productivity on the bevel cutting table, so much so that they give up beveling with plasma altogether, and instead let their expensive automated bevel equipment sit idle.

Obstacles to a Good Bevel

Bevel cuts are described throughout the industry by the English letter the cut resembles when looking at a cross section of the metal. The types include V, A, X, Y, and K (see

Figure 1

). The complexity increases with the number of plasma torch passes required to cut a bevel type.

The V and A bevels require only a single pass, followed by Y (top and bottom) and X, which each require two passes. For the Y bevel, one pass establishes the straight edge, or the

land

, and another pass cuts the bevel. For the X bevel, two torch passes establish the top and bottom bevel angles.

The K bevel is arguably the most challenging to cut as it requires three torch passes: one to establish the land and two more to cut the top and bottom bevel, not necessarily in that order.

The large range of available bevel angles, material types, thicknesses, and amperage levels increase the difficulty of determining the process parameters for achieving a good plasma bevel. Even just one parameter change requires new process data.

Physics also plays a role since, as mentioned earlier, the plasma arc isn’t static. The consumables wear with each cut, changing the arc. The variables abound: the distance between the torch and workpiece, the molten metal flow path, the impact of gravity on that path, and more.

All these factors determine the bevel-process compensations required. It implies that the process compensation data potentially needs continuous tuning to maintain the desired cut quality, angle, and dimensions over the life of the consumables. This is true even with dedicated bevel cutting heads that rotate to match the bevel angle being cut.

Beveling With Plasma

Better beveling with plasma could save fabricators an enormous amount of time and money. It would allow them to increase the number of parts cut in the given time by replacing non-value-added activities with production. Today’s high-definition class of plasma systems are more than capable of making excellent beveled edges. The tools required for this include a suitable torch, a dedicated bevel head, and a CNC preloaded with the cutting parameters through the plasma cutting software.

Bevel cutting requires a plasma system with a high open-circuit voltage (OCV) and industrial duty cycle. This ensures that the arc voltage during piercing and cutting, especially at the higher bevel angles (farther from perpendicular), will not exceed the plasma systems’ capabilities, all while maintaining a reasonable clearance between the torch and the plate. An adequate clearance is important for avoiding damage to the consumables from molten metal slag produced during cutting.

Most recommend a "pointy" plasma torch (see

Figure 2

) because it provides the effective cut height necessary to maintain a minimum clearance for bevel cutting without posing any threat to the consumables. "Pointy" is defined as a torch head with a shield face diameter and included shield angle that are as small as possible for any given amperage. A clearance value of 0.08 to 0.1 inch is recommended.

While it is true that greater clearances would reduce the likelihood of torch and consumable damage, greater clearances also lead to higher effective cut heights and higher cutting voltages, both of which have their own set of problems. Higher cut heights can lead to lower edge quality and require higher angle compensations, while higher cutting voltages could affect the plasma system’s duty cycle.

CNC cutting tables have two common types of dedicated bevel heads: AC and ABXYZ (see

Figure 3

). The AC-type bevel heads tilt about the X axis and rotate about the Z axis. The ABXYZ types tilt about the X and Y axes and use XYZ linear-axes compensation to determine a virtual torch rotation point.

The bevel pivot point, or rotation point, is the point in 3-D space that the bevel head tilts around. This point is at the tip of the torch or the end of the shield (see

Figure 4

). A bevel head uses validated motion transformation equations to rotate about the bevel pivot point.

Modern systems also minimize what’s known as

process shift

, when the plasma arc moves across the top of the plate as the torch tilts (see

Figure 5

). AC heads accomplish this by optimizing the relationship between the bevel pivot point and the plasma torch head. Knowing the size of that shift is necessary to calculate the eventual size of the beveled part. That’s because the size of the shift determines the amount of process compensation, or the level of adjustment made to the torch path.

ABXYZ-type heads can maintain a virtual bevel pivot point at the top of the plate to maximize plate utilization. In this case, the process shift becomes zero.

Bevel head alignment, or calibration, also is important for achieving the correct bevel angles and part sizes. Bevel head alignment is set by first determining the relationship between the bevel head rotation point and the torch head, then by setting the bevel head home position so that the torch is square to the plate.

Bevel head manufacturers use either an automatic calibration routine through the CNC integration or a set manual calibration procedure. Once the bevel head is calibrated, the system can use the bevel cutting parameters to achieve the desired results.

Figure 1 Each bevel type, from the A bevel to the K bevel, has its own unique plasma cutting challenges.

Figure 2 Bevel cutting with plasma usually calls for a "pointy" cutting head with the smallest shield face diameter and angle for any given amperage.

Figure 3 There are two types of plasma cutting heads for beveling: AC and ABXYZ. AC types tilt about the X axis and rotate about the Z axis. ABXYZ heads tilt about the X and Y axes and have XYZ linear axes.

Figure 4 The bevel pivot point, or rotation point, is the point in space that the bevel head tilts around.

Figure 5 Process shift occurs when the plasma arc moves across the top of the plate when the head tilts. The latest plasma cutting systems minimize this.

Figure 6 Higher torch angles require smaller shield diameters and angles to maintain the desired clearance and effective cut height.

Developing Bevel Compensation Values

There are more than a few factors to consider for cutting different bevel types. For example, V cuts have a smooth cut edge and a sharp bottom edge. The cut part becomes trapped beneath the skeleton and cannot be removed until the skeleton is taken off the table. The torch follows a path on the top of the plate. However, the part’s larger bottom-surface dimension, called the

major size

, varies with the material thickness and bevel angle. If the bevel angle or material thickness changes ever so slightly, so does the part’s major size.

When an A bevel is made with plasma cutting, high-temperature gases blown into the kerf result in a rough edge with a rounded top. The dropped part rests on top of the skeleton. The

minor size

(in this case, the part’s bottom surface) varies with the material thickness and angle. In addition, the top-edge rounding makes the major size (top surface) slightly smaller than it would be after plasma cutting a V bevel.

Performing A bevels can present difficulties when a fabricator is trying to achieve 45-degree cut angles on thin materials, because the high angle compensation values require a bevel head capable of tilting more than 55 degrees (see

Figure 6

). In this case, a torch with a small included shield angle is less likely to affect the clearance, the effective cut height, or both.

Y-top bevel cuts have a straight land dimension, a parameter that V and A bevels lack. In this case, the specific multipass cut sequence used affects the results. Operators should first cut the land and then make the bevel.

Two Approaches

The key to plasma beveling is to gather the right process data for every conceivable bevel situation. Because the number of different bevel types combined with different material types, thicknesses, bevel angles, kerf, cut height, cut speed, and arc voltages is so great, there are thousands of possible situations.

Fabricators can use two approaches to determine the right bevel angle and part size. The first is to use trial and error to uncover process compensation values for every individual job. The second approach focuses on the most commonly cut bevel types (V, A, and Y-top), material thicknesses (¼ to 2 in.), and angles (15 to 45 degrees) to iteratively derive the relationship between the desired angle and size and the process compensation data.

The first approach might seem less tedious initially, but trial and error for each new bevel job—as is often done now—leads to a lot of wasted time and material. The second approach, though more complicated, can save time and material in the long run.

Some of the latest plasma cutting systems have software technology that takes this second approach. In addition to plasma variability, process variables include table motion, bevel head motion, precision of transformation equations, lifter performance, and arc voltage control accuracy. Though not exact, the values in the process parameter tables should result in a part that is very close to the desired dimensions, though some fine-tuning may be necessary.

Still, fabricators using the embedded parameters are pleased by what they are seeing. Some using the latest technology report setting up new bevel jobs in minutes on the plasma table, with no postbeveling cleanup required—a far cry from making bevels with an oxyfuel torch, hand grinder, or other methods. The time and money this saves means more competitive pricing for customers and extra profit for the company.

Madhura Mitra is a design engineer at Hypertherm Inc., 800-643-0030,

www.hypertherm.com

.