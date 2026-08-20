# What’s a surefire way to revise a design in CAD?

[TARİH: 01.05.2020 The Fabricator]

Expertise » Precision Matters

These tips can help a CAD jockey avoid headaches when taking into account design changes

By Gerald Davis

Read more from Gerald Davis at

www.thefabricator.com/author/gerald-davis

Gerald would love for you to send him your comments and questions. Please send your questions and comments to

dand@thefabricator.com

.

T

he spawning of the design shown in

Figure 1A

is discussed in the previous episode of this column. Pack and Go (a brand-specific CAD tool) is useful for creating functional templates for drawings and starting models based on an existing design.

The enclosure shown in Figure 1A is designed to store an imaginary FMA cartridge and something that strongly resembles a grease gun. ("Pump in some FMA to make things easier! It’s that sort of thing.) The intent of this contrived mash of models is to provide context for various CAD tasks without violating any patents. The work flow described is specific to a brand of mainstream 3D CAD.

FIGURE 1A The concept of a lockbox of pumpable FMA is a success. That’s the good news. The revision news is that this box is resting on its back because there is no other good way to use it. The hinged door is awful and the top wants to be the bottom.

FIGURE 1B The REV A PDF has been marked up to document the changes needed for REV B.

Memo From Product Development

We have received good news after a month of testing: The basic product concept is good. We are keeping it pretty much the same size, color, and description. In other news, it is proven that the side-hinged door is frequently discarded after first use.

These needed changes to the design have been documented. See

Figure 1B

to find out what REV B shall be.

To summarize the needed changes, we need to move the hinges to the door’s long side and orient the box so there is a work tray at the top. Basically, the roof and floor swap descriptions and function. It also would be good to have holes for hanging this box on the wall—16-in. centers, according to most building codes in the U.S.

Here’s some insider knowledge: Several commitments were made in a revision planning meeting. There is no existing install base or inventory of this product to retrofit. As a result, extensive revision of the design is permitted. We’ll track the activity and history of change with an engineering change number. The author held such a planning event, of course.

Revision Versus Branching

A CAD jockey recognizes the two aspects of revision: things that are functional and things that are CAD administration. CAD admin includes folders, file names, and adherence to naming and description conventions.

Keep in mind that a branched design is a fork in the road; backwards compatibility is not an issue. Revisions are more sensitive to the past than branches. Functionally, it is sometimes possible, or even required, that a revision be backward-compatible with prior art.

Since the revision level is not included in our CAD file names, the file names used in this project will not be changing. Regardless of function, preservation of parametric links is the main CAD-related distinction between revision and branching.

Preserving the CAD links between files is vital. Pack and Go is recommended over Windows Explorer for changing file names. Again, that is discussed in the previous column.

FIGURE 2 The use of the Pack and Go tool to make zip files is a quick way to archive a design before updating files to a new revision.

The revision planning team has responsibility to define the mission well and thus restrict the expansion of the revision’s scope.

Because the file names are not changing in this demonstration, the parametric links between files are not in jeopardy. Nevertheless, Pack and Go is a go-to tool. It shall be used to create an archive file of REV A before burning bridges in CAD.

Safety First

This scenario is presenting a minimalist approach to CAD archiving. The internet provides modern CAD software (not discussed here) that provides backup and retrieval of prior art as an integral feature of the CAD. That is an ideal work environment. Without naming brands, sketching things up or online shaping offers your studio a very efficient and productive work flow.

If your goal is to be robust—to be able to model even when the internet is intermittently there—you always have old CAD. Good ol’ mainstream 3D CAD software started out life with minimal internet of things. To some extent, it can even run without an internet connection. It thrives on a restricted intranet.

Disclaimer: This scenario is presenting a minimalist approach to CAD archiving. A better approach is to use a product document management (PDM) add-in to provide a "vault" for collaborative access.

FIGURE 3 The completed REV B model shows changes to the location of hinges and hasp, moves the top to the bottom, and adds wall-mount holes.

FIGURE 4 The REV B drawing provides an audit trail via the revision history table to supporting documents that fully describe the change. In this example, a link to subscribe to

The FABRICATOR

would probably be better than a reference to my imaginary engineering change log.

An early step in our demo of recommended revision processing is to use Pack and Go to create an archive zip file that includes the drawings and decals.

Figure 2

is a screenshot (note the red boxes) emphasizing two settings in Pack and Go—Include Drawings and Save to Zip File. Or, if you have a PDM tool, you could check it into the vault and be happier.

The CAD team has made the changes happen.

Figure 3

shows the resulting REV B product line:

• The floor is now the roof.

• Holes for hanging are in place.

• The hinges are on the long side of the lift-off door.

• The door has a hem bend to create a friction latch.

• The friction latch has a hole (was slot) for a padlock.

• The hasp has an embossed dimple for friction latching.

• The hasp is located with a pair of half shears for a spot welded self-fixture.

• The hasp has FMA as a brand-logo feature. So nice.

A screenshot of the first sheet of REV B PDF is shown in

Figure 4

. The rev table has the engineering change number and revision bump. The bill of materials table shows Items 2 and 3 have exchanged their descriptions with each other.

To see the full PDF and to review nuanced details of the CAD files, download zip files of FMA Make Easier REV B. The model for the grease gun is almost good enough for manufacturing.

We conclude with a wagging finger. The revision planning team has responsibility to define the mission well and thus

restrict the expansion

of the revision’s scope. Mission creep is a threat to progress. It’s perfection at the expense of the good.

We gave ourselves free reign in this demo. For example, adding the FMA logo to the hasp (see

Figure 5

) is lovely but adds expense. Who authorized that, Gerald? Is it an essential expense? Will the customer treasure this enclosure more with an indelible FMA emblazoned upon it?

Sucking gums and glares. The final review meeting may not be final.

FIGURE 5 REV B includes an embellishment to the hasp. FMA is indelibly cut into the part before it is spot welded to the top using a pair of half-shear dots to self-fixture this snap-lock friction latch. Is this mission creep or something that the end user will truly value?