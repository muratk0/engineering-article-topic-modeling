# Shop Technology and 3-D CAD: Comparison of Two Animation Tools for Creating Walk-through Tours

[TARİH: 01.05.2016 The Fabricator]

Precision Matters

Tips and tricks for the movie director who wants to make the most of camera movement

By Gerald Davis, Contributing Writer

Read more from Gerald Davis at

www.thefabricator.com/author/gerald-davis

A

nimations of CAD models are often used as part of the design review. Starting with an exploded view to create an animation produces quick results, as discussed in the March edition. If the model is a mechanism that moves accurately with mouse-drag, then those kinematic relationships can be used to create animations, as discussed in the April edition. Our next CAD trick for animation production is to use a path to control the observer’s point of view. This technique applies to animations that simulate an aerial fly-by or walk-through of the 3-D CAD model.

To summarize our prior discussion, a timelinebased animation gives the movie director/CAD jockey the best opportunity for editing and embellishment. If quick is more important than editable, the CAD jockey can find easy tools that give simple results ("simple" meaning harder to edit and revise).

Eye of the Drone

Cameras on remote-controlled aerial drones are famous for capturing an inspiring and dynamic point of view. Our goal is to create a CAD drone to fly the audience through the design.

The plan is to use a sketched path to guide the observer through the model.

Here’s a CAD tip: Using the sketched path as a constraint, the Walk-Through tool can produce a drone-like, fly-by animation that offers the movie director some repeatable control over camera position

.

As an alternative to the walk-through, if you need to fly a camera around a mechanism that is doing something or changing in some way, a sketched path can be useful in a timeline-based animation.

There is no penalty for using the same sketched path for controlling either an avatar or a camera.

Here’s another CAD tip: Use the Walk-Through tool to rehearse the changes in point of view and then switch to timeline-based animation for final results

.

Sketchy Stuff

The CAD experience of creating 3-D geometry often leads to proficiency in 2-D sketching. The difference between a sketch and a camera path is simply in how the sketch is used.

A simple line segment, straight or curved, can be useful as a path for positioning the camera.

Figure 1a

shows a few setup tips: Create a plane for a path, and sketch a line on that plane. That line represents how the observer will fly past the model. In this example, the combination of sketch plane and the sketched line approximately travels between the two docking pits.

We then launch the Walk-Through tool, shown in

Figure 1b

. At this stage the sketch is added as an eligible constraint. Also, the observer’s eye level is defined as up relative to the top plane. The actual recording of the avatar’s change in view begins in

Figure 1c

. Note the game controller-like interface for moving the avatar.

Figure 1a

A simple path for a walk-through is made by creating a reference plane and then sketching one or more line segments on that plane.

Figure 1b

After the path in Figure 1a is made, the walk-through learns that it could use the sketch to constrain motion. After the up direction for the view is set, we’re ready to start taking our avatar for a walk.

Figure 1c

The Walk-Through controller is a game controller interface. The keyboard or mouse can be used for stepping forward, backward, or for a head swivel. This is where the path is selected for use.

At this stage the constraint is selected, and in this case, a sketch was used. Then the record button is clicked. A time meter displays the length of the record. The keyboard or mouse is used to move the avatar. When the tour is complete, click to stop recording.

The Walk-Through tool can be constrained to individual line segments from the path sketch. The movie director can use this trick to jump the camera’s location in the scene and then resume a smooth glide.

If several contiguous line segments are selected from the path, the camera will glide smoothly from segment to segment.

Here are a couple of CAD tips:

• Use fillets to blend the line segments for a smooth walk-through camera glide around corners.

• If you know that all of the line segments in the path will be used contiguously—no jumping needed—select the sketch from the feature list instead of entities from within the sketch.

Instead of individual line segments for a path, consider using a single smooth spline. Spline nodes have nice handle controls for changing the serpentine shape of the path.

The Third-Dimension Drag

Here’s another CAD tip: Instead of a 2-D sketch, use a 3-D sketch for the drone’s path. It takes a bit of practice. Sketching in 3-D on a 2-D monitor requires spatial awareness combined with mouse dexterity in switching between view manipulation and sketch manipulation.

As a work flow to speed the 3-D sketching process, start a 3-D sketch on a plane instead of in free space. That allows easy 2-D sketching of a spline, for example, that is flat to that plane. The top plane gives a nice overhead view of where the tour will pass the model.

After roughing out the spline in 2-D space, delete the constraints that hold the spline on the plane. Then it is relatively easy to move the spline points in 3-D space. This allows easy drag of spline nodes in 3-D space to create a roller coaster experience for the audience.

This is where the movie director’s art comes into play.

Figure 2a

shows an example of a 3-D spline sketched in space relative to the model.

Figure 2b

is a screen shot from the walk-through along the 3-D spline.

Keyboard Versus Keys

The quick-and-easy Walk-Through tool automatically records an avatar’s view each time the avatar stops moving. Moving the avatar is similar to watching freeze-frame steps of what a walking person would see. The Walk-Through avatar can be positioned with the mouse or with keyboard guidance. The avatar’s elevation and forward/backward motion may be constrained to a path. The constraining path makes it easier to freely look around while predictably moving through the scene.

The Walk-Through tool is quite useful even without a sketched path. The controls are very much like a first-person arcade game for moving forward, backward, up, down, and otherwise looking around.

Figure 2a

Instead of a simple line, a 3-D sketch can serve as an interesting tour path. Follow this tip: 3-D sketch on a plane, delete the on-plane constraints, and then drag spline nodes into 3-D space.

Figure 2b

This is a still shot from an AVI made using the 3-D spline path. The observer takes a roller coaster ride around the model.

Figure 3a

A timeline-based walk-through can use a path to position both the camera’s location as well as its aim.

Figure 3b

This still shot shows how the model moves while the camera is flying around.

For live demonstrations, the choice between using a camera view or using a Walk-Through avatar is a matter of preference in terms of mouse and keyboard controls. For recorded demonstrations, the advantage of the timeline-based animation over the Walk-Through tool is principally in the convenience of editing of the timeline-based playback. For playback, the walk-through tool can be used to save a recording of the steps taken by the avatar. Panning motion must be regestured if the playback is found to be wanting. By their nature, mouse and keyboard gestures are challenging to repeat when re-recording the animation.

Where the walk-through simply uses the path to constrain the avatar’s position, the timeline animation technique adds the complexity of creating a camera view and setting keys to control how the camera operates as well as what it sees.

The benefits of this moderate setup labor in CAD is the ability to control both the camera’s position and its target. Keys on a timeline are a durable and editable control for all elements of a scene. Keystrokes—moving an avatar—make for a quick tour but they are impermanent.

Playing Percentages

The camera’s position keys behave in a special manner when the camera is positioned on a path. In that case, the path keys control the distance along the path. This distance is calculated as a percentage of the path’s length. Similarly, timeline keys also can control the camera’s target of aim along a path.

In

Figure 3a

the same 3-D spline sketch is being used to position a camera instead of an avatar.

Figure 3b

is a still shot from this animation showing the model moving while the camera is flying around.

You might use separate paths for camera position and target or a single path for both. As with the avatar, the convenience of the path is in allowing the movie director to achieve smooth transitions in the view.

The view seen by a passenger in a car would be easier to re-create with separate paths for position and target. The view of the driver of the car is very easy to create with a single path.

Here’s one more CAD tip: Keep the camera’s target keys ahead of its position keys; otherwise, the camera’s view swivels as the position passes over the target. Sometimes that dizzying effect is desirable

.

When using the camera’s path keys to sneak around corners, keep the camera’s target, as a percentage along the path, very close to the camera’s position, again as a percentage along the path. When anticipating a turn or scanning the horizon, move the camera’s target farther along the path from the camera’s position.

Gerald Davis uses CAD software to design and develop products for his clients at

www.glddesigns.com

. Please send your questions and comments to

dand@thefabricator.com

.