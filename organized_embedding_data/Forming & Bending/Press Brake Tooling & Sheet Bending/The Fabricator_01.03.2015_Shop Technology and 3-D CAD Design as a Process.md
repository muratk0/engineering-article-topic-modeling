# Shop Technology and 3-D CAD: Design as a Process

[TARİH: 01.03.2015 The Fabricator]

Precision Matters

CAD plays a role in design, but so does a pencil

By Gerald Davis, Contributing Writer

Read more from Gerald Davis at

www.thefabricator.com/author/gerald-davis

T

he mechanism shown in

Figure 1a

features a spring pointing off in space to the right. One end of that spring is supported by contact with a pocket in a pivoting lever. The spring’s free end requires some kind of support, and we’re tasked with providing solutions.

As examples of what might be needed,

Figure 1b

illustrates a single-piece sheet metal solution, while

Figure 1c

represents an alternative using a swagedin pin.

(Disclaimer: We offer this look-over-the-shoulderas-the-work-is-done point of view as an example work flow for your own design projects. The specific mouse clicks required will depend on your CAD software The CAD models shown in the illustrations are available for your download.)

Figure 1a

The free end of the spring needs to be supported with an adjustable bracket that mounts using two threaded holes in this base piece.

Figure 1b

This sheet metal bracket has a bent post to capture the spring.

Figure 1c

A swaged-in captive pin is used to hold the spring in this alternative solution.

To determine a suitable solution in this case study, we apply various CAD tools to present options regarding aesthetics, structure, and cost. Our CAD deliverable is intended to inform the decision as to which solution to take to market.

We enter this scenario with only the 3-D model shown in Figure 1a. Pretend you haven’t looked at

Figures 1b

and 1c yet.

Goalposts First

As a list of design goals for our new spring anchor, we want:

• Spring retention.

The spring should be held in place by snugly sliding the spring over a post. The post must not be too big or too short.

• Adjustable spring force.

The size of the spring may need to change as the design matures. For any spring size, adjustment slots are to align with predetermined locations for clamping screws. The post must not interfere with swing-arm motion.

• Easy maintenance.

Springs must be replaced, so fragile features on the post should be avoided.

• Practical fabrication.

Production quantities are expected to be in the hundreds per month. Tooling expense must be amortized into the piece-part cost.

• Miscellaneous details.

The material selection must be compatible with that used in typical office equipment. The design must take into account manufacturing efficiency–whether the part should be stamped, machined, cast, or otherwise. Decisions have to be made about what documentation and drawings are needed.

(Here is a CAD tip: The listing of design goals is an important step in a design project.)

Doodling Is Dandy

With design goals in mind, we should next doodle and sketch ideal shapes for the spring anchor.

Figure 2

illustrates the idea of rough sketches to work out design approaches. Doodle with pencil and eraser before grabbing the CAD mouse.

While doodling, it is important to evaluate a variety of manufacturing options. The combination of ideal shape and practical fabrication will guide the first stage of CAD modeling.

In this scenario, the small production quantity and the need to minimize tooling expense have eliminated casting as an option. Machining this shape from billet might make sense depending on the available supply chain. Note how the list of design goals is influencing our CAD decisions.

Figure 2

Use pencil and paper to rough out concept sketches before grabbing the CAD mouse.

Our scenario’s requirement for adjustment slots and clamping screws has led to sheet metal as the basic fabrication approach. In order to model a sheet metal design, we need to create a part file, select a reference surface, sketch a base flange, and extrude it into a sheet metal body. From there we’ll embellish it with cut-extrudes for slots and tabs to create the post for the spring.

The Easy Way or the Magic Way?

Some folks routinely use their CAD for production of flat layouts in manufacturing and not much else. Assemblies of components, parametric links between components, and revision management may be infrequently used. And thus we delve.

We arrive at a fork in the CAD-modeling process. Will that new part file exist as a stand-alone item, or will its shape be linked to the 3-D model shown in

Figure 1a

?

When the design is in development, parametric links are a blessing. If one is merely investigating rather than purposefully editing a model, dragging a component and having it change shape can be awful.

On the other hand, a stand-alone model–one that does not have any parametric links to other parts–is somewhat easier to control in terms of accidental edits. However, the nonparametric revision process requires manual intervention to correct every discrepancy. A parametrically linked model can improve the efficiency of design development by keeping slots aligned with their screws automatically, for example.

(Here’s another CAD tip: A parametrically linked model can be locked to prevent unwanted updates to the model’s features. Use that tool for in-house revision control. In addition, use the easy-to-edit parametric model to export "dumb" STEP CAD models for exchange with manufacturing. As with PDFs, STEP files are relatively indelible and serve to support quality control during the manufacturing phase.)

In our design scenario, we take the parametric fork in the CAD path, as it were, and eschew the stand-alone modeling approach.

With the 3-D assembly model of the target mechanism from

Figure 1a

open, we insert a new part and proceed with the modeling of a spring anchor bracket. As shown in

Figure 3a

, we take advantage of the existing 3-D geometry to add sketch relationships to control the size and shape of our bracket’s base flange. We also link the size of our post to the inside diameter of the spring’s CAD model.

Figure 3a

The bent-post version of the bracket starts with a sketch for the base flange. The sketch has external relationships to parametrically link it to the master assembly.

Figure 3b

The completed model of the bent-post design is shown.

Figure 3c

Simulation of load on the post indicates that it can support more than 10 lbs. and less than 14 lbs. That’s good to know when evaluating the merits of the design.

After cutting away some material to create the adjustment slots and the spring’s anchoring post, we arrive at the sheet metal shape shown in

Figure 3b

. The rectangular post is the functional equivalent of a pin that is 0.09375 in. in diameter but is reduced somewhat due to the sheet metal gauge selected.

Fragility avoidance is one of our design goals.

Figure 3c

shows a screen capture of a quick simulation of a load on the post. This study reveals that just a few pounds of pressure will cause significant deflection.

As an alternative design, the use of a swaged-in captive pin would be more robust. A major hardware part provider offers an off-the-shelf option for a pin of ideal size. The company also offers CAD model downloads.

Figure 4a

shows the final stages of importing one of its files into our CAD software.

While modeling the sheet metal to receive the pin, we use external sketch relationships to ensure that the pin will align with the spring and that the sheet metal will hold the pin. See

Figure 4b

for a hint as to what the process can look like in CAD.

The model of the new pin and the sheet metal model of the bracket are mated in an assembly file to produce the model shown in

Figure 4c

. This is a relatively easy part to fabricate, and it is more robust than the previous design.

We are nearly ready for a design review meeting to call for a choice between these two designs. It would be useful to understand the difference in cost. As a reference, the costing tool gives an estimate for both sheet metal designs (see

Figure 5a

). The piece with two bends costs more than the piece with one bend–$2.53 versus $1.57, respectively.

The price of the off-the-shelf stud should be added ($0.30), along with the labor of installation ($0.10). This brings the captive pin version of the design up to $1.97. It remains relatively less expensive than the dainty single-piece version.

Figure 4a

Downloaded CAD models save time. In this example, Import Diagnostics were used to ensure that the imported geometry is fault-free.

Figure 4b

Again, parametric links are used to keep the bracket’s design in conformance with design goals.

Figure 4c

The completed assembly of an off-the-shelf pin and sheet metal bracket is shown. The BOM table gives a preview of what data is available to appear on fab drawings.

Everybody Is a Critic

As we evaluate and compare the designs in

Figure 5b

, we note:

The swaged pin is more robust than the bent post and is relatively good at holding the spring in the right direction.

The bent post is slightly more difficult to fabricate, but the design is easy to optimize for fit with the spring. The off-the-shelf pin is available only in a few sizes.

The swaged pin has a smooth friction-fit with the spring; the bent post has knife-edge engagement with the spring. Knifeedge makes for better spring retention, but may shorten the spring’s service life.

The swaged pin has minimum hole-toedge requirements that constrain the size of the sheet metal part. The bent-post design can be reduced in size and mass if needed.

The bent post has a less complicated supply chain than the swaged pin design. Not all sheet metal shops deal with hardware installation. Also, sometimes these hardware parts are out of stock.

(A final CAD tip: Minutes from design meetings are important and should be included in the record of the design’s evolution.)

Figure 5a

Two cost estimates are shown for comparison. On the top, the bent-post design costs $2.53 because of the two bends and profiling. On the bottom, the $1.57 bracket still needs to have the cost of the swaged-in pin included.

Figure 5b

Two designs are shown for comparison. When making these types of comparisons, keep notes and markups from design review meetings. You never know when a discarded idea will get another chance.

In this scenario, we depart before the decision to select is completed. One might imagine the review committee wrangling with the camp championing the bent post, as those folks favor simplicity, while the supporters of the off-the-shelf hardware contend that an aluminum bracket with a stainless pin will be lightweight, gentle, and strong.

As CAD jockeys, our mission was to visualize solutions that are tailored to a specific need and budget. To accomplish that we required clarity on the need, or design intent, as well as insight into the consequences of the modeling technique. It bears repeating: Write down the goals and doodle before grabbing the mouse.

Gerald Davis uses CAD software to design and develop products for his clients at

www.glddesigns.com

. From 1984 to 2004 he owned and operated a job shop. Please send your questions and comments to

dand@thefabricator.com

.