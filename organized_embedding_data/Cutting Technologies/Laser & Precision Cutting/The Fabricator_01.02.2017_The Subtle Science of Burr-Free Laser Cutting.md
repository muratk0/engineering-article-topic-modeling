# The Subtle Science of Burr-Free Laser Cutting

[TARİH: 01.02.2017 The Fabricator]

Ensuring molten metal evacuates in the right way at the right time

By Tim Heston

A

n operator offloads a sheet of cut parts. Aside from the small parts tabbed in place, the cut pieces lift out of the nest to reveal clean edges, ready for the next operation. That’s the ideal, at least.

Quite oft en, of course, burrs (or dross) remain. Such imperfections may seem like par for the course, but many times operators can avoid them by making the right adjustments to the cutting parameters. To uncover them, operators need to know exactly what has to happen when the laser cutting beam, assist gas, and workpiece interact to create the perfect cut edge.

So what are these parameters? To find out,

The FABRICATOR

spoke with Charles Caristan, PhD, a technical fellow and global market director, fabrication and machinery, at Air Liquide’s Conshohocken, Pa., office. A longtime expert in laser cutting, Caristan is the author of Laser

Cutting Guide for Manufacturing

, published by SME.

So what’s the secret to burr-free laser cutting? There is no "one" secret, of course, but Caristan described some strategies that revolve around one element of laser cutting that’s largely under the operator’s control: the gas flow dynamics, or how the assist gas flows through the kerf.

Knowing Which Parameter to Change

For the most part, modern machines control the laser beam characteristics: specifically, the beam power (usually at the maximum) and beam profile. The beam focus, based on the focusing optic used, is set for particular material grades and thicknesses.

Technicians (and on modern systems, the machines themselves) may check myriad parameters, from beam alignment through the beam delivery system (in CO

2

lasers) to centering the nozzle, to calibrating the focus position to ensure that the focus position commanded on the CNC matches the true focus position on the workpiece for every lens diameter used.

For certain applications, having that focus spot too high in the cut can leave spiky dross; focusing too low in the cut yields slower cutting speeds and can leave beads, a telltale sign of "overflushing."

The focus position usually is saved as part of a cutting program table. The remaining parameters include the gas pressure, nozzle standoff, commanded laser power-frequency duty, and cutting speeds for various cut contours.

Many parameter adjustments are automated on modern systems, including changing the nozzle to a smaller or larger diameter. "This means the operator standing by the machine usually adjusts gas pressure, focus position, and cutting speed,"

Caristan said. "Sometimes they do whatever they need to do to get the job out, and they don’t necessarily adjust parameters in the right direction, at the cost of edge quality or manual dross filing." Say an operator notices a burr on the bottom of the cut edge on a stainless steel part. The operator’s first (and logical) reaction is to slow the cutting speed. "This just makes sense, because in his or her mind, the cutting head is traveling too fast, thus generating problems with repeatability and cutting performance," Caristan said.

In laser cutting, how the laser beam, assist gas, and material interact determines the quality of cut. Here, dross forms as molten material solidifies before it can be evacuated from the kerf.

After slowing down and changing the assist gas pressure to accommodate, the operator finds an even larger burr. What gives? The answer, Caristan said, lies in knowing exactly how the gas, beam, and material interact to create the burr in the first place.

What Creates the Burr?

Caristan began by describing the basics: The laser beam’s intense energy brings the metal beyond its melting temperature, and the dynamic action of the assist gas evacuates the molten metal from the kerf. When using nitrogen, an inert gas, the cutting process relies solely on the beam’s energy to melt the metal. When carbon steel is cut with an oxygen assist gas, the oxygen interacts with the hot metal to create an exothermic reaction, which adds heat.

"For that reason," Caristan said, "you don’t need as much gas pressure to actually eject the material. That’s why with oxygen cutting, you have much lower pressure and much slower dynamic flow of the assist gas."

In either case, burrs are created from the molten metal (and, in the case of oxygen cutting, slag) solidifying faster than it can be evacuated. That solidified material becomes a stalactite at the bottom of the kerf, which constitutes a burr.

What causes the metal to solidify faster than it can be evacuated? As Caristan explained, find the cause (or causes), and you’re on your way to a cleaner laser-cut edge.

Gas Dynamics

Operators ideally should make changes with quality, efficiency, and costs in mind, particularly when it comes to nitrogen assist gas. "Nitrogen assist gas can make up 35 to 50 percent of the variable costs in laser cutting," Caristan said, "so it’s important to control that consumption. Therefore, one of the first considerations when you set up cutting parameters is to minimize the nozzle diameter. That is, you choose the smallest nozzle diameter you can use to obtain the desired quality and performance."

He added that when it comes to assist-gas flow rate, the nozzle diameter makes a huge difference. If the operator increases the nozzle diameter by a factor of 2, the flow rate of gas increases by a factor of 4.

"Once you determine the smallest nozzle diameter, you determine the lowest possible pressure necessary to obtain a good-quality cut, where you have good molten-metal separation and no burrs," Caristan continued. "And you definitely don’t want to go too high on the pressure, or you end up increasing your flow rate proportionally."

Caristan reiterated that nitrogen cutting pressures are generally set above 150 PSI and as high as 375 PSI for thicker workpieces—much higher than relatively low-pressure oxygen cutting (28 PSI or lower, depending on the operation and material thickness). The pressure should be high enough, but, to save cost, no higher than necessary.

With the smallest "good" nozzle diameter determined, the operator then follows a rule of thumb and sets the standoft distance from the workpiece equal to one nozzle diameter. The reason for this isn’t entirely intuitive.

It’s true that setting the standoft too high causes the assist gas to have trouble evacuating the molten metal cleanly and eft iciently from the kerf. If the operator doesn’t know he should reduce the standoft distance, he increases gas pressure to compensate, increasing gas utilization and those variable costs.

But another reason maintaining a specific nozzle standoft is so critical has to do with, of all things, breaking the sound barrier, at least with nitrogen cutting. The gas flow becomes supersonic and, in doing so, produces a shock wave. When the nozzle is not at the right height, "those shock waves interact with the workpiece surface and the kerf in a negative way," Caristan said, adding that the same thing applies to spatter sticking on the nozzle’s edge or internal wall. The protruding spatter interrupts the gas flow dynamics and deflects that supersonic shock wave on the kerf. The shock wave makes the molten-metal evacuation erratic, and some metal cools before it exits the cutting area, solidifying while still hanging on to the bottom cut edge. In other words, you get a burr.

That’s why cutting with a clean nozzle is so critical. It’s also one reason that modern laser machines have sensors to detect nozzle obstructions and automatically clean nozzles to eliminate them.

On the inside, most nozzles are cylindrical and very capable for a variety of sheet thicknesses. Some nozzles, suited for a narrow range of (usually thicker) material, have a convergent and divergent shape, designed to give the gas flow enveloping the beam a similar convergent and divergent, or hourglass, shape.

The hourglass shape of the beam as it enters and exits its focus point, along with the location and nature of the exothermic reaction when oxygen cutting, creates that characteristic cut edge seen on thicker plate. "The thicker the material, the more difference you have in the gas dynamic and laser beam shape between the top and bottom surface of the cut," Caristan said. The edge is smooth on top and becomes rougher deeper in the cut, eventually turning into rough striations at the bottom.

The assist gas also interacts with ambient air. Hot gas molecules move faster than colder ones, and those molecules bombard the fast-moving molecules of the assist gas. Humid air also behaves differently than dry air. All this affects the gas flow dynamics. The nozzle diameter and gas pressure may be set one way on a morning in January and another substantially different way on a July Afternoon, all because of changes in ambient air temperature. So when determining optimal settings for cost-effective operation—again, smallest nozzle diameter and lowest pressure for a good cut—the operator needs to be aware of the effect of ambient air temperature from the start.

Slower Doesn’t Mean Better

The "smaller and lower" logic for nozzle diameter and gas pressure doesn’t apply to cutting speed. Caristan again described a typical situation when nitrogen-cutting stainless steel: that is, the operator slows the cutting speed to avoid burrs.

"When you go too slowly, you end up injecting more heat than is needed in the kerf. You end up raising the temperature to an extreme level, which causes vaporization that disturbs gas flow." That disturbance in turn causes more burrs, not less, which is why an operator can make cut quality worse by slowing the feed rate.

The operator essentially misinterpreted exactly what was happening in the kerf. The laser beam was dwelling a little too long at each point along the cut edge and, hence, induced excess heat and a little ablation. This disturbed the gas flow dynamics, which in turn did not evacuate the right amount of molten metal at the right time. It left some metal behind, which solidified into burrs at the bottom of the cut.

Knowing this, the operator could have prevented the burr by actually

increasing

the cutting speed slightly. That speed increase would reduce the heat input and the ablation, and restore the gas flow dynamics to its proper state.

Oxygen Cutting Considerations

When an operator switches to oxygen cutting for carbon steel, he also must consider the exothermic reaction. As Caristan explained, here is where oxygen purity level plays an important role.

Oxygen-cutting carbon steel benefits from higher oxygen gas purity levels. "It has been proven many times that, with both CO

2

and fiber lasers, increasing oxygen global purity to 99.95 percent or above—to 99.98 or 99.99 percent—we can increase the cutting speed in production significantly, sometimes between 30 and 40 percent."

If an oxygen dewar or cylinder has a drop in purity level, that impurity is usually argon. This is because when the oxygen gas is being produced cryogenically in an air-separation unit, both oxygen and argon liquefy at very similar temperatures.

The argon impurity doesn’t change the gas dynamics, or how the assist gas flows through the cut. "But argon is heavier than the oxygen molecules and has very different thermal conductivity characteristics," Caristan said. "So when you add argon to the mix, you alter the chemical interaction between the mostly oxygen assist gas and the molten metal."

This changes the exothermic reaction, which can in turn aft ect the cutting performance. The exothermic reaction works in conjunction with the gas flow rate (again, much lower than in nitrogen cutting) to burn and evacuate molten material and slag. If that molten material and oxidized slag aren’t removed effectively, it remains as a burr on the cut edge.

Don’t Forget the Plumbing

Most laser cutting system installers know to avoid elbows in the gas plumbing (which can induce pressure drops) or to oversize the piping diameter to compensate for pressure drops if elbows are unavoidable.

"One more thing: When you have downtime, and gas is not flowing to the laser, air is penetrating and filling the pipe," Caristan said, which can cause problems when the laser is restarted for the next shift or operation. "Unless you purge the atmosphere in the pipe, you will still have cutting difficulties because your [assist] gas is contaminated."

A Subtle Science

It can seem like a juggling act to avoid burrs and obtain a clean cut edge. But it really boils down to the laser beam parameters and the gas dynamics. Some beams may call for far different gas dynamics. For instance, fiber and disk lasers, Caristan explained, are highly focusable and yield small spots that create a narrow kerf; narrower kerfs require higher gas flow rates and thus pressure to evacuate the molten material properly (though modern iterations of the technology have longer focal lengths and beam characteristics suited for thicker material). Although the beam wavelength and profile may be different, fiber lasers and the assist gas still work together.

Attaining a burr-free cut is about ensuring the beam parameters and gas dynamics work together to ensure the right amount of molten metal evacuates the kerf at the right time and in the right way. If operators and technicians try to solve cut quality problems without considering the process fundamentals, they may be shooting in the dark.

Senior Editor Tim Heston can be reached at

timh@thefabricator.com

.

Illustration courtesy of Airgas, an Air Liquide company, 866-924-7427,

www.airgas.com/industries/manufacturing-metal-fabrication

.