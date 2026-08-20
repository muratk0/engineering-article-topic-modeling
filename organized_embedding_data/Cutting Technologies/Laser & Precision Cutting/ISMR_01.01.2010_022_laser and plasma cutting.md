# LASER AND PLASMA CUTTING

[TARİH: 01.03.2010 ISMR]

## TABLE1. GEOMETRICAL PARAMETERS FOR TUBE FORMING TESTS

Fig. 2. Samples for laser forming tests

<table><tr><td>Sample</td><td>Tube scanned length [mm]</td><td>Number of scans perline</td><td>Angular dimension of a single scan [°]</td><td>Distance between consecutive set of scans [mm]</td></tr><tr><td>A</td><td>9.8</td><td>20</td><td>360</td><td>2</td></tr><tr><td>B</td><td>3.8</td><td>10</td><td>56</td><td>0</td></tr><tr><td>C</td><td>15.8</td><td>20</td><td>360</td><td>2</td></tr></table>

boundaries (about 56°). At each time step, the spot moved so as to overlap for a half to the previous position. Fixing the rotational speed to 0.628 rad/s, the resulting time step depended only on the mesh size and was nearly 0.085s.

After each laser heating step, a cooling step of 80s was simulated. Ten heating-cooling cycles were performed. The material properties were implemented as a function of temperature. A thermo-mechanical analysis was performed to simulate the forming process. Thermal analysis was carried out by using SOLID70 thermal elements. After obtaining the thermal solution, the thermal elements were converted into SOLID45 structural elements and the thermal solution was used to define the thermal loads. At the end of the simulation, the radial displacement of a reference node (Figure 1) was evaluated.

## MATERIALS AND METHODS

Laser forming tests were performed by putting into rotation slotted tubes, made of AISI 304, under a focused HPDL beam at a speed of 0.628 rad/s. All the tubes were 20mm in outer diameter and 1mm in thickness, according to the previously described FE model. To provide rotational speed, the tubes were cut to a length of 50mm and clamped to a stepping motor. The geometrical features of the tubes are depicted in Figure 2. In particular, sample (a) had no slots, whereas sample (b) had a Ushaped slot and (c) had four symmetric slots along the tube end. The laser-treated zone is shown in Figure 2 with a darker colour for each sample. Sample (b) presented the same geometry discussed in the Numerical Modelling section.

A 1.5 kW diode laser (Rofin-Sinar, DL 015) was used for tube forming. It had 940nm wavelength and a rectangular spot (3.8 x 1.2mm2) due to the superposition of two different rays, each one coming from a 750 W emitter diode. A 63mm long focus lens was used to maximize the depth of field.

FIG. 3: RADIAL DISPLACEMENT OF THE REFERENCE NODE DURING THE FIRST SCAN

During tests, the laser beam was focused on the external tube surface and the laser power was fixed at 150 W. The tube clamping length was 15mm. Initially, the laser was focused on the tube’s external surface and a first scan was performed along the tube circumference. At the end of the scan, the laser spot was moved to the initial position to repeat the same scan. Up to a maximum of 20 scans were performed consecutively. At the end of this first set of scans, the tube was left to cool in air. Subsequently the laser spot was moved along the tube length to perform a set of scans on a parallel circumferential line. The total processed length of the tube ranged from 9.8 to 15.8mm, the number of scans per circumferential line from 10 to 20. The single laser scan encompassed the entire tube external circumference apart from sample (b), for which an angular dimension of 56° was observed to bend just the tongue of Figure 2. The distance between two consecutive set of scans was 2mm. As the laser spot maximum axis was aligned to the tube length, a 1.8mm superposition resulted between successive scans.

## RESULTS AND DISCUSSION

## Numerical modelling

Figs. 3 and 4 show the results of the numerical simulation in terms of radial displacement of the reference node as a function of time for 1 and 10 scans respectively.

As Figure 3 shows, at the beginning of the laser exposure, a sudden increase occurs due to thermal expansion up to a maximum (point 1). In this case, the laser path is too short and the constraining effect of the surrounding material determines this

Fig. 7: Aspect of the samples after laser processing  
FIG. 6: RADIAL DISPLACEMENT MAPS (SECTION VIEW) AT THREE DIFFERENT TIME STEPS.

deformation. Subsequently, the radial displacement decreases down to a minimum (point 2). In fact, after 1s, the laser path is sufficiently longer than the spot size (Figure 5). The tongue deforms entering the tube wall and the minimum displacement is negative.

As the thermal strains have the same temperature gradients, the maximum is on the side of the spot and the tongue bends in the opposite direction. But in this condition, due to the very high temperature, the material starts to yield in the laser-processed zone. When the laser spot is sufficiently far from the early processed zone, the material starts to cool. However, due to the previous yielding, the tongue cannot return to the initial configuration but it starts to bend in the opposite direction.

Figure 4 shows the effect of successive superimposed scans. At the beginning of each step, the same mechanism as Figure 3 is repeated. In particular, the relative minimum is always clearly visible. After 800s of laser processing, over 1.8mm of total radial displacement is achieved (point 3).

In Figure 6, three displacement maps are shown that demonstrate these points. For a better understanding, maps 1 and 2 are shown with a scale factor of 10, map 3 is in true scale. The complex forming mechanism that leads the tongue to invert twice the bending direction is evident.

The numerical simulation was validated by the experimental test on sample (b). It was measured with a maximum radial displacement of about 2mm, according to the results in Figure 6.

## Laser forming tests

In Figure 7, you can see the formed tubes.

A flare was obtained for sample (a). In sample (b), the result was similar to that of sheet metal and the tube wall deformed towards the laser source.

However, the unprocessed surface of the tongue remained unaltered with the shape of the initial cylindrical surface. Instead, in sample (c), the laser spot was moved from one end to the other for a distance of almost 16mm. A complex double curvature surface resulted in the four tongues.

## CONCLUSION

In this study, a diode laser was used to form stainless steel tubes under different conditions. Under the proposed conditions, low power was sufficient to ensure good forming efficiency, even though the tube is thin-walled. The main aim was to enable new forming processes, apart from bending. Tongues, flanges and flares can also be achieved and used in small production runs or prototypes.

## EDITOR’S NOTE

A complete list of references can be found with the full version of the paper. This article has been edited from the original paper in the Proceedings of the 12th ESAFORM Conference on Material Forming Enschede (Netherlands), 27-29 April 2009 (edited by A.H. van den Boogaard and R. Akkermann, University of Twente), Int J Mater Form (2008) Suppl 1:1343 -1346. © Springer.

ISMR highlights a selection of the latest welding technologies and uncovers manufacturers’ views of the market
