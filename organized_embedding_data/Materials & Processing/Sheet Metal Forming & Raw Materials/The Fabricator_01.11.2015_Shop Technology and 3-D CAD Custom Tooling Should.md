# Shop Technology and 3-D CAD: Custom Tooling Should be in your Customer’s Design Library

[TARİH: 01.11.2015 The Fabricator]

Precision Matters

Fabricating technology and tooling that are unique to the shop can be shared as CAD resources

By Gerald Davis, Contributing Writer

Read more from Gerald Davis at

www.thefabricator.com/author/gerald-davis

I

n this CAD modeling scenario, our fabrication shop owns excellent tooling that is underutilized. We’d like to generate more demand for it. A specific example is shown in

Figure 1a

.

This tooling creates a flanged hole in sheet metal. Also known as an extruded hole, this embossed feature provides better thread engagement with a screw when compared to flat sheet metal. Because it functions like a nut but doesn’t require labor to "install," this sheet metal feature could be a real cost benefit to our customers.

When considering how to impress designers with our shop’s capability, we could distribute the model shown in Figure 1a by posting it on the web for the public to download and admire.

Figure 1a

This CAD model resembles thin-turret tooling for a form-up extruded hole.

Figure 1b

The CAD model of the tooling has all of the detail, springs and screws included. The CAD model also moves to show how the stripper plates move.

Figure 1c

Here’s a CAD model of sheet metal with extruded flange holes.

Other CAD jockeys will admire the variable-pitch stripper spring in the punch head. A few might be impressed with the multibody modeling used in the die core. The pitch and thread engagement is wellmodeled.

(Here is a prediction: Any downloads and demand for this tooling model will be by people who want to make tooling. That’s not our goal. Nonetheless, we want to be faithful throughout the promotion of our capability. If we could download most of this model from the web, that would be ideal. Otherwise, we’ll have to reverse-model the physical item.)

Tooling Is Not a Forming Tool

Figure 1b

shows the internal components in the die set. The top stripper plate is captured with two screws. They adjust the overall height and the preloaded spring compression of the finished assembly. The screws travel up and down with the stripper plate. Sleeves provide friction management for those screws. The die springs are arranged in four pairs to create a balanced lifting force.

As the stripper plate is pushed down, the die springs compress while the screws slide in the sleeves. As the stripper plate descends, the stationary pin in the center of the die will protrude above the stripper plate.

When the pressure on the stripper plate is released, the springs lift to hide the stationary pin. Hiding the die pin except when punching the hole keeps it safe and sharp.

To illustrate the distinction between tooling and the designed product,

Figure 1c

shows sheet metal designed with flanged holes.

Even with those illustrations and an explanation of form-up tooling, a CAD designer who is not expert in the sheet metal trade might not yet see how this tooling matters to their design.

Tool Rules

We could offer a few more illustrations to demonstrate the fabricating process.

Figure 2a

shows a cross-section view of a piece of sheet metal that has been positioned with a pilot hole over the die pin. We could explain to our customer that a pilot hole is required for this process, but they don’t really need to know that.

Figure 2b

shows what happens as the punch is pressed down to sandwich the sheet metal against the die. The sheet metal is bent past the stationary pin in the die. The pocket in the face of the punch tip forces the sheet metal into a ring flange around the hole.

Figure 2a

Step 1: The pilot hole is aligned with stationary pin in die.

Figure 2b

Step 2: The punch pushes sheet metal over the pin to form a flange ring.

Figure 2c

Step 3: The springs eject the sheet metal from the tooling.

The pressure from the punch not only causes the sheet metal flange to form, it also causes the spring in the punch head—Figure 1a—to compress, bringing the punch face and the punch stripper to be in full (hard) contact with the sheet metal.

As described earlier, the die set with its crunched springs is loaded to strip the center pin from the sheet metal.

Figure 2c

shows the sheet metal with the newly formed flange after it has been ejected from the tooling by the springs.

It is likely that you’re reading this article because you have tooling expertise. You haven’t really learned anything yet. But keep in mind that this story is for a job shop’s customers as well. We want something that designers can use, not just fabricators.

So far we’ve described the function of the tooling fairly well with some nice illustrations. We also have 3-D models that we can share. Will our customers be ready to start requiring the tooling for their design? Maybe, but there are rules to using this tool.

If the customer has been paying close attention to Figure 2b, they might note that the punch stripper creates a restriction on the spacing between these extruded holes. For this tooling, the distance is 0.90 inch. This particular tool also creates a 0.125-in. through-hole and works only with 16-gauge mild steel. And it forms only in one direction, so part marking and other formed features either have to cooperate or be fabricated as downstream processes.

These rules and restrictions, along with our explanation of how the tooling works, could be enough for most designers to competently adopt our extruded hole feature into their design—something perhaps like Figure 1c.

For those of our designers who use compatible CAD software, we could go an additional step and make their modeling of our extruded hole easier by distributing a Forming Tool model for inclusion in their design library.

Finding the Right Form

In

Figure 3a

, the example tool model is specifically for a flanged hole for a No. 4 screw thread. To make extraction from the punch easier, the pocket in the punch face is tapered. This results in the extruded flange having the same angle.

The tapered flange along with a slightly reduced outside diameter allows the stationary pin to extrude taller flanges into the sheet metal. It takes more force to accomplish this, but it does give better thread engagement. The wall thickness of the extruded flange is less than the base sheet metal thickness.

Figure 3a

Taper is sometimes required to assist in stripping from the punch. A smaller-diameter pocket forces taller extruding of walls. Extrude too far and the sheet metal fractures or forms a jagged rim.

Figure 3b

To model a Forming Tool, the CAD jockey uses the "Forming Tool" feature to define stopping face and faces to remove on an ordinary part. Note that it is drag-dropped from any folder, but that folder

must be designated as a Forming Tools folder

.

Figure 3c

The Forming Tool is dragged from a Forming Tool folder onto a sheet metal part’s surface. The shadow of the stopping face gives a hint about keep-away. The notes modeled into the Forming Tool also hint at that minimum spacing.

Here’s a CAD Tip: To model a thin-wall feature in a sheet metal design, use a two-step process: Model a bump and add a hole. If the flange thickness is equal to the sheet metal thickness, then the Forming Tool can make the through-hole in one step.

Forming Tools are created as an ordinary part that looks like the interior of the extruded hole. Forming Tools require a "stopping face." The drag-and-drop insertion of the Forming Tool into the model will be onto a face. The tool aligns its stopping face with the face on the sheet metal part. The Forming Tool also can remove sheet metal.

These settings for the behavior of the Forming Tool are saved in its Feature Manager as a Form-Tool1 feature (see

Figure 3b

).

The dimensions used in this Forming Tool model roughly match a No. 4 pilot hole.

Note the following CAD tips:

• Use the shape of the stopping face as a visual aid during drag-and-drop of the Forming Tool into a sheet metal part. In Figure 3b, we see that the keepaway zone is a circle with a radius of 0.900 in.

• An instructional note modeled in the stopping face of the Forming Tool is visible during drag-and-drop as a reminder of the keep-away zone.

Figure 3c

is a screen shot of the Forming Tool being positioned with the tool’s rules visible in yellow. Thanks to tech support from MCAD of Colorado for that tip.

• Give your Forming Tool a good file name to reveal purpose as well as the shop that can manufacture this part.

Sheet Metal Rules

CAD sheet metal isn’t exactly like real sheet metal. CAD sheet metal requires all walls to be equal thickness. Real sheet metal is malleable. Extruded flanges can be thinner than the rest of the sheet metal part.

For an example of three variations in extruded hole models, see

Figure 4a

. The wall thickness of the extruded flange at the left is the same as the base sheet metal’s. It also has zero radius on the inside and outside of the flange. While actual tooling can almost do this, it limits the length of the extruded flange.

It is more likely that there will be some radius in the final sheet metal feature.

We want to make it as easy as possible for our customer to design products that require our tooling. If the Forming Tool model provided to the customer can cut the through-hole too, we will have enabled the model to do it all. The leftmost extruded holes were done in one step with the CAD Forming Tool.

When the wall thickness of the flanges is less than material thickness—as with the rightmost extruded hole—we have to ask the CAD jockey to model the through-hole separately from the Forming Tool.

For designing Forming Tools, the main consideration is the CAD requirement for uniform wall thickness. The inside bend radius of sheet metal has to be a positive value. This means that the outside bend radius minimum is equal to the sheet metal thickness.

Figure 4a

Comparing different Forming Tools in the same sheet metal application reveals curvature results.

Figure 4b

Curves in Forming Tools must be bigger than or equal to the material thickness.

Figure 4b

shows the Forming Tool used to create the middle extrude in Figure 4a. The radius is modeled at 0.064 in. When that is pressed into sheet metal that is 0.059 in. thick, the inside bend radius will be 0.005 in. (0.064 – 0.059 = 0.005). This Forming Tool works with sheet metal up to 0.064 in. thick.

If this Forming Tool is used incorrectly, it will fail in the CAD model. For example, 14-gauge steel is about 0.074 in. thick. The Forming Tool would make a negative 0.010-in. radius, but a negative radius cannot exist.

Making CAD Magnets

Caution: This article is not about engineering tooling. Rather, this is a demonstration of how a shop might document and promote existing tooling capabilities. Punching tooling manufacturers will start with the desired shape you need in sheet metal and create the tooling to produce that shape. The tooling in Figure 1 would be designed by such a firm. The Forming Tool shown in Figure 1a is simply reverse-engineered to achieve the desired result in CAD.

When communicating with our customer to promote this tooling, we offer:

A CAD Forming Tool design feature for drag-and-drop modeling of extruded flanges.

Recommendations for spacing, materials, and screws.

An example of a sheet metal part made with our CAD Forming Tool.

Illustrations and models explaining the operation of the tooling.

Gerald Davis uses CAD software to design and develop products for his clients at

www.glddesigns.com

. Please send your questions and comments to

dand@thefabricator.com

.