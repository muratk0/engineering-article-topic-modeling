# Beam shaping and manipulation pushes laser welding’s limits

[TARİH: 01.06.2020 The Fabricator]

The process moves a step closer to fully autonomous operation

I

magine a workpiece fixtured and ready for laser welding. The robotic system doesn’t have a typical laser welding program. In fact, all it really has is a computer model of the parts at hand and instructions that amount to "weld this."

The system draws from a vast database of material grades, thicknesses, joint configurations, and other variables. Armed with artificial intelligence and a highly adaptable laser welding process, the system commences and within minutes produces the perfect weld—every time.

Will this dream ever become a reality? No one can say at this point, but it’s an ideal worth striving for. To that end photonics scientists and engineers have made laser welding more controllable and adaptable than ever. And in this quest for laser welding perfection, beam shaping and manipulation continues to play a critical role.

Levels of Automation

To understand the true implications of shaping and manipulating the beam in laser welding, consider how the process fits within the broader landscape of autonomous manufacturing. You can think of levels of laser welding automation to be a little like the iterations the automotive industry has taken (and continues to take) toward developing the fully autonomous driving experience (see

Figure 1

).

At Level 0, the automation has zero autonomy. Someone needs to drive and maintain the car, just as an engineer or technician needs to program a laser. The car needs to be given direction; the laser system requires process development and detailed instructions.

Level 1 introduces cruise control, Level 2 lane assistance, and Level 3 has auto-braking and other conditional levels of automation whereby the driver is given assistance but must be ready to take control at all times. Levels 0 through 3 effectively describe laser welding’s current state in most production environments. Engineers and programmers test application parameters and design a welding cell around a laser beam with fixed optics, analogous to Level 0. At the upper end of the processing spectrum, lasers are coupled with real-time seam trackers that allow the system to adjust certain welding parameters like travel speed—analogous to a car’s auto-braking in Level 3.

No doubt, welding engineers continue to push the envelope. But when it comes to the laser system itself—both the laser source and optics—real-time adaptability has been limited. A laser can "autobrake" to, say, increase penetration, but for some applications slowing the travel speed (and increasing the heat input) might adversely affect the weld. Finer levels of control could help laser welding accomplish more and bring the process a little closer to that intelligent, adaptable, autonomous welding ideal.

Beam Manipulation and Shaping

Beam manipulation and shaping has been around for years, and one of the oldest forms is the twin spot technique. The beam emerges from the fiber delivery cable and through a collimation optic, like any solid-state-laser setup. But before the beam reaches the focusing lens, a wedge-shaped optic sends a portion of the beam at an angle to create a second spot. In this arrangement, the primary and secondary beams split the laser energy.

FIGURE 1 Self-driving vehicle development serves as a good analogy to illustrate the industrial laser’s journey toward fully autonomous operation.

FIGURE 2 In the twin spot technique, a leading secondary spot can be used for cleaning or preheating.

In some cases, the secondary spot can be designed to have as much as half the overall processing energy. In a typical laser welding application, though, the primary spot has about 80% of the processing energy while the secondary spot has 20% (in most cases, a secondary spot with less than 20% of the processing energy can become unstable). Again, this can be fine-tuned to the application (see

Figure 2

).

Regardless of the exact setup, a secondary spot can introduce a host of laser welding possibilities. In the "pre-running" configuration, the secondary spot runs ahead of the primary spot. In this arrangement the secondary spot can clean the path head of the processing beam, a good option to overcome challenges from surface imperfections and to accommodate adverse effects from outgassing in coated material. In other pre-running configurations, the secondary spot can serve a preheating role. In a trailing configuration, the secondary spot can play a postweld heat-treat role, controlling the weld pool’s cooling and solidification rates to minimize discontinuities and allowing time for impurities to escape the molten material.

FIGURE 3 This beam oscillation beam-shaping technique is used in a twin spot setup to mitigate outgassing effects on coated material. The sine wave indicates the oscillating path that the spots take as they travel across the weld.

Another type of beam shaping is

beam oscillation

, where optics oscillate the beam to distribute energy (heat) in advantageous ways (see

Figure 3

). In a keyhole welding setup, this might allow a spot that produces a very small keyhole (such as less than 0.4 mm) to melt a large fillet profile quickly and effectively. You get a wider area of penetration without resorting to the beam defocusing typically required in conduction-mode laser welding.

The oscillation also can help bridge the gap between base materials in less-than-perfect joint fitups. Laser welding still requires extremely good workpiece fit-ups, of course, but beam oscillation has at least helped ease the stringent fit-up requirements early adopters had to deal with in decades past (see

Figure 4

).

Welding engineers can adjust some beam oscillation parameters. For instance, they can change the oscillation amplitude and frequency. In this context, the amplitude and frequency refer to the shape of the sine wave created by the laser spot’s path as it travels forward along the joint, as shown in Figure 3.

Frequency is a function of the processing head’s travel speed. As its travel slows and the oscillation rate remains constant, the beam oscillates a greater number of times over a shorter distance, so the frequency increases. Amplitude establishes the path’s width (or

scan width

) and is controlled by the oscillation optics.

Beam oscillation cannot solve every welding problem on its own, though. Consider the lap fillet configuration in

Figure 5

, which shows a remote laser beam welding application involving aluminum, a heat-sensitive material. The beam power remains constant, but when the beam oscillates, the level of weld penetration changes. The beam spot size is small and the energy profile highly gaussian, so its penetration ability differs dramatically depending on exactly where the center of the spot is at a given moment during the welding cycle. And adjusting the oscillation amplitude and travel speed (oscillation frequency) can accommodate for only so much.

FIGURE 4 Beam oscillation in laser welding can help bridge gaps between workpieces.

Here’s where another beam-shaping technology can help. It’s called

temporal laser power modulation.

Again, an oscillating spot’s path can be viewed as a sine wave, and now the laser beam’s power can change as it travels along it. Adjusting the power as the spot travels from crest to trough along that sine wave can help shape and perfect a weld-penetration profile. (Power typically changes up to four times from the crest to the trough of a single sine wave; it theoretically could be adjusted more frequently, but attempting to implement such fine adjustments usually produces negligible benefits.)

Consider Figure 5 again. Across a scan width—that is, the distance from crest to trough in the oscillation; 2 mm, for example—the penetration changes if the laser power remains constant. Weld penetration starts strong at the crest, diminishes as it travels down the sine wave, then increases again as it approaches the trough before the beam oscillates the other direction.

Add laser power modulation and the story changes. The laser power increases as it moves down the sine wave and then decreases as it reaches the trough (toe of the fillet). The result: a consistent weld-penetration profile. This consistency can make the process more reliable and resilient, even in the face of material inconsistencies.

FIGURE 5 Synchronizing laser power modulation with the oscillation helps shape an ideal penetration profile.

FIGURE 6 A setup that involves real-time seam tracking, beam shaping, weld monitoring, and postweld inspection brings laser welding one step closer to fully autonomous operation.

Beam shaping happens at the laser source too. Today manufacturers offer lasers that can be "tuned" to a specific energy distribution profile—having attributes of gaussian profiles, ring profiles, and even combinations of both—to benefit a specific application. In fact, some advanced laser welding cells today actually incorporate these adaptable, "tunable" beams with other shaping and manipulation techniques, including laser power modulation.

The Next Level: Tracking and Inspection

Such advanced processes might be incredibly adaptable, but they still need manual intervention to adjust the parameters. Here is where tracking and inspection step into the picture.

Picture a setup in which a seam tracker leads the processing beam, after which an LED laser line inspects the cooled weld bead. A coaxial camera performs all the image acquisition for tracking and inspection. Such technology brings laser welding to Level 4 automation in Figure 1—a semiautonomous setup. The car drives itself, but the driver has the freedom to take over. In the context of laser welding, the seam tracker "steers" the process. The beam oscillation is synchronized with laser power modulation to control heat input. It also helps make the process adaptable. In some fillet applications, the adaptive scan and laser power modulation have bridged gaps that are nearly half the thickness of the thinner (usually top) base metal (see

Figure 6

).

The latest iterations of this technology are bidirectional. That is, the LED lines on either side of the active weld pool change roles—either seam tracking (before welding) or inspection (after welding)—depending on the direction of travel. In some applications this can help shorten cycle times significantly.

Closing the Gap on Level 5

At a most basic level, beam shaping simply gives engineers more "knobs to turn" for fine-tuning a laser welding process. The ultimate goal is to have those knobs turn themselves. Tracking and inspection help, and as more data is collected, the process will become even more intelligent.

This is where we are today, on the road to Level 5, at which point laser welding becomes truly autonomous. Many applications are starting to feed data to the cloud, where massive data sets might eventually make AI-based autonomous laser welding a reality.

The industry isn’t to Level 5 yet, of course. Some limitations are physical, like weld joints in confined spaces that make common tracking, monitoring, and inspection techniques inadequate. And that’s just one example. Complications abound.

Regardless, the "fully autonomous Level 5" ideal is worth striving for. And considering how far industrial lasers have come over the past 20 years, the industry might achieve Level 5—or at least come very close to it—in the not-too-distant future.

Information for this article came in part from presentations given at recent Advanced Laser Applications Workshops (ALAW), organized by the Fabricators & Manufacturers Association (FMA),

www.alawlaser.org

. The presentations were given by Sebastian Moser, director of sales, and Brian Smith, sales and service engineer, at Precitec Inc.,

www.precitec.us

. The company also is hosting FMA’s Laser Welding Technology Certificate course Sept. 22-24, 2020. For more information, visit

www.fmamfg.org/events

.