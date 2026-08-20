# Preserving those parametric links when changing file names

[TARİH: 01.05.2021 The Fabricator]

Expertise » Precision Matters

Don’t rely on the Windows file renaming tool

By

Gerald Davis

Read more from Gerald Davis at

www.thefabricator.com/author/gerald-davis

T

he brand of CAD that is used to produce illustrations for this column relies upon the Windows operating system. If parametric CAD modeling techniques are used in a project, the file names and their folder paths become a vital part of the CAD database, also known as the design. Protecting the parametric information is part of the job.

Figure 1

highlights several broken links denoted as "-?" by the software.

FIGURE 1 "-?" denotes broken external references—a problem that is time consuming to repair. Avoid this problem by using file management tools that are able to preserve the parametric links between files.

Avoiding such damage is easy. Don’t use Windows rename to change file names; instead, use Pack and Go, Solidworks Rename, or perhaps Save-As. Repairing such damage involves replacing broken external references with new context, essentially repeating the initial modeling process. This article is more about prevention than repair.

As a modeling scenario to demonstrate possible parametric peril, please consider

Figure 2a

. At this early stage of invention, the shape of the product concept is likely to change. Maybe this product will have a different flow, maybe longer or wider in some way. In this scenario, the concept piece has been given the prep-for-fabrication-but-expect-itto-change approval.

FIGURE 2A A concept model has preliminary approval for shape and functionality; proceed with design for manufacturing. The next task is to develop sheet metal features that can be fabricated.

FIGURE 2B A top-level assembly is created. It has only one component so far; the sheet metal parts will be added to complete the bill of materials. Note that the concept part will be excluded from the BOM.

The ideal concept model is quick and easy to shell out, but perhaps not suitable for a specific method of fabrication. We want to keep the concept model as the driver of shape so that the fabricated parts will update automatically as the design evolves.

The method of construction, welded sheet metal, is chosen for this project. Also, a given is the requirement that each piece part be assigned its own file. The drawing for the welded funnel features a bill of materials table (BOM as opposed to cut list) displaying the required piece parts.

A CAD Funnel Recipe

In

Figure 2b

, a new assembly file contains the concept part. The name of the assembly is arbitrary; design work is the priority. "Funnel Concept" works for now.

This top-level assembly is created with two goals in mind:

1. Its components will populate the BOM table for the weldment drawing.

2. It will allow parametric links between the sheet metal parts and the shape of the concept part. (As a side note, the concept part is excluded from the BOM.)

The parametric features (external links) emerge because of the CAD modeling technique. All of the components are created and edited within the context of the top-level assembly.

This demo walks through modeling one of the walls—more specifically, the back wall. The other three are modeled in the same manner.

To model the back wall of the funnel, a new part is inserted into the assembly, is renamed, and saved as a part with the arbitrary filename "Back Wall."

In a better world, we might already know the proper name to give the newly created or at least wait longer before converting virtual files to arbitrary file names. But that would be too easy. Perhaps your planning will take advantage of the ease of renaming virtual components.

CAD nuance: Newly created components are fixed in position by default. The author prefers to change them to floating and then to mate their origin to the origin of the master part in order to align all planes and axes between parent and child. You may find that "fixed" works just as well or better than mated.

Figure 3a

shows the surface offset that follows the floor, back wall, and mounting flange of the concept part. As modeled, the entire top flange is a single surface. It requires trimming into an appropriate shape.

FIGURE 3A The floor, back wall, and top flange of the concept model were used to create a surface offset. The top flange will be trimmed in the next step.

FIGURE 3B A 3D sketch will trim the surface. The side walls overlap this back, so the edges are trimmed by a material thickness. Three sides of the top flange will be discarded, all in the next step.

FIGURE 3C The surface is trimmed using the 3D sketch. The cyan colored surfaces will become sheet metal. Purple will be discarded.

Figure 3b

shows a 3D sketch that will be used for trimming. The sketch elements have parallel relations so that only a single dimension is required. This dimension could be equation-controlled to match the sheet metal thickness.

Figure 3c

shows the trimming that the sketch controls. Purple goes away and cyan is kept.

Figure 4a

shows the result of converting the trimmed surface into a sheet metal body. A gauge table was used with our preferred k-factor for 13-gauge (0.090 in.) thickness.

The modeling process (insert new part, edit new part with surface offset, trim, and convert to sheet metal) is repeated for the remaining walls.

Figure 4b

shows an exploded view of the sheet metal parts that now reside in our top-level assembly with the concept part.

Figure 5a

shows the product as designed for manufacturing. The CAD files for the assembly and its components have preliminary names.

FIGURE 4A The Convert-to-Sheetmetal tool converts the three trimmed surfaces into a sheet metal body, ready for fabrication.

FIGURE 4B An exploded view of the top-level assembly shows the concept part and the derived sheet metal parts. Design for manufacturing is well underway.

FIGURE 5A It’s time for a progress report: The design for manufacturability looks OK, but the file names are incorrect.

We now imagine that design review and approval have taken place. Part numbers are designated, and ideal file names are to replace the preliminary. The CAD system’s Save-As could be used with good result. However, it only works one file at a time. Save-As functionality allows us to preserve the external references, but Pack and Go is a wonderful way to change several file names all in one go.

Convenience and Speed

Figure 5b

shows Pack and Go ready to Save-As our concept work with improved file names. The cells in the table accept double-click to allow editing. All of the green entries have been changed to show the ideal file names.

The save button on the Pack and Go panel launches all of the new file names.

In

Figure 5c

, the properly named top-level assembly—now called "FMA-2021-05-1.sldasm"—shows the names of its well-mannered children. Yellow highlighting of the "->" external references (parametric links) shows our joy.

FIGURE 5B Pack and Go can be more efficient than several Save-As operations. Either way, these tools preserve the parametric information as the file names change.

FIGURE 5C The well-named top-level assembly has well-mannered children. Pack and Go preserved the external references. "->" is good, and "-?" is bad.

Recall the bad example—Figure 1 highlighting broken "-?" links in components. That damage was done using Windows Rename instead of Pack and Go to change the name of the top-level assembly.

Send your questions and comments to

dand@thefabricator.com

.

GET THE LISSMAC EDGE

Increase your quality and output with our full range of solutions for:

Deburring Deslagging Edge rounding Finishing

17 Route 146

Mechanicville, NY 12118

518.326.9094

getthelissmacedge.com

sales@lissmac-corporation.com