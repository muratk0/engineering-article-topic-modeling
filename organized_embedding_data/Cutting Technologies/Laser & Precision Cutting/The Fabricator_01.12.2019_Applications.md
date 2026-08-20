# Applications

[TARİH: 01.12.2019 The Fabricator]

Technology

Laser peening system conquers adaptive limitations with PC control

Situation

LSP Technologies (LSPT), Dublin, Ohio, is a pioneer of laser peening, a process that helps engineers increase the strength of metals in manufactured goods. The peening process bombards a metal workpiece with other objects to press the material into itself, making it denser and stronger and mitigating the effects of metal fatigue. In laser peening, a high-powered beam is directed at the metal surface while a stream of water flows over the workpiece. The beam impacts the surface of the metal, creating a small explosion between the water and the surface of the part, which forces the shock waves to travel deep into the metal, thus creating a material with a higher fatigue life.

One of the company’s newest laser peening systems is the modular Procudo®. This self-contained, turnkey system is tailor-made for use at customer facilities, so its design is never final. Some iterations feature machine cells the size of large rooms to accommodate multiple articulated robots.

Metal parts, especially large or awkwardly shaped components, often are difficult to move within a machine cell when accommodating fixed-position lasers. This is particularly challenging with workpieces like massive ship hulls and anchors in the maritime industry, for example. "In the past, we generally used part-to-beam processing by aiming the laser at a fixed point in the processing cell and then moving the parts with robotics," said David Lahrman, vice president of business development at LSPT. "To process very large parts, however, we now use beam-to-part processing, which involves moving the laser with robotic arms from KUKA robots to peen areas that require treatment."

Flexibility is key, since each customer has unique requirements. Whenever the company’s engineers install new systems or process new components in-house, they must make significant changes. It is not as simple as shipping out a prepackaged product. For this reason, it is critical that the automation and controls technology used in the new laser peening systems be highly scalable. The equipment must be able to handle workpieces that are very large, as well as others that focus on the smallest, most precise details.

Standardization and synchronization of the technology also are important factors. Dynamic software and hardware systems must communicate and cooperate seamlessly, even in multivendor applications.

Resolution

To meet the system’s complex requirements, LSPT contacted Beckhoff Automation, interested initially in its interface options, including HMI hardware that is customizable for a variety of applications and rugged enough for industrial environments. Both the built-in CP2912 multitouch control panel and the pole-mounted CP3913 multitouch control panel offer LSPT the options needed for unique client demands, according to Controls Engineer Alex Portolese: "For smaller Procudo laser peening system designs that require stand-alone HMI panels, we implement the CP3913 to interface with the finer controls of the laser system. However, the CP2912 is the standard control panel for the … system, as it works well for custom applications and mounts directly to electrical cabinets."

LSPT also uses the Beckhoff CX2040 embedded PC, featuring quadcore, 2.1-GHz Intel® Core™ i7 processors, to run HMI, connect to the cloud, and communicate with the laser peening system and higher-level systems. "With the addition of SQL databases, this allows us to maintain compact electrical cabinet footprints," Portolese explained.

However, the laser peening system’s standard control hardware for robotics and other laser peening functions is the C5240 industrial PC (IPC). Electrical Engineer Avery Calhoun sees additional benefits in the 19-inch rack-mount PC, which uses up to quad-core Intel Core i7 processors of the sixth and seventh generation: "The C5240 is very powerful and provides ample serial and Ethernet ports to connect with the EtherCAT I/O system. The IPC’s form factor is also easy to incorporate with our other rack-mount components."

TwinCAT 3 automation software gives LSPT the flexibility to complete all programming in a standard engineering environment, according to Keith Glover, head of electrical engineering at LSPT. In addition, TwinCAT can scan and automatically configure third-party devices over ADS and Ether-CAT, reducing commissioning times for laser peening systems that feature multivendor architectures. "Fast communication with third-party industrial devices or existing factory fieldbuses is a key advantage of TwinCAT," Glover said. "Implementing special protocols in serial modules and TCP-IP modules, for example, is easier with the Beckhoff platform compared to others." This helps when implementing complex systems with robotics.

As a KUKA Gold partner, LSPT implements multiple articulated robots to move lasers, and sometimes also workpieces, to ensure that the beams strike parts with high accuracy. AM8000 servomotors from Beckhoff help move the beam closer to the target part to complete the laser peening process.

As the fastest fieldbus, EtherCAT provides communication for more than the robotics in the modular laser peening system. Inside the machine cells where high moisture is present, LSPT uses water-resistant, IP67-rated EtherCAT Box modules; in electrical cabinets, it uses standard EL-series EtherCAT I/O terminals because of their compact design and numerous channels for all common sensors, actuators, and other field devices.

The Procudo system emits an 8- to 16-nanosecond pulse containing 10 joules of energy. While the laser has a standard repetition rate of 20 hertz, it also can achieve firing speeds from 1 to 200 Hz. As a result of the high synchronization possible with TwinCAT and EtherCAT, the system can process up to 29 square inches of material per minute. In addition, the laser peening system remains highly customizable through open, scalable technologies.

"What led us to choose Beckhoff from the technology side was the speed and real-time determinism of EtherCAT and TwinCAT. The ability to have the same networking and software combination on the same device with high-speed data sharing was critical," said Glover. "Additionally, the ability to synchronize motion with the laser output is critical to the repeatability and quality of our processes, enabling us to reliably provide the benefits of laser peening to customers across many industries."

Beckhoff Automation

www.beckhoffautomation.com

Custom sheet metal parts solve storage space limitations in outer space

Situation

Five decades after mankind first set foot on the moon, NASA is developing the Orion spaceship, which will launch astronauts back into lunar orbit, to the moon’s surface, and, if all goes as scheduled, to Mars.

Lockheed Martin, a major NASA contractor, is designing parts of the infrastructure that will support NASA’s Gateway, a space port that will orbit the moon. In a Florida building, the company is constructing an earthbound, full-sized physical model of the living quarters portion of the Gateway, called the Habitat Ground Test Article (HGTA). The space-based version of this module will provide a comfortable environment for astronauts on their long journeys and currently is scheduled to launch in 2024. It will dock with another module that will generate power and propulsion, which will launch in 2022.

Not surprisingly, to accommodate astronauts traveling through the vastness of space, Lockheed Martin has to consider small but critical details—like storage—as carefully as big ones.

Resolution

For sheet metal fabrication for the HGTA’s storage modules, the aerospace company decided to work with Protolabs; the companies have partnered before, including producing prototype parts for a portable drone.

Jeff Budny, a Lockheed Martin systems integration engineer, visited Protolabs’ Nashua, N.H., facility to ensure that the company’s sheet metal fabrication capabilities were up to the task, and the build began soon thereafter.

Protolabs’ framework had to be lightweight to maximize fuel efficiency but also strong enough to hold heavy objects in place and survive the jostling that is inherent during a rocket launch. Cargo and experiments can’t tumble down from a storage rack midflight, so the system needed to be able to maintain its integrity when confronted with excessive g-forces.

Lightweight but strong aluminum proved the best material for this project. "The parts that Protolabs created for this project will have to last for an entire generation—the lifetime of the project," said Chris Cloutier, Lockheed Martin’s Advanced Programs prototype lead. "That means modularity is especially important so we can adapt the structure to meet tomorrow’s needs." The storage area Lockheed Martin and Protolabs created can easily change configurations to accommodate today’s experiments or whatever might be needed in the future.

Safety also was taken into consideration, as an injury 200,000 miles from Earth can result in tragedy. To that end, Protolabs used techniques such as chamfering to craft parts carefully and eliminate sharp edges.

Some parts also have complex bends, which Protolabs manufactured to tight specifications. When completed, the parts were shipped to Florida for what Cloutier referred to as "easy assembly."

The parts for this next-generation space mission now are installed in the HGTA, and Lockheed Martin’s designs are entering a test phase. NASA astronauts will soon experience the HGTA environment for themselves and help determine if the model meets their needs and expectations. As part of the testing, they will be looking closely at the storage modules that Protolabs fabricated.

Protolabs

www.protolabs.com