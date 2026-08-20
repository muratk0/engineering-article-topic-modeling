# Can this Product be Made?

[TARİH: 01.05.2016 The Fabricator]

Biz Talk

If one industry project is successful, designers should know from the start

By Tim Heston

Read more from Tim Heston at

www.thefabricator.com/author/tim-heston

F

ollow a job through a competitive fab shop, and you can see its parts come together quickly. Inventory buffers may be there for outsourced processes like powder coating or plating, but for the most part, work is on the move.

Then in the front office you have the inbox, either physical or electronic. Why is a job pending? Because the engineer is checking with the customer on a specification, and the customer has to check with his engineering team to approve the change. And people on that engineering team are handling umpteen other projects, so it takes hours or days to hear back. Then another question arises, and the job parks itself again in the inbox, waiting for a response.

In recent years many fabricators have told me how they’re now focusing on front-office operations more than ever. They realize how much time orders, especially new ones, spend going back and forth between departments, customers, and suppliers. It remains a weak, inefficient link in a supply chain aiming to be lean.

Many blame the problem on the fact that, well, people are busy. Engineering departments downsize. People leave their jobs and new hires take up the reins (often before they really know how to ride). A lot of manufacturing experts are aging or retiring. It’s just the nature of the beast.

But is it really? This problem in part can be organizational. For instance, some shops have attempted to tear down the walls between different departments—sales, estimating, engineering, purchasing—to create front-office "cells." A salesperson can roll his chair over to the engineer to ask a question, then talk to estimating two steps away. Everyone is in constant contact.

This is a great thing, but if it’s all about basic manufacturability, why are people asking these questions now, right before the job is scheduled to hit the production floor? Why weren’t these questions asked at the very start?

For that matter, why do basic manufacturability questions need to be asked at all? These aren’t queries up for philosophical debate but instead are based on physics: what a manufacturing process can or cannot do to specific materials. Couldn’t this be handled by software, at least to some degree?

To some extent it is already. Companies like aPriori have offered design for manufacturability (DFM) tools for product designers for years, providing detailed cost estimates that allow designers to think about the best manufacturing path to take. And a project called iFAB aims to broaden the scope.

"We’re making it more accessible to the designer. It makes it less ethereal and more of a synchronous process."

So said Mark Traband, PhD, a project lead for iFAB and head of the Manufacturing Systems Division of the Applied Research Laboratory at The Pennsylvania State University.

"We’re making [design for manufacturability] more accessible to the designer. It makes it less ethereal and more of a synchronous process."

— Mark Traband, PhD, The Pennsylvania State University

Imagine a designer finishes one iteration of a product in CAD and saves it in a format that captures the product manufacturing information such as material type and characteristics, heat treating, and plating requirements. (The emerging STEP AP 242 standard is one such format, Traband said, but added that iFAB isn’t limited to it.)

The designer then clicks a few buttons in the CAD window, which instructs the software to push information out to a server on the cloud. The server then uses a mix of costing software technologies, including aPriori but also others, such as an assembly planning tool from Penn State and another costing tool from Ohio State. In seconds the system sends the designer a PDF of a costing report for that specific part or assembly.

Traband added that the costing function can be tailored for specific operations. The framework is all open source; the code is free and accessible. On top of this framework, companies can add specific (and proprietary) costing variables pertaining to their operations, their manufacturing machines, methods, and materials.

iFAB isn’t short for iFabrication. It’s an acronym that stands for Instant Foundry, Adaptive through Bits. In this case, a "foundry" is a network of manufacturing capabilities tied directly to the product.

Work on some of the elements behind iFAB began under the Adaptive Vehicle Make (AVM) project sponsored by the Defense Advanced Research Projects Agency (DARPA). In essence, AVM aimed to make developing the next-generation combat vehicle (and, more broadly, any DOD project) much more streamlined, flexible, and less expensive.

When the AVM program ended in 2014, the iFAB program was handed over to the Digital Manufacturing and Design Innovation Institute, or DMDII (

dmdii.uilabs.org

), a federally funded R&D organization of UI Labs, based near Chicago.

"This represents some of the tools we at DMDII are trying to promulgate into industry," said George Barnych, DMDII’s director of R&D programs. "And this [iFAB] project is just one of them."

The project is being tested by DMDII industry partners, each of which has used company-specific, proprietary costing information on top of the basic open-source structure of iFAB. The idea is that once a designer finishes his product design, he’s been fed manufacturability data all along the way. From here, CNC programs, assembly planning, even work instructions are then automatically generated. Prepping a new product for manufacturing is boiled down to a few mouse clicks.

Traband said that this program, particularly the nearly instant manufacturability feedback, may have implications in the custom metal fabrication space. He added, though, that iFAB isn’t meant to be a mechanism for manufacturers to just put pricing pressure on suppliers. The goal is to give designers comparative costing information: between machining and waterjet cutting a plate, for instance. It really doesn’t provide something that reflects a negotiated price with suppliers, each of which can have different costs depending on how they operate.

iFAB brings to mind some big possibilities. No longer would a CAD technician be sending or leaving voicemails, asking if, say, a certain hole could be moved a little farther away from the bend radius. Instead, a fabricator’s engineers could spend their days analyzing in-depth concepts about product designs and manufacturing processes. That adds a lot more value than the tedium of checking part after part, radius after radius, sheet edge after edge, hole after hole, just to make sure the machines on the floor can make them.