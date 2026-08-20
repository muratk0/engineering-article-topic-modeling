# 3D models need to be more than pretty

[TARİH: 01.12.2020 The Fabricator]

Expertise » Precision Matters

Import your export file to ensure enough billet is there for the job

By

Gerald Davis

Gerald

would love for you to send him your comments and questions. You are not alone, and the problems you face often are shared by others. Share the grief, and perhaps we will all share in the joy of finding answers. Please send your questions and comments to

dand@thefabricator.com

.

Read more from Gerald Davis at

www.thefabricator.com/author/gerald-davis

FIGURE 1.

A 2D drawing for a modified bolt is shown. Section A-A shows the areas where thread is removed. This removal is modeled by (drum roll, please) removing the threads from the billet and attaching a hole callout—text that pretends the thread is there. The red box shows a view with threads. If perfectly modeled, such threads can be useful in fabrication.

T

he fabrication drawing shown in

Figure 1

is for a modified bolt. Starting with a common off-the-shelf item, the idea is to make a tapped hole in the threaded-end ¼-28 and to drill and tap the headed end for a ¼ NPT fitting.

Several details are revealed in the drawing. Section A-A shows our desired through-hole, a zone removed by the ¼-28 threads; a pocket made by the pilot drill for the ¼ NPT; and the tapered section removed by the pipe threads.

CAD software helps to automate the production of such drawings. The hole callouts for the tapped holes required simple mouse clicks to add the detailed drilling notes to the drawing. Such information is pulled from the modeled features in the 3D part. This helps to minimize and goof-proof the typing chore.

A CAD model that is excellent for making 2D drawings may, at the same time, be a catastrophe in fabrication. I know because I received some parts that had threadless holes that matched the STEP file (not the PDF) perfectly.

FIGURE 2.

This is a cross-section view of the 3D model used to create Figure 1. The external threads will grow in later stages from an undersized shank. The internal threads will fill up oversized pockets.

Figure 2

shows a cross-section view of the shaded 3D model that was used to create Figure 1. When it comes to tapped holes, the 3D representation of threads is a trade-off between computer speed and visual accuracy. For speed, threads are often shown as

cosmetic threads

– just phantom cylinders, not actual helical spirals.

FIGURE 3.

A cross-section view of threads added to Figure 2 is shown. The Thread feature quickly models the straight threads. A combination of Hole Wizard and helical sweep create the tapered thread. Disclaimer: If you download the example, the threads are not guaranteed to be standard profiles.

The helical threads shown in

Figure 3

(peek closely to see the cross section) require a few more CAD modeling steps. Helical surfaces task the computer’s video system with more work. An alternative modeling technique is to revolve “threads” instead of sweeping the helix. That illusion works great as a speed and time saver.

The scenario for this project requires that we produce both a 2D PDF (see Figure 1) and a 3D STEP file (see Figure 3).

FIGURE 4.

The off-the-shelf bolt is modeled with a revolve, head hexing cut, grade bumps, forged taper, and 5/8-18 fully threaded 2-in. shank. The product manufacturing information will be for the finished machined item. The raw material just happens to be a bolt.

Our raw material—a common grade 5 bolt—is shown in

Figure 4

. To create this model, we used a revolve. Revolves take slightly fewer CPU cycles than a boss-extrude. (Sure it’s a small nuance, but we do what we can.)

The wrench flats were cut with a sketched hexagon. The forged taper on the head is modeled with a revolved cut, a small detail that adds visual credibility.

Three bumps on the head means grade 5. The grade marking has the pattern-of-three in the sketch for a single boss-extrude. An alternative is sketching for one boss-extrude and patterning it three times, but that takes slightly more CPU effort.

The thread feature adds the 5/8-18 thread around the shank of the bolt. The thread is not needed for the 2D drawing, but it is useful for visualization. It can also be important in the STEP file that is exported for fabrication.

FIGURE 5.

This is the Hole Wizard setup for drill and tap of a ¼-28 hole. A handy setting is shown in a red box: Remove Threads. This works well with the Thread feature, which will later be used to add in the helical threads.

Figure 5

shows the Hole Wizard setup for drilling and tapping a ¼-28 hole. Our red box has been added to emphasize a setting—Remove Thread. This works nicely in conjunction with the Thread feature, which puts the threads back in.

For the big tapped hole, the Hole Wizard is again set to

remove the threads

. The missing tapered thread is modeled back in using a sweep along a tapered helix.

FIGURE 6.

Configurations are used to change the model from

Off the Shelf

to

Modified

to

Modified Without Threads

. Perhaps another configuration is needed for

raw billet

for exporting purposes.

Three configurations are used to control this model.

Figure 6

shows the “No Threads” configuration in the graphics window. All three of the thread features—5/8-18, ¼-28, and ¼ NPT—are suppressed in this configuration. For comparison, Figure 3 shows the model in the

modified

configuration.

So now we hammer home the CAD caveat: If the STEP file is going to be used for manufacturing, it is possible that the modeled configuration that works for making a 2D drawing will not work as a billet for machining. Without the threads in place, the modeled billet is too small for the external threads and too large for the internal threads.

Here’s the CAD tip: Import your export and evaluate it as a billet for machining. Are the holes too big? The pegs too small?

A CAD model that is excellent for making 2D drawings may, at the same time, be a catastrophe in fabrication.