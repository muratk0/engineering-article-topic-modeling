# When working with CAD sheet metal, workflow options exist

[TARİH: 01.12.2024 The Fabricator]

Precision Matters

Merits of a short feature history and speed of rendering and completion help to identify the right workflow

Gerald Davis

S

heet metal in the CAD modeling world implies that coining or bending a flat workpiece is part of the process to fabricate the finished product. Getting bent makes sheet metal distinct from industries based on carving or depositing a billet.

In

Figure 1

, we compare a pair of modeling approaches for a sheet metal bracket. Disclaimer: These are only two of many possible workflows.

The upper bracket was modeled using a sketched base flange, a CAD technique that is recognizably sheet metal oriented from the getgo. This is perhaps best for design for manufacturability (DFM).

The lower bracket has a feature history of once being a boss-extrude (almost any shape). Any extrude can be converted into sheet metal. Have faith! Design exploration and then final adoption of sheet metal are perhaps best for a CAD model’s development.

CAD software tries to mimic the reality of sheet metal with a suite of Sheet Metal tools, which grant the model the ability to behave similarly to actual sheet metal. In particular, we are interested in the software’s ability to fold or flatten the model with a mouse click. Perhaps we also might be interested in using that functionality to resolve a tear where two bends intersect.

The behavior of a well-behaved sheet metal model is useful when optimizing for DFM. If the model won’t unfold, it is not well behaved.

The Sheet Metal tools we’re talking about are handy in CAD, but not essential to design development. If flat pattern functionality is needed, it can be added at any time with the Convert-to-Sheet Metal tool, as hinted at by the workflow for the lower bracket in Figure 1.

FIGURE 1 Two workflows are compared. Both result in about the same bracket. The upper workflow starts with a sketch for a base flange that will unfold. The lower workflow converts a boss-extrude into a sheet metal feature that will unfold. One workflow has fewer steps in its feature history.

FIGURE 2A A workflow sequence (for the upper bracket shown in Figure 1) for a sheet metal bracket is shown (left to right, top to bottom). The sketch locates the bend. The base flange adds thickness. The edge flange can be added with a couple of clicks, and so forth. A CAD sheet metal model will unfold (given correct thickness, radius, and k-factor) to predict the actual flat layout.

FIGURE 2B Contrast this workflow with that in Figure 2A. The sketch creates a boss-extrude. Convert-to-Sheet-Metal adds thickness and defines all of the flanges. In this example, the process saves a step with corner reliefs. This CAD sheet metal model will unfold (given correct thickness, radius, and k-factor) to predict the actual flat layout.

FIGURE 3 The Hole Wizard creates a pattern of holes. That pattern can be used to create a pattern of components. In this example, captive studs are part of the assembly with the sheet metal bracket.

The Best Workflow Is On Time

Ideal workflows result in fewer steps in the feature history, make it easier for the computer to resolve, and are intuitive for the human to apply and revise. The incentive behind fewer steps (i.e., shorter history listed in the Feature Manager) is less labor. If it takes more time to model with fewer steps, the return is diminished. To put it another way, sketching circles is muscle memory; setting up the Hole Wizard takes several moments to master and basically results in sketched circles. Is it worth taking the time to be elegant?

Here’s a CAD tip: The Hole Wizard is your best friend. Sketch dots instead of circles.

The incentive behind modeling for light weight under the mouse (fast rendering by the computer hardware) is joy. Technique for speed becomes more important with components that will be used many times in a large assembly, such as washers and bolts. It is a victory to model efficiently while being on or ahead of schedule.

Here’s another CAD tip: Model washers with revolves, not with boss-extrudes.

Intuitive workflow is used here as shorthand for optimized for fabrication. A nice model has a logical progression from start to finish. Fewer steps in the model’s history aides subsequent review and revision. We could have modeled the bracket starting with a flat layout and added bends. If that workflow makes it easier to develop the design, do that.

The Get-Go or Finishing Touch

Figure 2A

shows steps in a workflow that starts with a sketch to create the base flange. The sketch sets flange positions and angles. It is basically one surface of the part. You decide whether it is inside or outside.

The sketch mostly locates flanges, whereas the base flange feature that uses the sketch controls the material thickness and bend radius. The base flange feature also retains data for flat-layout compensation for the stretching that occurs when the sheet metal is bent (k-factor).

From starting sketch to flat layout, Figure 2A shows seven steps, described as follows. An edge flange is added to a base flange. Then, corner reliefs are added where bends intersect. The sharp sheet metal corners get filleted for safe handling and for a laser-friendly profiling path.

The Hole Wizard creates a pattern of holes for locating a pattern of captive studs.

Here’s one more CAD tip: Use

up to next

for the hole depth for a more readable hole callout for drawings

.

In critiquing the workflow in Figure 2A, the person doing the modeling must understand commonly available gauge thicknesses and bend radii. The press brake tooling used affects the bend deduction, so familiarity with the CAM standards for the production line helps.

One of the rules of sheet metal is that the material must be of uniform thickness. The sheet metal tools used in Figure 2A automatically comply with that rule. This workflow emphasizes the appearance of sheet metal as the design evolves.

Another rule of sheet metal is that flanges cannot intersect with each other. When the edge flange was added in the third step, the software warns of problems with impossible features.

Figure 2B

shows an alternative workflow that adds sheet metal functionality to a solid body. We’re taking advantage of the fact that the Convert to Sheet Metal tool assures the uniformity of thickness. Almost any blob can become a bracket. Here, a box becomes a bracket with three bends in one step as thickness is automatically created during conversion.

This is a fancy trick for a magazine article; it would be more intuitive to model the solid body to look more like sheet metal before converting it into sheet metal.

Figure 2B only took six steps, whereas Figure 2A burned up seven. The best workflow is the one that gets the job done. The freedom to model with familiar extrudes and cuts (without obsession about the rules of sheet metal) can be liberating. On the other hand, the discipline of modeling with the constraints of sheet metal fabrication in mind can avoid dead-end designs.

CAD/CAM and the Friendly Flats

The preceding has been said from the perspective of inventing the design. When it comes to fabrication of the design, the designer is likely to export the native CAD model as a STEP file. It does not matter if the part was modeled utilizing a base flange or base extrude. That nuance is lost in the STEP file; only the final shape is retained.

The fabricator imports the STEP and adds CAM functionality to the model to unfold it. If both parties are using the same CAD software, the Convert to Sheet Metal tool is used on one of its children. Savor the ironies of fabrication.

The CAD Jockey, of course, verifies that the part is without error before exporting it as a STEP file. Should sheet metal parts be exported in a formed or flat condition? Or both? Only the CAM crew for the production line knows best. Ask them. The following is a probable answer.

The STEP file (or whatever exchange file format is in use between CAD and CAM) is a form of buddy check or verification of compliance with sheet metal rules. By exporting the formed part, you convey the goal for the completed item. You trust the fabricator to be able to adapt the bend deduction and bend radius to achieve whatever flat pattern is needed to meet the goal.

By exporting the flat part, you are requesting to receive that flat part. You are taking responsibility for forming the part as needed.

To recommend the value of the Hole Wizard for creating patterns,

Figure 3

shows the future of this sheet metal part. It’s to be swaged with captive studs, something discussed in a past episode.

Gerald would

love for you to send him your comments and questions. Please send your questions and comments to

ddavis@fmamfg.org

.

4 ROLL HYDRAULIC DOUBLE PINCH PLATE BENDING MACHINES

REAL WORK HORSES

FROM TENNESSEE • MADE IN USA

The 403 Series from WDM.

Over 40 years of experience with 3 generations working in the business.

Built in USA with American and global components.

30 gauge to 1″ thick, 1′ to 12′ wide.

Custom and built to order options available.

We are a dedicated business specializing in customer service and lasting customer relations.

From complete custo many popular/standard machines in stock.

Waldemar Design & Machine LLC

224 Pierpont Street

Petersburg, WV 26847

606-787-8474

sales@wdmrolls.com

www.wdmrolls.com

Contact us direct, or contact your favorite machine tool distributor and ask about WDM Machine Tools.

3 & 4 Roll Hydraulic Double Pinch Plate Bending Machines Initial Pinch Sheet Plate Bending Rolls • Bending Systems & Complete Forming Cells

THE Next-Gen Metal Fab

PODCAST

PODCAST NETWORK