# Just how much detail is needed in a 3D model?

[TARİH: 01.09.2024 The Fabricator]

Precision Matters

Some details are essential in 3D models, but others are a waste of time

Gerald Davis

FIGURE 1A The start of a spiral for a tapped hole could be constrained in the 3D model and fully specified on the fabrication drawing. In this example, it doesn’t matter that the fabricated part probably won’t exactly match the 3D CAD. This is offered as a permissible omission of detail.

FIGURE 1B We have an application for an SD card reader. A generic device is available, but there is no suitable mount for our specific design. To specify the mount for fabrication, we need a model of the SD card reader.

FIGURE 1C Our model for the breakout board is based upon hand-measured dimensions. We are probably accurate within ±0.25 mm. Not ideal, but sufficient for designing this mount.

Figure 1D The CAD software can efficiently resolve the location of planes. This makes for speedy mates in a 3D assembly. We have created a few planes for the convenience of mating this card with the socket.

I

n the real-world experience of CAD, a useful 3D model often lacks perfect accuracy. Not all details need to be fully specified, and some details don’t need to be modeled.

As an example of acceptable deviation from reality, the starting angle of the spiral in a tapped hole is likely to be randomly created during a machining process. As it lowers, a tap spinning in a tapping head will find an engagement point as it centers in the pilot hole.

An example of spiraling detail is shown in

Figure 1A.

A helical spiral’s starting point might be specifically located in 3D CAD but, since it is not critical to function, not specified on the 2D dimensioned drawing for quality control. It’s left as an ambiguous feature. In other words, some forms of short-cut (incomplete specification) are reasonable. It’s omission as a matter of efficiency in producing a useful virtual prototype.

The efficient addition of essential detail depends upon skillful application of technique. Of course, determining what to do about the nonessential detail is a matter requiring essential judgement.

The story here is that an off-the-shelf electromechanical device drives the design; our design must adapt to that device. We are not to fabricate the device, just design the mount for it.

Figure 1B

shows our storied device (an SD card in a card reader circuit board). How do we attain such a 3D CAD model for an off-the-shelf device?

Best Scenario

If available, download and import it. Quite often, the manufacturer offers a file in STEP (or similar) CAD file format. Suitable downloads might be found in model libraries such as

www.3dcontentcentral.com

and

grabcad.com

, as well as resellers like

www.mcmaster.com

.

This Scenario

Downloads for this SD breakout board can be found on GitHub. The files are mostly for electronics developers and programmers. I did not see a handy 3D file for our simple task of mechanical layout. In other words, we need to know more detail about the hole size, the socket, and the locations of each.

After receiving a physical sample of the board via the mail, this CAD jockey created a CAD mod-el of the SD device by reverse-engineering the physical sample. The resulting measurements are shown in

Figure 1C

. The absence of the intended tolerances and target dimensions for the board means that we must be generous with our tolerance planning for the mount; our dimensions are suspect. This is not an ideal scenario.

Here’s some sage advice: When a CAD model must be created from scratch, anticipate how the model will be used (mated and visualized) in the overall CAD project. Reference geometry can be particularly useful for establishing mated relationships between components. In this project, we use a convenient combination of planes we create and planes available by default

(

see

Figure 1D

).

Irregular as Routine

The modeling of this SD card mechanism is nearly a very routine project—simple sketches and extrudes. However, we have some solder tabs that are irregularly entertaining.

To the left in

Figure 2A

we see an SD card socket with a sketch-driven pattern of solder tabs on the back of the shield. The distance between the tabs is irregular; they match the traces on the circuit board. As a result, a linear pattern for these tabs (very regular) is the wrong CAD technique.

FIGURE 2A To the left, a socket with an irregular pattern of solder tabs is shown. To the right, the sketch that constrains that pattern is shown. The pink tab is the only tab actually modeled. The rest are copies of it.

FIGURE 2B Add configurations by clicking on "Creates a new configuration." Here, four configurations have been set up for the location of the SD card: Docked, Eject, Release, and Toggle. The value of the dimension in the path (D1@Distance1) is unique to each configuration (0.187 in., 1.500 in., 0.370 in., and 0.167 in. respectively).

When a CAD model must be created from scratch, anticipate how the model will be used (mated and visualized) in the overall CAD project. Reference geometry can be particularly useful for establishing mated relationships between components.

A sketch-driven pattern is the right technique. It requires something to pattern with the sketch. In this example, that something is one solder tab (shown in pink in Figure 2A). The other tabs will appear where points in the sketch are located. Note no point is found at the location of the modeled tab.

Planning Access With Configurations

The SD card system has specific mechanical access requirements. The SD card slides into a socket. When fully pressed into the socket, the latching mechanism toggles to dock and lock the card. When pressure is released, the card is locked in place. One must again fully push the locked SD into the socket to toggle the latch for unlock and eject.

FIGURE 3A The model for the mount starts with a screw boss that is constrained to be concentric with a screw hole in the breakout board. All other features are children of this boss extrude.

FIGURE 3B With the screw boss completed, other features are added to the mount. All are dimensioned relative to the boss or to the card reader.

FIGURE 3C The mount is completed by mirroring, by adding a tapped hole specification with the Hole Wizard, and by adding modeled spirals so that the threads might be 3D-printed.

FIGURE 3D The board is screwed to its mount. The SD card is configured in its docked position.

Figure 2B

illustrates these various card-socket relationships. A distance mate controls the location of the SD card relative to the circuit board. When this mate was created, the default name, D1@Distance1, was established. That name appears in the Modify Configurations table (launched by a right-mouse click on the dimension mate and then selecting configure).

Modeling on the Mount

With an accurate model of the device to mount completed, we turn to modeling the mount. In

Figure 3A

, the history of the modeling effort is shown.

The mount is modeled in the context of an assembly, the first modeled feature is a screw boss located at the center of a screw hole. All other features of the mount will be children of this screw boss. Some of those children also will be constrained to features of the SD card reader model.

In

Figure 3B

, the relationship between the screw boss and the feature of its children in the mount is revealed. Modeling in the context of an assembly is an efficient means to tailoring the mount to the device.

Figure 3C

shows the result of mirroring the body shown in Figure 3B. Mirroring is wonderful for time-saving. Note that the Hole Wizard was used to add the tapped hole feature after the mirroring operation.

This modeling choice was made (hole pattern as opposed to mirroring the tapped hole) because the Hole Wizard creates a useful sketch that can be used to pattern the screws in the assembly. Also note that a thread feature was added to the tapped holes to facilitate 3D printing of this mount.

Figure 3D

shows an almost-complete 3D model. We note that the traces on the board are merely implied by the decal, not by modeled features. The latch mechanism is simulated, not modeled, and the read/write slide on the SD card is always in write, to cover a few outstanding items.

The model is useful, however, for designing a mounting system. It is very useful as a prop for a magazine article, right at the limit of providing too much detail.

Gerald

would love for you to send him your comments and questions. You are not alone, and the problems you face often are shared by others. Share the grief, and perhaps we will all share in the joy of finding answers. Please send your questions and comments to

ddavis@fmamfg.org

.

Efficient deburring and leveling.

Visit our booth #S17007 in Orlando, FL from Oct. 15-17

Deburring and leveling technology from a single source:

www.arku.com

Increase productivity:

with double-sided deburring and edge rounding.

Optimal downstream processing:

thanks to flat and stress relieved parts, sheet and plates.

Editor’s Note: CAD files associated with this column can be downloaded at

www.thefabricator.com/page/shop-technology-and-3-d-caddownloads

.