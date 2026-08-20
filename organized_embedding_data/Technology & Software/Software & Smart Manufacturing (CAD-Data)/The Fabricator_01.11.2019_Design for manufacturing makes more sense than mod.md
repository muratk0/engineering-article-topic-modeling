# Design for manufacturing makes more sense than modeling for procurement

[TARİH: 01.11.2019 The Fabricator]

Expertise » Precision Matters

Design intent for the 3D modeling technique may anticipate the BOM preparation for the purchasing department

By Gerald Davis

Read more from Gerald Davis at

www.thefabricator.com/author/gerald-davis

Gerald Davis would love for you to send him your comments and questions. You are not alone, and the problems you face often are shared by others. Share the grief, and perhaps we will all share in the joy of finding answers. Please send your questions and comments to

dand@thefabricator.com

.

D

esign and CAD modeling tasks include determining the form of raw material for fabrication of the product—billet, sheet, or something off the shelf. If the purchasing department can obtain it without sending out a drawing, then it is easy in CAD, requiring just an entry in the product manufacturing information (PMI) system. In contrast, modifying something that is almost finished can lead to interesting modeling and documentation issues.

We will review the bittersweet inspiration for this article in a moment, but feel compelled to start with a happy scenario to protect the innocent.

Figure 1

The product starring in this episode features a welded cap on one end and machined pipe threads on the other end. The end cap is easy; just buy it. How to make the threaded tube is the question we are left to ponder.

Cap It Good

Figure 1

shows an example product, a welded end cap on threaded pipe. Of course, one should model weld beads for magazine articles. In the real world, our objective is to document how to fabricate this product. We are fully enabled CAD jockeys, with power to issue part numbers and to determine raw materials.

Warning. Harmonious analogy lies ahead. The part numbers used in this scenario will be a chorus to the verse of BOM tables.

A welded cap on a chunk of pipe may seem to be a trivial design problem. For our purposes, it is a useful example of modeling for when modification of any off-the-shelf item is the plan.

Possibilities for this product include carving the parts from billet or tubing, which would give better quality control on wall thickness and thread engagement, but we don’t really need that in this scenario. Our goal is to use off-theshelf material at every opportunity.

Figure 2

This drawing has a bill of materials table that shows the parts required: a pipe and a cap, M00121 and P00541, respectively. See Figure 3 for the drawing for the pipe.

Whack It in Half

Figure 2

presents one method of manufacture—cut an off-the-shelf, double-ended standpipe in half and weld a cap onto it. This creates two parts out of one billet. Note that

Figure 3

is required to explain how to cut the pipe in half.

Well, why not just buy a single-ended threaded standpipe and weld a cap onto that? That’s a good idea as well. Please see

Figure 4

. That alternative method of fabrication gets it done with just one drawing instead of two drawings, one assembly instead of two assemblies in CAD. It eliminates the mystery of the kerf width (required to cut finished parts in half). In the situation where an off-the-shelf length for a singleended standpipe is suitable, we have a winner.

In the event that the design is likely to change to call for a unique overall length and that the part-off piece also could be used, making the two-parts-from-one-billet idea somehow practical, then Figure 2 might be an approach.

The efficient-minded tendency in 3D modeling is still to model a single-ended standpipe to some finished length. There’s no need to model both ends in CAD and then delete one of them, unless the CAD model needs to show the sequence of fabrication. Oh, such is the agony of opportunity.

This tempest in a teapot puzzle regarding modeling-for-procurement is useful for illustrating some nuances in the bill of materials—the BOM table. Please compare the BOM in Figure 2 with the BOM in Figure 4.

BOM Rules

Very similar to each other, both BOMs list a standpipe and an end cap, and both BOMs have the same entry for item 2: the end cap with our assigned part number P00541. The difference between these two BOMs is in their item 1—the standpipe. Is it made or bought?

M00121 and P00784? In 3D CAD, half-pipe M00121 is an assembly file that cuts full-pipe P00540 in half. P00784 is a part file for a readymade half-pipe.

These part numbers lead us a bit further into digression. "Why not use the vendor’s part number instead of assigning our own?" BOM item 1 in Figure 4 is 9157K776. That is something that can be googled. P00784 is an alias that has little meaning to the world.

Figure 3

The BOM on this drawing shows that an off-the-shelf, double-ended pipe is the raw material. Cut the pipe in half to make the single-ended part we need.

Figure 4

An alternative method of fabrication is to purchase a single-ended pipe and weld an end cap to that. No custom drawing is needed for the pipe.

Glad you asked that question. The use of inhouse part numbers for everything has two benefits—consistency and the opportunity to use "equivalent" items. As may be seen in Figure 2, the BOM table has a column titled "Equivalent Okay." Neatly prepared drawings are a blessing. Vendor part numbers have random lengths and can sometimes mess up our pretty BOM table. By assigning part numbers, we can predict how they will appear in the BOM table.

If an equivalent item is commonly available from several vendors, such as an end cap for pipe, our assigned alias part number can allow any of those alternative vendors to be part of the supply chain. The meaning of equivalent is tricky. Metal is not equivalent to wood—usually. One can imagine situations where they might be, but common sense must prevail.

While sharing the secrets of our in-house part number system, the world is made up of A, B, and C. We assemble things in-house; those are the "A series" players. Some of the things we assemble per our A series drawings are made to our specification; those are the "Make this" items. Most of the things we assemble are purchased designs that we trust others to fabricate and thus document. You already figured it out! "P" in the part number means it can be purchased without sending out a drawing to get it right.

Why model a part with two threaded ends and then cut one of those ends off? To preserve the source and PMI for the raw material, in this example an off-the-shelf item.

Policy and procedure drive how the 3D model contains the PMI. In other words, the organization and naming of models in 3D space must comport with rules for names and tables. Every organization has its own evolving policy. Our AMP (A series-Make this-P!) naming convention is offered for reflection more than as advice.

Policy and procedure drive how the 3D model contains PMI. In other words, the organization and naming of models in 3D space must comport with rules for names and tables.

The Worst-case Scenario

Back in the day when Company B came up with this part number system, it needed a 24-inch standpipe. Wonderfully, 4813K81 was available online so the CAD department assigned P00540 to it. As time passed, the R&D guys grabbed one of those P00540s out of inventory; whacked it in half; welded caps onto the pair; and proclaimed it to be a design, which they conveyed with a thump onto the desk of the CAD department for proper documentation.

The CAD jockey followed instructions. The P00540 part file was modeled in an assembly for the benefit of being cut with an assemblycut feature CAD technique. The resulting body is the "part" that carries the PMI of M00121, as well as P00540, into the database that is corporate memory. The design intent used was simple—"model it the way it is made." The result is a part, another part, an assembly, and another assembly was not necessarily simple.

When the design for cost optimization was reviewed, it was noted that a large inventory of welded M00016s were out in the barn—twice as many as needed. CAD policy had created the need to create a custom version of an off-theshelf item, produced at twice the rate needed, without informing purchasing. The guys in production couldn’t help themselves. They welded caps onto every M00121 pipe that they sawed into existence.

Thus Figure 3 is obsolete. We could have started with that, but then this would have been a very short article.