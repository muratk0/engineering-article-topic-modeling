# Giving a welding robot some eyes

[TARİH: 01.10.2014 The Fabricator]

Servo-Robot launches a new platform for its sensing technology

By Tim Heston, Senior Editor

An idle robot in the corner of a custom fab shop isn’t an unusual sight. The company might invest in a robot cell to fulfill one large-volume order, but after that order ends, the robot sits, waiting for the next big job. Fewer customers want large batches of parts, because no one wants to hold much inventory anymore.

Instead, they order a little at a time, and that’s just not conducive to robot welding. That’s the traditional view, at least. Not only do you have the fixture-building and teach-pendant programming, but variation abounds. If you run several hundred of one part in July, then run the same part again in September, the part may not be exactly the same, thanks to slight variations in forming and cutting processes upstream. In most operations, robots weld blind. It just goes where the program tells it to go, and so the operator needs to make changes to adapt the program to the part in front of the robot arm.

To remain cost-effective, the custom fabricator traditionally has had two choices in this situation: to perfect processes to improve part geometry and fixturing consistency, or simply send the part to a manual welding station. After all, welders adjust to slight changes in seam geometry all the time.

But there’s also a third option: seam finding and tracking. This option usually has been reserved for critical applications with high costs of failure. But recently Quebec-based Servo-Robot introduced a platform with the idea of making such sensing much more pervasive. Called the iCUBE, the cube-shape system sits near the end of an articulated robot arm as a self-contained unit, which, according to the company, makes it relatively simple to integrate into a welding cell.

“This is an entirely new platform for us. All the power, the camera, laser, and all the processing is done onboard,” said Jeff Noruk, president of Servo-Robot Corp., the company’s U.S. division.

The company has introduced the platform initially for seam finding and process monitoring, which effectively gives the robot “eyes” and sensory perception. A part is fixtured in place, and as the robot approaches, a laser emits a horizontal line onto the workpiece. A camera reads the laser light’s intensity, and from that spectrum of data it determines where the seam truly is, its actual gap measurement, and related characteristics. Unlike a laser spot, which has to be moved to detect seam variations from the nominal position, a line laser emits a line that in this application is several inches wide, covering the entire joint area at once and providing instantaneous feedback. “You turn it on, it automatically recognizes the joint, and then automatically corrects for it,” Noruk said.

If the laser needs to find a groove weld in a batch of 100 parts, the sensing goes into action for the first workpiece. It knows the V should produce a specific signature template, with different levels of intensity as the laser line descends over the bevel shoulder and into the weld root. That data feeds into an algorithm, which compares what’s real to what’s in the weld program. Within a second or two, the robot knows where to go to account for the new seam position and starts to weld. It then uses this information for the remaining 99 pieces in the run. After that batch is finished and the operator loads a new part, the sensor springs into action again. The sensor also can be set up to run for every part, especially valuable if the weld fixture moves ever so slightly as operators swap out workpieces.

Welding isn’t the cleanest of fabrication processes, so throughout this cycle, the system uses air pressure to ensure most debris from the work envelope stays away. The company reports that the system is designed to endure tough welding environments, including those with high-frequency starts like with gas tungsten arc welding and plasma arc welding, as well as high temperatures.

Currently the system is set up to finds seams; it doesn’t track them. It gives the robot eyes for an instant, but once the robot starts to weld, it is blind again. In the near future, however, the company plans to add seam tracking, which provides the robot system with continuous updates, allowing it to make adjustments in real time, as well as perform postweld inspection.

“Seam tracking can help overcome part variation, fixture variation, or any distortion that may happen during the welding itself,” Noruk said. “A manual welder would obviously make corrections during the weld, but the robot doesn’t know how to do that.”

The company has also integrated a microphone into the camera, which in turn can project this sound to a speaker outside the cell. A slight change in the arc’s buzz can convey a lot to the welding engineer and technician. The platform also will be able to sense torch or gun angles to ensure they match what the welding procedure specifies.

Noruk is careful to point out that having seam finding and tracking intelligence doesn’t magically make the robot account for bad or inconsistent joint design. “The biggest misconception is that if you put any kind of sensing technology on a robot, all your problems are solved,” Noruk said. “That’s not true. There has to be a weldable joint that’s within the procedure’s requirements. The gap and fit-up have to be reasonable. Sensing technology is designed to handle variation off of a nominal and extend the process window.”

There also has to be a direct line of sight between the laser and seam, and the joint can be only so deep and narrow. “On some very deep joints, the laser goes down and isn’t reflected back with enough intensity for us to really read it properly,” Noruk said. He added that certain joint geometries, like a flare bevel joint of a stamped component, can also present unique challenges because the radius on the formed edge can vary, and that makes it more difficult for sensing to be precise. “Still, in most cases it is far better than welding blind.

“We consider these systems to be intelligent, but they’re intelligent only because we teach them certain rules,” Noruk continued. “If you break the rules, it still doesn’t have all the ability to recalculate and interpret the information like a human welder.”

These limitations aside, the iCube is designed to work on the vast majority of weld joints in industry. Servo-Robot designed the system to be universal, easy for robot manufacturers to integrate onto existing platforms, and simple to program. Long-term, Noruk said the company has an outlook similar to Microsoft’s dream in the 1970s: a computer on every desk. “Our dream is to have a sensor on every robot,” Noruk said.

Perhaps one day we’ll all look back and wonder how robots ever welded blind.

Servo-Robot Inc., 1370 Hocquart, St-Bruno, QC J3V 6E1, Canada, 450-653-7868,

www.servorobot.com