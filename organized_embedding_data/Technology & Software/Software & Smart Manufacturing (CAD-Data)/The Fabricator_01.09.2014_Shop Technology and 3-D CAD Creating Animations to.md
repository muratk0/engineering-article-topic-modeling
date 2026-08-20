# Shop Technology and 3-D CAD: Creating Animations to Explain the Invention

[TARİH: 01.09.2014 The Fabricator]

Precision Matters

Observe the work flow of a 3-D CAD movie director

By Gerald Davis, Contributing Writer

Gerald Davis

is a job shop consultant and chairman of the board of DSM Manufacturing Co.,

gerald@glddesigns.com

.

B

efore grabbing the mouse, we begin our 3-D CAD animation by preparing a written outline—a storyboard—of the scenes that are to be included in the movie. As we doodle on a page like that in

Figure 1

, we determine how each stage in the play will contribute to the overall impression the animated clip leaves.

Figure 1

This is the actual storyboard that started this article. The idea of planning before starting work applies to animation as well as it does to design work.

Initially the storyboard might simply be a short list of topics that must be covered in the video clip. Those topics might be further outlined as sequences of scenes or perhaps just a single scene. A scene includes the background and camera point of view, as well as components that are animated to fade, appear, or move in some way.

The storyboard also will be used to “program” the 3-D CAD software. A timeline of events—similar to a player piano’s roll of holes—will control the animation. Each event is marked with a key point. Keys are used to set distances and angles between components. Key points are also placed to control cameras and component appearances. The software magically calculates the transitions between the key points. Those transitions are rendered to become individual frames in the video clip.

The 3-D CAD software used in support of this article is well-suited to working on individual scenes. Other software may be more efficient for composing the overall movie.

The events on the timeline depend on prior events. After we edit the keys to refine the movie, the event sequence may require recalculation, sometimes a time-consuming process.

The shorter the clip is, the quicker the recalculation will be. Thus, the experienced CAD jockey tries to anticipate the level of complexity. Perhaps multiple Motion Studies are in order.

Action!

In our scenario, the goal—also known as the

complexity

—is to show the observer how to mark a line at a 1.25-inch location on the workpiece using a square and a scribe. The movie clip produced for this scenario will be incorporated by others into a more comprehensive production.

The following is a refinement of the storyboard shown in

Figure 1

. Messages that are to be conveyed in the clip are:

Set the square’s ruler to 1.25 in. Loosen the thumb nut, slide the ruler, and tighten the thumb nut.

Position the square against the workpiece. Hold flat and true with the long edge of the blade about 0.5 in. from the short edge of the workpiece and with the 1.25-in. blade perpendicular to the long edge of the workpiece.

Scratch a line in the workpiece. Unlock the scribe from the square’s head and scratch along the end of the ruler.

Hide the tools to reveal final marked workpiece.

This assembly has components that are mated to constrain how they move relative to each other. Relative motion between components can be simulated in two basic ways: real-time mouse drag and calculated Motion Study.

A mouse drag provides immediate gratification and sometimes random results. Motion Studies require methodical preparation and are used to achieve controllable results in the animation. (

Animation

refers to the result of playing the Motion Study’s timeline of keys.)

A Motion Study is similar to a scene in a movie in that several Motion Studies can be part of an assembly, just as several scenes can be found in a movie. To decide how many Motion Studies are likely to be needed, you might want to review the CAD tricks required for each scene.

1. Set the ruler to 1.25 in.

Turn the nut counterclockwise to demonstrate “loosening” of the nut; slide the ruler to 1.25 in.; turn the nut clockwise to demonstrate “tightening” of the nut.

A set of three of the keys on the timeline of the Motion Study manage the start/stop of the nut’s motion.

Figure 2

provides more detail. In this demo, those timeline keys control a distance-mating relationship—or distance-mate—between the nut and the ruler clamp. This model features a screw-mate between those same two components. The result is that the nut turns as the distance changes. After the nut’s distance-mate is changed, another key changes the distance-mate between the end of the ruler and the face of the head casting to 1.25 in.

In addition to component motion, this scene should give the observer a clear view of the ruler scale and the nut

before

the nut starts turning. The scene then calls for a zoom-in for a clear shot of the ruler scale at 1.25 in.

Figure 2

Motion Study keys are used to control the distance of the nut from the casting. Start at 0 in., move to 0.1 in., and then return to 0 in.

Figure 3

Motion Study keys also are used to control the position of the camera. The point of view is controlled independently of component motion or appearance.

Figure 4

The distance-mating relationship, or distance-mate, between the square and workpiece is changed to 0 in. to make the square appear to rest on the workpiece. Note the mate-group folder has been rearranged so that the mates belonging to the Motion Study are at the top of the list.

Figure 5

A path-mate to a spline that is fitted to a 3-D sketch controls how the scribe moves in the movies. The Motion Study controls the distance along the path.

A few more timeline keys are needed to control the observer’s point of view by moving the camera.

2. Demonstrate the proper positioning of the square on the workpiece

(see

Figure 3

). Zoom in to show the square and workpiece separated a short distance from each other, and move the square toward the workpiece until they touch.

Several keys are needed to change the point of view to follow the action. The goal is to make it clear that the head casting is resting against the workpiece’s face and that the ruler is also in good contact with the workpiece.

A pair of keys to set the starting and ending distance between the workpiece and the ruler takes care of the motion (see

Figure 4

).

3. Fetch the scribe and scratch a line at the end of the ruler.

Demonstrate the tip of the scribe moving against the face of the ruler.

Three path-mates are used to control the

flight

of the scribe. Path-mates involve some setup, such as 3-D sketching and mating, before launching the Motion Study editor. We’ll use the same 3-D sketch and mate to it three different ways. Any of those three mates simultaneously being active causes mate conflict. To avoid that, we suppress them after creating them; that is the same as “turning them off” in Motion Study speak.

Back in the Motion Study editor we then can add a few timeline keys to turn on only the appropriate path-mate during the desired time period in the video clip (see

Figure 5

). With one of the three path-mates turned on, another corresponding key pair controls the scribe’s starting and ending distance along the 3-D sketch path.

A

docking

path-mate flies the scribe in and out of the square’s head. This path-mate has a pitch control setting that keeps it moving horizontally as the distance along the path is changed.

A

flying

path-mate controls the flight of the scribe into approximate position for scratching. The orientation of the scribe during this stage is not important. This path-mate allows free pitch and roll of the scribe, giving a fluid motion along the 3-D path.

A

scratching

path-mate moves the scribe along the end of the ruler. The scratch scene matters. The scribe must tilt its tip to make realistic contact with the ruler. This path-mate locks the Z axis of the probe at an angle to keep it away from the face of the ruler. In addition to credible motion for the scribe, a scratch is to appear in the model of the workpiece.

4. Demonstrate the emerging scratch in the workpiece.

As the scribe moves along its path, extend the length of the scratch in the workpiece.

The scene for the emergence of a scratch is shown in

Figure 6

. The technique is to model a cut-extrude up to a plane in a featureless model and to control the position of that invisible model with distance-mate timeline keys. It might be difficult to spot in

Figure 6

, but an emerging scratch is visible in the body of the workpiece model.

Figure 6

The distance along the path also influences the motion of the scribe, the length of scratch, and the creation of the “glowing” scratch body. Download the movie and grab some popcorn!

Figure 7a

The glowing scratch is sometimes changed in appearance to fill in and hide the scratch.

Figure 7b

The cut-extrude is now maximum length. The fill-in volume body is maximum size. The appearances of both are cranked to grab attention.

5. Demonstrate what a pristine workpiece looks like

(see

Figure 7a

),

as well as emphasize the completed scratch

(see

Figure 7b

). To hide unwanted edges and faces, model yet another component to parametrically match the volume of the scratched groove.

Not only does it hide the not-zero-length cut-extrude, the timeline keys make this component’s appearance glow brightly to emphasize the existence of the scratch.

6. The finale changes the appearance of the square to become fully transparent

(see

Figure 8

),

which effectively hides it.

A pair of timeline keys allows that transparency. This scene also zooms in to emphasize the lovely new scratch in the workpiece, which the last couple of keys enable.

The Final Cut

This scene/CAD review is summarized as six scenes spanning approximately 40 timeline keys. On the average, that’s about 10 timeline keys per scene. From personal experience, a 50-key limit on an old and slow laptop is about as complex as a single Motion Study needs to be. Motion Studies are really limited only by the hardware resources of a workstation. The amount of time spent waiting for the clip to recalculate can be significant.

Figure 8

Fade the tools out of the scene by changing their appearance to transparent. We’ve randomly staggered the timing of their disappearances to add interest to the clip.

Figure 9a

With the timeline keys completed, save the output as a movie file. The default is AVI. Several other formats are options.

Figure 9b

The default settings for compression are OK. The decisions about file type and format are usually driven by the next user of the clip. For editing, less compression is good. For sharing with other people, more compression/lower frame rate/lower resolution makes for smaller file size.

How long does it take to populate a timeline with keys? In general, this sort of project takes at least a half-day and probably consumes a full day’s attention.

Although it is a simple and easy drag-and-drop mouse procedure to place or edit timeline keys, a CAD jockey requires discipline to stop reviewing the animation and re-editing the keys once they exist. Here’s a tip for speeding the key-placement process: Before launching the Motion Study editor, open the Mates folder and use the mouse to drag the angle- and distance-mates that are to be controlled dynamically in the Motion Study to the top of the list in the Mates folder. Give them useful names, too. For example, rename “Distance8” to “Nut Distance.” (See

Figure 4

for an example of reordered and renamed mates.)

The more specific the planned storyboard is, the easier it is to set up the Motion Study. It is helpful if the storyboard addresses details such as the observer’s point of view, scale of view, background and shadow settings, component visibility, component motion, and the rate of change for these animated elements.

Returning to our scenario, the CAD jockey/movie director has refined the storyboard into six scenes, but might now employ the mouse to deploy a few experimental keys on the timeline to evaluate changes in camera aim.

Let’s start with a scene showing only a pristine workpiece:

Change the camera angle to show both the workpiece and the square separated by a short distance from each other.

Hide the workpiece and zoom in tight to show only the square. This will be the scene where the ruler is moved to the correct setting.

Return to the view showing the distance between the square and workpiece. This camera will be held stationary while the square moves into position on the workpiece.

Zoom in tight on the square and workpiece.

A 360-degree tour with the camera provides a thorough reveal of where the square goes.

When played, this preliminary storyboard clip appears to fly the observer around a scene. The visible components do not change appearance or move. This is a good opportunity to work out the timing and transition between these major points of view.

Director’s Commentary

The next layer of key points to be added to the timeline will control the motion and appearance of components. When an object appears out of nowhere, the event helps to draw the observer’s attention. It is therefore important to consider the impact of simultaneous motion with fade-in. Components that remain stationary while materializing give the observer time to assimilate the arrival of something new. Subsequent motion of the object will help to maintain the viewer’s attention to that object.

This recommendation is made in the theme of expository cinema, not action/drama. A dramatic animation might feature a materializing part that is already flying along a path. The observer might be startled. Timing and sequence of keys on the timeline make all the difference in what impression is left with the observer.

To control the observer’s point of view, the director has the opportunity to employ as many cameras as are desired. The default graphics window is simple and has controls to turn the

perspective

view on. CAD jockeys/movie directors are encouraged to set up additional software cameras that allow photorealistic control, including depth of field and aiming. These cameras can be conveniently selected and controlled precisely with timeline keys.

In review, we started with a jotted storyboard and used it to place keys on the timeline to sequence the main scenes in the clip. We then revisited each of those scenes and changed the appearance and motion of components to comport with the storyboard. We’ve previewed the animation and are satisfied with the sequence and timing.

The next step is to generate a video file for distribution to our observers (see

Figure 9a

). Decisions about video file type (default AVI), frame rate (usually 30 frames per second), and graphics rendering are made at this step. If AVI format is selected, the AVI compression defaults are generally useful for playback on Microsoft operating systems (see

Figure 9b

). Other file types and export options may be better-suited for use with video editing software. For example, the uncompressed raw frames produce large file size, but possibly better import into the video editor.

Gerald Davis uses CAD software to design and develop products for his clients at

www.glddesigns.com

. He is a former owner and operator of a job shop from 1984 to 2004. Please send your questions and comments to

dand@thefabricator.com

.