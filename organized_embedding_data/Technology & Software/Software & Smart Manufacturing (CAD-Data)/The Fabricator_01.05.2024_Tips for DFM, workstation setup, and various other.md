# Tips for DFM, workstation setup, and various other best practices

[TARİH: 01.05.2024 The Fabricator]

Precision Matters

A real-world collaboration leads to a discussion of how to alter a feature management tool

Gerald Davis

FIGURE 1 A screen shot of the author’s 3D CAD workstation shows the Feature Manager on the left, Graphics Window in the middle, and Property Tab on the right.

FIGURE 2 To control what the Feature Manager displays, right click on the first entry, select Tree Display, then check your favorite data boxes.

FIGURE 3 A feature can be created that is offset from the sketch plane, thus eliminating the need for dedicated reference geometry (a plane) just for this feature.

FIGURE 4 Selecting a contour in a revolved feature allows us to cut a groove by not selecting it.

FIGURE 5 A barb will be patterned. Its revolved feature is centered on a port.

F

igure 1

is a screenshot from a mainstream 3D CAD workstation. It is set up with the Feature Manager on the left, the flyout Property Tap on the right, and the Graphics window in the middle. The two component parts in this assembly are displayed with their descriptions visible in the Feature Manager.

Some workstations display many data fields in the Feature Manager by default. This can be distracting and unhelpful. The setup sequence to control what is displayed in the Feature Manager is shown in

Figure 2

. This control over the Feature Manager was news to a recent collaborator in a CAD session, so it is reviewed before the world here.

Returning to Figure 1, the barbed CAD models shown in the Graphics Window present concerns regarding design for manufacturing (DFM). Concern arises from the discrepancy between the ease of modeling things in 3D and the difficulties of producing them in real life.

We start with the ease of modeling.

Figure 3

presents a method for creating an extruded feature that is not on the sketch plane. In this example, an extruded boss is offset from the sketch plane by 0.45 in., thus skipping the creation of a plane just for extruding.

Disclaimer: Sometimes a time-saving trick is a curse to those who are tasked with editing the model. It might help to be slow (and obvious) rather than speedy (and esoteric). Here, we like speedy.

Figure 4

presents another approach to speed— reducing the computer’s workload. We’re using a single revolve to model a port with an O-ring groove. There are other ways to model this, but all require more steps in the Feature Manager.

The sketch for the revolve includes two contours in one sketch—another time-saving trick. When we select the region that excludes the O-ring groove, the O-ring groove is cut as the revolve is created, so there’s no need to add a feature to machine the groove. However, there is a need to repeat the disclaimer—quickest isn’t always bestest.

Figure 5

stays with the revolve theme, but with a slightly more complex profile, this one for a hose barb. The design calls for at least two of these barbs. The CAD plan is to model a pattern of barbs to achieve this. In this example, the one instance pattern results in two barbs.

The "at least" notion is that this is presented as an imaginary design in progress. The modeled barb in Figure 5 is located at the center of its corresponding port. The sketch used for patterning will take advantage of this concentricity with related features.

Figure 6A

is the sketch for creating a pattern of barbs. It is just a single point located at the center of the other port. This comprises the entire sketch.

Figure 6B

shows the finished barb pattern. Yes, a simple copy operation, perhaps a rotated pattern, could accomplish the same thing. It would have been more dramatic in this demonstration to require more than two barbs on unequal intervals, but this shows a modeling technique that might save time and deliver clarity and versatility at the same time.

Figure 7

adds some fillets and chamfers to the model. These frills are offered as a topic of DFM. For this design and its intended method of fabrication, fillets are created by rotating cutting tools. That requires dedicated tooling, perhaps with unique grinding and sharpening requirements.

As a DFM guideline, chamfers are generally easier to tool and program than fillets. Fillets can be important to strength and safety in the final part. Sometimes they are a necessary feature of the cutting tool. But they add time and perhaps tooling expense to the part’s cost.

Figure 8A

presents an undesired consequence (bad specification for a countersink) from using speedy CAD tools—here, specifically, the use of the Hole Wizard to create a pattern of countersunk holes.

A related speedy tool—the Hole Callout tool— uses what the Hole Wizard creates. We used the Hole Callout tool to insert dimensions into the 2D drawing. At the lower right in Figure 8A, the callout is for a 0.201-in. through-hole and a 0.385-in. countersink at 82 degrees. The separate 0.211-in. dimension at the lower left was added to emphasize the actual through-hole created by the Hole Wizard.

As a side note, this kind of knife-edge countersink is a challenge to machine, hard to inspect, and nearly impossible to deburr—and thus very unwanted in nearly every design.

Why is the Hole Callout specifying a hole smaller than can be made? Because the Hole Wizard doesn’t know how thin the flange is. Thus, we must specify the through-hole diameter manually for countersinks in thin stock.

Figure 8B

shows the through-hole diameter as corrected to a more realistic 0.221-in. diameter.

In this rather cause-and-effect way, the Hole Wizard helps keep us on our DFM toes. The trick is to spot the undesired phantoms.

As an alternative to the speedy revolve in Figure 4,

Figure 9A

introduces the use of a solid body as a cutting body in a Cut Sweep. This is another demonstration of using CAD tools to goofproof the DFM.

In general, Cut Sweeps follow a path. In this example the path is a circle that matches the floor of the circular O-ring groove.

We model the cutting body as a separate body from the workpiece. In this example, the cutting body is simply a disk that represents a rotating saw blade. Yes, it does take 11/2 moments to model the cutting bos dy, so this isn’t a fast technique, but it is cool.

Figure 9B

shows the DFM aspect of this coolness. When the saw blade is modeled at 5/8-in. diameter, it is perfectly too big. It accidentally cuts the adjacent post as it follows the groove path. That’s a DFM violation revolution revelation.

In

Figure 9C

, the cutting body is edited to be a smaller saw (⅜-in. diameter) so that it does not cut the adjacent post.

Figure 9D

shows the groovy glory. As a side note, we could model a library of cutting tool bodies and insert them as needed into a design. Cutting bodies don’t have to be created ad-hoc.

When the saw blade is modeled at ⅝-in. diameter, it is perfectly too big. It accidentally cuts the adjacent post as it follows the groove path. That’s a DFM violation revolution revelation.

FIGURE 6A Patterning one barb to one location will result in two barbs. If we add a point at the location of the original barb, we will end up with three barbs in the model, but two of them will be at the original barb’s location.

FIGURE 6B In review, a sketch with a single point will result in a pattern of one barb. With the original barb, that adds up to two barbs. By changing the sketch pattern, we can add more barbs in any location.

FIGURE 7 We added chamfers to the ends of the barbs and fillets to deburr the part. In machining applications, fillets generally are more expensive than chamfers.

FIGURE 8A As a DFM hazard, the Hole Wizard can specify holes that are smaller than practical when the material is thin. Here the Wizard says 0.201 in. when 0.211 in. is minimum.

FIGURE 8B When a DFM error is encountered in a countersink, the Hole Wizard can be corrected to use a bigger through-hole.

FIGURE 9A A solid body can be used in a Cut Sweep to saw a groove.

FIGURE 9B DFM violation discovered! The solid body accidentally cuts an adjacent post when swept to cut the O-ring groove.

FIGURE 9C The solid body for the cutting tool is edited to change the diameter from 5/8 to 3/8 in. so it does not cut the adjacent feature.

FIGURE 9D The successful solid body for the cutting tool for the O-ring groove shows that it will clear the adjacent features without difficulty. DFM is achieved with CAD techniques that mimic how the part is actually fabricated.

Gerald would

love for you to send him your comments and questions. You are not alone, and the problems you face often are shared by others. Share the grief, and perhaps we will all share in the joy of finding answers. Please send your questions and comments to

ddavis@fmamfg.org

.

Editor’s Note: CAD files associated with this column can be downloaded at

www.thefabricator.com/page/shop-technology-and-3-d-caddownloads

.