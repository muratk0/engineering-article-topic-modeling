# A review of tricks to reduce rebuild time

[TARİH: 01.06.2025 The Fabricator]

Precision Matters

Minimize the details and get back to designing

GERALD DAVIS

I

n the CAD brand used here, rebuild time is the patience that it takes to wait out the update of the database that is maintained by the Parasolid kernel (the geometric modeling engine, within 3D modeling applications). This rebuilding can be triggered by initial loading, by edits to a chain of parametric links, or by changing the shape of a body. Even with fast computers, some complex models can take hours to rebuild.

In general, less rebuild time is desirable. To help with the discovery of opportunities for improvement, the software provides tools to evaluate how the computer is getting mesmerized. It is usually no surprise that 80% of the time is spent rebuilding 20% of the features. Focus on the 20%.

Riveting Content

As a point of focus, a rivet might be used many times, and as a result, the rebuild time for its model becomes significant. A revolved body is likely to rebuild more quickly than a stacked series of base-extrudes. Sometimes it makes sense to change the modeling technique, even though the resulting surface of the design is identical.

It doesn’t always pay to focus on rebuilding. Focus instead on building. Get the design completed and the other deliverables done. Take care of the higher priorities. When there is a luxury of time, take time to save time.

Harkening back to our previous episode of this column, while discussing the benefits of downloaded models to save time, we mentioned that CAD models sometimes require editing for the benefit of speed. Modeled threads are often a performance penalty in native CAD.

The example shown in

Figure 1

was downloaded from an online hardware store in native CAD format. The initial rebuild time of 5.68 seconds drops to 2.28 seconds after a forced rebuild (CTRL-Q) and save (CTRL-S) (see

Figure 2

). Unless the design is changed, that’s the baseline we’ll use for rebuild time for this fitting in native CAD.

The lead-in and -out for the thread are reasonably accurate—and include some pretty fancy CAD work. This model is nearly suitable for fabrication. Adjustment for deburring and perhaps thread profile compliance would be the next level of refinement if we were intending to fabricate instead of purchasing this item.

If this CAD model is used as a solo item, a couple seconds for rebuild time might be acceptable. For our purposes, we have no plans to fabricate this fitting. It is used in our virtual prototype primarily to verify hole size and clearance. It also is useful for retaining the product manufacturing information about the item—its mass, description, supplier, part number, etc. (This is all information that might appear in a bill of materials.)

In other words, this CAD model for a pipe fitting could be much less realistic. We don’t need to accurately visualize the threads in this project.

FIGURE 1

A model for a pipe fitting has been downloaded in native CAD format. The initial rebuild time is reported as 5.68 seconds. Most of that time is spent on one feature—Cut-sweep1, which is the helical thread. How do you improve on that time?

FIGURE 2

The CAD software has a tool to force a model to rebuild (CTRL-Q). That by itself has cut the rebuild time down to 2.28 seconds. That is still a significant delay unless the helical thread is somehow dealt with

.

FIGURE 3

Perhaps time will be saved if the helical thread does not have to be displayed. To find out, a revolved body has been added to hide the threads. Instead of saving time, we’ve added time—about 0.11 of a second. This isn’t progress

.

Perhaps hiding the helical surfaces would save time. In

Figure 3

, a revolved extrude hides the helical threads. Unfortunately, the rebuild time is longer—now 2.39 seconds.

Instead of hiding them, let’s delete them.

Figure 4

shows that delete-face is quicker than a revolve, but it still takes longer to rebuild overall—2.37 seconds.

Since we don’t want them, don’t create them. Let’s suppress the helical threads.

Figure 5

shows that the rebuild time shortens to 0.05 of a second. That’s a significant improvement. If we need to maintain the remaining feature history for some reason, this native CAD file could be good.

Instead of maintaining the native CAD history, let’s import the model as a STEP file. If we use STEP AP214, the colors from the master model will be preserved. Color is not a big deal in this project.

FIGURE 4

As with hiding the thread, deleting the helical thread simply adds to the rebuild time

.

FIGURE 5

If you don’t want something, don’t create it in the first place. Here, the helix and the cut-sweep that create the thread have been suppressed. This is the best time yet—0.05 of a second of rebuild time. These features could be unsuppressed in a configuration if they were somehow important to the project

.

FIGURE 6

Instead of importing the native CAD format, a STEP file has been imported. Imported bodies have no feature history, thus having practically no rebuild time. The STEP AP214 format supports color, so one could use a master model and export it to create a speedy model. Keep the link to the master filename to preserve the chain for revision

.

No Waiting Around

In

Figure 6

, we see that the reported rebuild time is 0 seconds. Once the STEP file has been "built" in the Parasolid kernel, it does not need to be rebuilt. There is no feature history. This is the speedy trick: Save it as STEP, import it to strip feature history, and reduce rebuild time to minimum.

If the link to the imported file is maintained (see yellow highlight in Figure 6), changes to that file can be propagated into this imported version of it. In this example, we don’t care about design changes to the fitting so the link can be broken (see

Figure 7

).

FIGURE 7

If the link to the STEP file (preserving revision history) is not needed, the link can be broken, perhaps saving a bit of disk-access time on the local computer

.

Instead of maintaining the native CAD history, let’s import the model as a STEP file. If we use STEP AP214, the colors in the model will be preserved.

Gerald

would love for you to send him your comments and questions. You are not alone, and the problems you face often are shared by others. Share the grief, and perhaps we will all share in the joy of finding answers. Please send your questions and comments to

ddavis@fmamfg.org

.

High Octane Laser Fabrication

VIDEO SPECS WEB

Plate 6025 30 kW

Speed of Light

www.peddilaser.com

|

info@peddilaser.com

| (815) 937-3800