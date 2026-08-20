# Getting your tube bender on solid ground

[TARİH: 01.05.2026 The Fabricator]

Exploring Tube Benders

Proper electrical grounding ensures safety and machine reliability

By

Jay Robinson

sabelskaya/iStock/Getty Images Plus

L

ate one Friday afternoon, I got the call that tube bender technicians absolutely dread: "Our machine has been down for a week, and we have to have it running by Monday!"

After traveling that night and arriving on-site Saturday morning, I came across a real head-scratcher: The machine would home, run a few parts, and then the bend arm would either slam back against the machine or not fully return.

The machine had recently been moved across the entire plant. In addition to connecting the machine to the building ground with the main power, the customer had drilled through the concrete next to the machine and installed a ground rod directly into the earth and bonded the frame of the machine to it. The shop had done the same thing when the bending machine was originally installed.

Grounding industrial machinery is one of the most fundamental—and often overlooked—elements of electrical safety in manufacturing plants. Whether in fabrication, CNC machining, or automated production lines, proper grounding protects people, equipment, and processes from potentially catastrophic failures.

WHAT GROUNDING IS AND WHY IT MATTERS

Grounding is the intentional connection of electrical systems and equipment to the earth. This creates a low-resistance path for fault currents, allowing excess or unintended electrical energy to dissipate safely into the ground rather than passing through a person or damaging machinery.

Protect People from Electric Shock.

The most critical role of grounding is safeguarding workers. If a fault occurs—such as a short circuit where a live conductor contacts a machine frame—the metal surfaces can become energized. Without grounding, touching the machine could result in severe injury or death.

A properly grounded system ensures that:

Fault current flows directly to ground.

Protective devices such as breakers or fuses trip quickly.

Dangerous voltage is removed almost instantly.

Prevent Equipment Damage.

Industrial machines like CNC tubing benders, mills, and robotic systems rely on sensitive electronics, including PLCs, drives, and control boards. Improper grounding can lead to voltage spikes, electrical noise, and erratic machine behavior.

Grounding stabilizes voltage levels and provides a reference point, helping protect components from transient surges and reducing long-term wear.

Reduce Electrical Noise and Interference.

Modern industrial equipment often combines high-powered motors with low-voltage control systems. Without proper grounding, electromagnetic interference can disrupt signals. This can cause false sensor readings, communication errors, and inconsistent machine operation.

A solid grounding system also helps maintain signal integrity, which is especially important in precision operations.

Ensure Proper Operation of Protective Devices.

Circuit breakers and fuses rely on sufficient fault current to trip. If grounding is poor or nonexistent, fault currents may be too low to trigger protection. This creates a dangerous condition in which equipment can appear to operate normally even though hidden faults remain active. This can increase risk of fire or shocks. Grounding ensures faults are detected and cleared quickly.

Minimize Fire Risk.

Ungrounded or improperly grounded systems can allow stray currents to flow through unintended paths, generating heat. Over time, this can lead to insulation breakdown and electrical fires. A proper grounding path directs fault current safely away from operators and the machine, prevents overheating of unintended conductors, and reduces ignition risks.

SPECIAL CONSIDERATIONS FOR INDUSTRIAL MACHINERY

Grounding the Frame.

All exposed metal parts of machinery should be bonded and connected to a reliable earth ground. This ensures that any fault energizing the frame is immediately neutralized.

Avoiding Ground Loops.

While grounding is essential, improper implementation can create ground loops—multiple ground paths that introduce noise. Best practices include:

Single-point grounding for control systems.

Proper shielding and cable routing.

Separation of power and signal grounds when necessary.

IMPORTANCE OF GROUNDING THE 0V SIDE OF DC POWER SUPPLIES

In modern industrial machinery—especially CNC equipment, PLCs, and automated lines—DC power supplies (commonly 24 VDC) are used extensively for sensors, controls, and communication. While the practice of grounding the 0V (common) side of the DC power supply is often misunderstood, it’s also highly important for several reasons.

Grounding the Control System.

Control panels, PLCs, and DC power supplies should have a clean, stable ground reference. In many CNC systems, grounding the 0V side of the DC supply helps to stabilize signals while reducing noise and improving repeatability.

Establishing a Stable Voltage Reference.

Grounding the 0V side creates a fixed reference point for the entire control system. Without this reference, voltage levels can "float," which means that signals may become unstable and measurements between devices might vary unpredictably.

By tying the 0V to an earth ground, all components share the same baseline, ensuring consistent and accurate operation.

Improving Noise Immunity.

In industrial environments, motors, variable- frequency drives, and switching devices generate interference—basically, they are electrically noisy. A grounded 0V provides a path for noise to dissipate, reduces voltage fluctuations on signal lines, and improves the reliability of analog and digital signals.

This is especially important for:

Analog inputs (0 to 10V, 4 to 20 mA).

Communication systems.

High-speed I/O, like encoders.

Reducing Risk of Ground Loops.

While improper grounding can create loops, intentional single-point grounding of the 0V, when done correctly, actually helps prevent them.

To achieve grounding without introducing circulating currents, ground the 0V at one location only, typically inside the main control panel. Also be sure to avoid multiple ground connections along the system.

Protecting Sensitive Electronics.

PLCs, HMIs, sensors, and communication modules are sensitive to voltage instability. For these components, grounding 0V helps prevent transient voltage spikes, reduce stress on internal components, and extend the lifespan of your electronics.

BEST PRACTICES FOR GROUNDING DC SYSTEMS

When establishing a solid ground for DC systems:

Bond the 0V to earth ground at a single, clearly defined point.

Avoid grounding the 0V at multiple locations.

Separate high-power grounds from signal grounds, then bond at one point.

Follow manufacturer recommendations for drives, PLCs, and power supplies.

MAKING SENSE OF THE MACHINE

Regarding the machine with the wonky bend arm, I noticed that even when the machine was idle, the counts from the bend arm encoder would change a little bit every few minutes.

Thinking something was wrong with the bend arm’s encoder, I physically removed it from the machine and swapped it with a spare the shop had. But even with the new encoder, we got the same result. I swapped the cable back to the original encoder (still disconnected from the machine), and the counts were rock steady! Holding the encoder, I touched the body of it to the frame, and the counts took off running, even though the encoder shaft was stationary.

As it turned out, there was a measurable difference in voltage between the ground from the ground rod and the building ground pulled in with the supply wires. This difference was creating a ground loop.

When I measured the voltage between the 0V side of the DC power supply and the ground source, there was as much as 5 to 10 VDC showing. That meant that the system essentially had a floating reference, which was causing the control to see counts from the encoder that were not really there.

Utimately, we added a copper ground wire from the ground rod to the same grounding point as the building ground and also tied the 0V side of the DC power supply to the same ground point. With a fixed reference point, the feedback from the bend arm’s encoder became stable and repeatable.

BOTTOM LINE

We tend to think of machine grounding only in terms of safety, but proper grounding also improves machine accuracy and reliability.

Grounding the 0V side of a DC power supply is essential for both safety and performance. It stabilizes voltage, reduces electrical noise, improves fault detection, and protects both operators and equipment.

In industrial machinery, a floating DC system may appear to work, but a properly grounded one is far more predictable, diagnosable, and safe.

Jay Robinson

is owner of Robinson Bender Services and Automation Inc.,

rbsaindustrial.com

.

Roll. Punch. Bend. Better.

Your source for metal fabricating machinery: Ironworkers, Plate & Angle Bending Rolls, Angle & Plate Processing Lines, and more!

Backed by unmatched service and decades of industry experience, Trilogy partners with top manufacturers to bring proven performance to your shop floor.

EXPLORE our exclusive brands.

TrilogyMachinery.com

/ 888.988.7865