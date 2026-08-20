# Nesting and the fiber laser

[TARİH: 01.01.2014 The Fabricator]

The software doesn’t have to change, but the process thinking might

By Dan Davis, Editor-in-Chief

All a fabricator had to do was walk around at this year’s FABTECH, North America’s largest metal fabricating tradeshow, to take notice of the fiber laser cutting machines on the show floor. All of the well-known machine tool builders had their versions there, and even smaller, not-yet-known companies exhibited cutting machines built on fiber laser technology. The one-time cutting curiosity is now a full-blown fabricating force to be reckoned with.

If the technology turnout at the tradeshow wasn’t evidence enough of the fiber laser’s permanent place on the fabricating landscape, industrial research backs up the observations. Today fiber lasers represent about 17 percent of the overall laser metal processing market, according to “The Worldwide Market for Lasers” (2013) from Strategies Unlimited, and that market share is expected to increase to 30 percent by 2015. Looking at near-term growth, the publication

Industrial Laser Solutions

suggested in its “2012 Annual Economic Review and Forecast” that fiber laser sales were expected to grow by 7 percent in 2013, while sales of more traditional CO

2

technology actually were going to contract by 1 percent in what was expected to be a relatively flat market. The adoption rate for fiber laser cutting equipment is only going to increase as fabricators become more comfortable with the long-term viability of the technology and developers improve cutting performance across the range of material thicknesses.

So if this exciting cutting technology is here to stay, what happens to the processes that surround the fabricating activity? Machine tool builders and automation experts have altered material storage and retrieval towers and part loading systems to keep up with the increased cutting speeds of the fiber laser machines. On the back end, the part removal and sorting is a bit more complicated, but again, the machine tool builders are hard at work showcasing some novel ideas to make that labor-intensive operation more efficient.

What about nest creation? In all honesty, there might not be that much to worry about.

A Fiber Laser Review

To understand how the fiber technology has changed the traditional thinking about laser cutting, a fabricator needs to know a little about the laser generation process.

Actually, if you look at the origin of “laser,” you see that it is an acronym derived from Light Amplification by Stimulated Emission of Radiation. It’s all about getting electrons stimulated—or “amplified”— so that they give off photons. The photons proliferate during this excitation phase and a focused light, or the laser beam, is created.

Most in the metal fabricating industry know that CO

2

gas has been the dominant laser-generation medium as it relates to machinery used to cut metal. CO

2

and other gases are found in a laser cavity where the electrons are energized, photons are produced, and mirrors reflect the photons back and forth to create the laser beam. The laser is then guided through a series of mirrors to a cutting head where the 10-micron-wavelength beam is released.

CO

2

laser cutting machines have been the industry workhorse for a couple of decades. They cut a variety of metal thicknesses, and machine tool builders have worked hard to make them much more user-friendly, with modern touchscreen controls and automated laser lens and cartridge changeout. However, the units still rely on lasing gases and require regular maintenance, such as replacement of mirrors.

Fiber laser technology debuted in the metal fabricating industry for the first time in a major way in the Salvagnini L1Xe at the 2008 EuroBLECH trade-show. These solid-state lasers use multiple laser diodes to generate electromagnetic wavelengths that are fed into double-clad fiber-optic cables, containing rare-earth elements, where the excitation process takes place.

The fiber laser beam that is generated doesn’t require any complicated optical systems to be delivered to the cutting head. This makes the 1-micron-wavelength beam very stable when used in metal cutting applications, which translates into high-tolerance cuts. Because of the lack of mirrors and beam compensation systems (the beam path length never changes), the cutting head is light and compact, enabling it to be moved at higher speeds when compared to traditional laser cutting heads.

Indeed, this has resulted in fiber laser cutting systems that can cut twice as fast as CO

2

systems (see Figure 1) in the thinner range of metal, such as 20 to 22 gauge. Recent developments showcased at 2013 FABTECH indicate that technology improvements related to beam size control has fiber laser cutting machines closing the speed gap with CO

2

lasers in the thick range of material, too, said to be more than 0.25 in. Fiber lasers are speedily making inroads into job shops because they are demonstrating the ability to cut all materials quickly.

Figure 1

Positioning speeds of fiber laser cutting heads are incredibly fast, with most surpassing 4,000 inches per minute.

Does the Speed Affect the Nesting?

With this increase in cutting speed, fabricators have to wonder if nesting practices should change or if nesting software algorithms have been altered to accommodate the new capabilities. For the most part, the answer is no.

“We can take pretty much any of our programs from our machines and throw that on the fiber laser and it will run just fine,” said Steve Aleshin, Salvagnini’s applications manager for laser cutting.

What about the smaller beam size? Does that translate into tighter nests? “That only really applies when we do our common cut because we do account for the kerf width so that you still get an accurate-sized part,” Aleshin said. “Again, that would just be a setting change that already existed [in the machine control].”

What about the material being cut on the laser? The fiber laser’s short wavelength means it can cut highly reflective materials, such as copper—something that isn’t easily done with CO

2

lasers. Does that alter the nest layout? “Not really. Even if you look at the heat generated,” Aleshin said. “Copper is a pretty hot-cutting material, but if that’s a problem, I’m going to treat that like I would treat cutting 0.5-in. material with oxygen using a CO

2

laser. I’m going to jump around on the sheet instead of going through a sequence across the sheet to spread out the heat. So it’s really not a different thought process.”

There Is One Scenario …

For the most part, nesting practices used for a CO

2

laser carry over nicely to the fiber laser. However, if a fabrication operation works with a lot of square or rectangular parts, it might want to consider a specialized nesting layout that takes advantage of the fiber laser’s speed (see Figure 2).

Figure 2

A metal fabricator that cuts plenty of the same-sized square or rectangular shapes might want to consider a grid-patterned nest to take advantage of the fiber laser cutting machine’s speed.

In this nest, the quadrilaterals are aligned with the edges along similar axes. The cutting head can fly through the cut before venturing off into another direction.

“What really happens is that you have a bunch of squares in a grid-shaped pattern, for example,” said Deepak Ethirajan, an application engineering manager for nesting software developer Metamation. “So the laser cuts one side of the square and keeps going in the X direction. It completes all of the horizontal rows first and then completes the verticals.”

This type of sequenced cut is sometimes called “stitch cutting,” according to Ethirajan, who acknowledges it is for very specialized fabricating applications.

He added that the company’s software algorithms are primarily the same as the ones used for the CO

2

machines. It’s the sequencing logic that can be looked at to help get parts laser-cut and off to the next fabricating operation in as little time as possible.

“It’s not so much about the special care that needs to be taken for the fiber laser,” he said. “It’s only about reducing the processing time.”

Other Considerations

Processing time is a concern for most fabricators, and that’s why they need to be cognizant of a fiber laser’s operation. The cutting machine operates incredibly fast, which can be a blessing, as long as everything functions as it is programmed, or a curse, if things go wrong.

It’s not so much nesting, but the thought process behind the nesting, according to Doug Wood, sales and services director, Radan.

“From our perspective, the emphasis has been put on the logistics behind nesting—looking at improvements of the entire process,” he said. “Something like hazard avoidance—we are putting everything that we can to lead the way in logistics in cutting nests to avoid collisions.”

The logic is simple: A fiber laser cutting machine produces a tremendous amount of parts when it is running, and having the cutting head avoid a part tip-up keeps the green light on. An incredibly fast cutting machine is especially noticeable when it is not cutting anything.

Wood said that fiber lasers actually may tempt fabricators to consider using some laser cutting techniques that they ignored previously because the traditional lasers couldn’t take advantage of them without adding considerable processing time to cutting jobs. As an example, he pointed to scrap cutting for holes and cutouts.

“You have a fine line between a hole that will drop through with no problem and one that won’t. At a certain size it might get hung up [on the grates],” he said. “Because of the speed, companies will choose to chop that up into smaller pieces.”

No trapped holes or cutouts means a much smaller chance of a collision occurring between the scrap and cutting head. Wood said that the speed at which the fiber laser cutting head moves convinces laser operators to engage the scrap destruction software option because, even with the extra cutting, the new laser technology is still likely to outperform traditional laser cutting performance in thinner gauges. In fact, some fabricators might want to engage in scrapping up the sheet with the cutting head, making the laser operator’s job that much easier when the laser cutting job is complete.

Another area of focus for the software developer has been in the area of passing along critical manufacturing information via part etching. Someone has to sort parts as they come off the fiber laser machine, and because the equipment is so adept at churning out large amounts of laser-cut blanks, that part sorter has a large job to do. But what if the CAM software were able to pull key information, such as part or order number, from the manufacturing resource planning software and have the fiber laser cutting head etch that onto each part? The part sorter wouldn’t have to engage in a guessing game and would be able to organize the blanks based on detailed information etched on the part. Such a scenario might prove particularly useful for a fabricating shop that cuts parts for assembly of kits, especially if more than one type of kit is included on one nest.

“With the speed of fiber lasers, you can etch part numbers on components much faster than you could in the past,” Wood said, “so it’s become a reality for many shops.”

Fiber laser technology hasn’t really changed the way fabricators nest, but it may force everyone to look more closely at the actual laser cutting process and postcutting operations.

Editor-in-Chief Dan Davis can be reached at

dand@thefabricator.com

.

Radan, 25 N. Lake St., Suite 220, Forest Lake, MN 55025, 800-875-7232,

www.radan.com

Salvagnini America Inc., 27 Bicentennial Court, Hamilton, OH 45015, 513-874-8284,

www.salvagnini.com

SigmaTEK Systems LLC, 1445 Kemper Meadow Drive, Cincinnati, OH 45240, 513-674-0005,

www.sigmanest.com