# Linear versus sketched patterns for real-time demonstration

[TARİH: 01.03.2025 The Fabricator]

Precision Matters

Sketched patterns are versatile, linear patterns are dandy

GERALD DAVIS

L

et’s discuss a project that required revision of an existing virtual prototype. The mission was to rearrange the components. The task required importing a STEP assembly (see

Figure 1

).

FIGURE 1

The goal: "move the furniture." The method: recreate some patterns and delete the legacy holes, then drag the model around for show and tell.

Recreating the product manufacturing information and the 2D drawings was expected to be the most time-consuming part of the project, which included preparing the model for a real-time design and review meeting.

The components shown in Figure 1 included some items that were modeled in the native CAD as patterns as a matter of efficiency. For the convenience of the task, I needed to recreate some of these patterns in my favorite CAD program.

A pattern of components can be driven by linear vectors or by a sketch. The CAD software does not have a preference; the best modeling technique is determined by circumstance.

With a sketch-driven pattern, a bolt might appear everywhere that a point is sketched. Those points could be arranged in a grid, and the result would be the same as a linear pattern. Or they can be located wherever needed.

This versatility of the sketch-driven pattern requires some preparation and introduces a bit of overhead—sketching or editing the sketch—just to move the bolt. I find it delightful that this mimics reality—the bolts end up where the holes are, not the other way around.

The overhead required for versatility could be a drawback, especially during a live demonstration. But before I continue, a bit of history.

A pattern of components can be driven by linear vectors or by a sketch. The CAD software does not have a preference; the best modeling technique is determined by circumstance.

My career with CAD began while running the CAM department in a sheet metal job shop. In the late ‘70s, paper tape loops were part of the cutting-edge technology for batch manufacturing.

At the time, the physical length of the G-code program was of paramount importance. We used canned cycles and macros if it meant shorter tape loops; long tape loops were fragile and caused production delays.

I was exposed to CAD after CAM. To this day, it is an effort for me to design without thinking about how the item would fold on a press brake. When I model items, I am aware of CAM. My modeling process ends up mimicking how the item could be fabricated. I start from a DFM point of view and adapt to the aesthetic goals. My default routine is to model the holes and then put the fasteners into the holes. I use the Hole Wizard as if I were programming for a turret press—the fewer the tool changes (hole sizes) the better, follow the short path, be easy to edit. I get good grades for my skills in DFM from collaborating engineers.

FIGURE 2A

The imported screws are being replaced with a linear pattern using one of the original screws as the seed. Linear patterns are convenient for dragging around with a mouse; only the seed component needs to be mated.

FIGURE 2B

The legacy holes are deleted using the Face-Delete tool. There are many other ways to get the same result, but this is speedy.

FIGURE 3

Now that the screws are patterned and located relative to the camera bracket, the mouse can drag all things related to the camera to the ideal location. This repositioning can happen in real time. As a final step, the screw holes are located where the camera is.

Anyway, after a couple decades of living the life, I graduated from the job shop to hang my shingle as a CAD slinger for hire. Because I had more than a few happy customers, I felt confident in my abilities. Sketch-driven patterns were spiffy. Now, back to the story.

For the design meeting, the STEP import needed some assimilation into this brand of CAD. My approach was to replace the individual repetition of components with linear patterns (see

Figure 2A

). I also deleted their legacy mounting holes (see

Figure 2B

).

My thought was that mouse manipulation (dragging the furniture, as it were) of any component of the pattern would be responsive during the live presentation.

In fact, my customer was delighted to spot the opportunities as the layout evolved.

During the meeting, the task felt a bit like moving the furniture in a new home. As the design evolved, my default self was personally alarmed by the absence of holes; the model was unrealistic. The blessing was that visually, the model was credible and predictive—good things in a design review meeting.

To finally get the holes into place and bring the model into reality, the Hole Wizard proved to be efficient. It was easy to locate the holes where the bolts were (see

Figure 3

).

My sage advice from all this is that linear vector-driven patterns are useful for quick modeling but are not as versatile or as easy to revise as sketch-driven patterns.

Editor’s Note: CAD files associated with this column can be downloaded at

www.thefabricator.com/page/shop-technology-and-3-d-cad-downloads

.

Gerald

would love for you to send him your comments and questions. Please send your questions and comments to

ddavis@fmamfg.org

.