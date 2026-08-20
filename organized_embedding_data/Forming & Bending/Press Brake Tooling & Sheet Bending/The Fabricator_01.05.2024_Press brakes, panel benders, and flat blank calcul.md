# Press brakes, panel benders, and flat blank calculations

[TARİH: 01.05.2024 The Fabricator]

Bending Basics

Be prepared for some changes

By

Steve Benson

Question:

For years, we have been bending most of our parts on press brakes, and our solid models were created with the intention of being run on them, incorporating the applicable k-factors, bend radii, bend allowances, and bend deductions. Today, we’re processing parts through automation that incorporates panel bending. In theory, we believe we shouldn’t have to change the drawings. The software should bring in the drawings and unfold them with its own variables. Nevertheless, we have been struggling with part fit-up in assembly. We’re using the same flat blank, but we seem to be achieving a new inside bend radius.

The software seems to be unfolding with different variables. And the machines do have tables for angle corrections, bend deductions, and air gap settings, but we don’t want to just start adjusting values and "fudge it."

All this said, why do the flat blanks differ when we form them on a brake versus a panel bender? We think this might be making our parts difficult to assemble. What makes panel bending unique, and is the action similar to a leaf brake, where the sheet is also clamped in place and folded? What exactly are the differences between bending on a press brake and a panel bender, and is there a way to update our part files to better accommodate the process?

Answer:

From my time on the shop floor to the hundreds of shops I’ve visited over the years, I can say that many have similar issues after purchasing new equipment. Is there a way to ease your current situation without rewriting every program? I can’t say for sure. My knowledge of your situation is somewhat limited, though there might be ways to improve things, depending on the specific challenges you’re facing. Regardless, I can give you some foundational information that should give you a good place to start.

So, why are you encountering differences between parts formed on a panel bender and parts formed on a press brake? These differences arise for many reasons, but let’s look at a few of the bigger ones.

Machine Dynamics

Panel benders and press brakes have different mechanical abilities and dynamics. The way in which they apply force, the rigidity of the tools, and other machine-specific factors lead to variations in the final formed part. The tooling can vary in terms of material makeup, surface finish, wear, and precision. These differences affect how the sheet metal reacts during bending, especially over varying forming styles and methods.

Even though you might be using the same material, variations in grain direction, thickness tolerances, and other mechanical properties can always be a factor. These affect how the material behaves during bending and, ultimately, the size and shape of the inside bend radius. The inside bend radius also can vary depending on the bending machine you use (panel bender or press brake), material properties, and the tooling your machine uses.

Panel Bender Versus the Leaf Brake

Panel benders typically produce a tighter inside bend radius when compared to leaf brakes. This is because they typically use a specific wiping action for the bending process, allowing for a tighter radius without excessive material deformation (see

Figure 1

).

Panel benders have tight control over the bending process and use specialized tooling, which means the size and shape of the inside bend radius can be very consistent and predictable. Of course, the variations will depend on the equipment, tooling, and process parameters you use.

Although less consistent than panel benders, leaf brakes can produce a broad range of inside bend radii depending on the tooling setup and the bending process parameters (see

Figure 2

). The inside bend radius formed on a leaf brake is influenced by factors such as the clamping method, the force applied during bending, and the material’s behavior under pressure. Compared to panel benders, which wipe the workpiece, leaf brakes may be limited in achieving very tight inside bend radii, particularly for thicker or harder materials.

FIGURE 1 A panel bender’s tools wipe the flange up or down. The approach usually makes the inside bend radius very consistent and repeatable.

FIGURE 2 This restored Cornice brake is a thing of beauty. It clamps the material in place, after which the apron swings upward to form the bend around the tool. These old machines, and their modern manual cousins, might be less consistent than CNC brakes and panel benders, but depending on the tooling setup and other parameters, they can produce a broad range of bend radii. Fun fact: The first Cornice brake was patented in the U.S. in 1882.

FIGURE 3 In air forming, the radius is "floated" in the die. The resulting inside bend radius forms as a percentage of the die opening.

zilber42/iStock/Getty Images Plus

Panel Bender Versus the Press Brake

Press brakes use a punch and die setup in which the punch applies pressure to the material from above, and the sheet material is supported by the V die below. Air forming on a press brake relies on applying pressure to the top of the material using the punch while the underside of the material rests on the V die. Press brakes allow for more flexibility in achieving different bend angles and radii.

The shape and size of the inside bend radius can vary based on the geometry and condition of the tooling. The inside bend radius can "float" (see

Figure 3

), as in air forming (where the radius forms as a percentage of the die opening), or it can take on the punch nose radius, as in bottom bending.

The material’s behavior under pressure can differ between press brakes and other bending methods. When air forming on a press brake, the material tends to flow more freely, which can affect the final shape of the bend and the inside radius. Parameters such as bend angle, bending speed, and tooling setup can influence the shape and size of the inside bend radius.

While press brakes offer versatility and flexibility in bending a wide range of materials and thicknesses, the shape and size of the inside bend radius may vary compared to panel benders or leaf brakes due to differences in process control, tooling, as well as the way they handle material. Be sure to consider these factors when selecting the appropriate bending method.

How to Move Between Machines

As you can see, because panel benders form differently, they require unique considerations, especially if you’re moving parts that were previously formed on a press brake. As you state, software does account for these differences, but you also need to consider other operational variables, including what assemblers need to fit pieces together as intended. Again, this will depend on the geometries you’re assembling and the tolerances you’re holding.

Next month, we will look at ways we might be able to move projects between different machines and processes seamlessly. As it is with so many challenges in forming, a lot can be solved with good documentation and communicating information effectively to everyone who needs to know, including programmers, operators, and quality control.

Steve Benson

is a member and former chair of the Precision Sheet Metal Technology Council of the Fabricators and Manufacturers Association. He is the president of ASMA LLC,

steve@theartofpressbrake.com

. Benson also conducts FMA’s Precision Press Brake Certificate Program, which is held at locations across the country. For more information, visit

www.fmamfg.org/training

, or call 888-394-4362.

Every profile, a Work of Art.

Dalian, since 1978 the avant-garde in Italian engineering and design.

Specializing in precision roll forming machines and systems for thin material processing, we stand at the forefront of innovation, efficiency, and environmental respect. Our production lines, the result of over 45 years of research, offer unmatched performance:

speeds up to 3901pm/min

, advanced automation caple of

reducing labor by up to 75%

, and

material consumption reduction by up to 15%

.

Dalian America Corp.

18 Bridge Steel, Unit 2°

Brooklyn NV 11201 USA

sales@dallanamerica.us

-

www.dallan.com

RESISTANCE WELDING

ONE-STOP-SHOP

New & Used Machinery Consumables & Supplies Service & Process Training

INDUSTRIAL

WATER CHILLER

HUGE SELECTION OF WATER CHILLERS

IN STOCK!

TJSNOW.COM

CALL (800) 669-7669

Have you ever seen anything like this?

It picks, fits, and welds without a programmer. Without a welder.

Learn more about our AF-1 Cell and see how it can help with your high-mix, low volume welds.