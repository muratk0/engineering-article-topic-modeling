# Cybersecurity risks with EV fast charging

[TARİH: 01.10.2024 ISMR]

Engineers at Southwest Research Institute (Texas, USA) have identified cybersecurity vulnerabilities with electric vehicles (EVs) using direct current fastcharging systems (the quickest, commonly used way to charge electric vehicles). The high-voltage technology relies on powerline communication (PLC) technology to transmit smart-grid data between vehicles and charging equipment. In a laboratory, the SwRI team exploited vulnerabilities in the PLC layer, gaining access to network keys and digital addresses on the charger and vehicle.

"Through our penetration testing, we found that the PLC layer was poorly secured and lacked encryption between the vehicle and the chargers," said Katherine Kozan, an engineer who led the project for SwRI's High Reliability Systems Department. The team found unsecure key generation present on older chips when testing, which was confirmed through online research to be a known concern.

In this latest project, SwRI explored vehicle-to-grid (V2G) charging technologies governed by ISO 15118 specifications for communications between EVs and electric vehicle supply equipment (EVSE) to support electric power transfer.

“As the grid evolves to take on more EVs, we need to defend our critical grid infrastructure against cyberattacks while also securing payments to charge EVs," said Vic Murray, assistant director of SwRI's High Reliability Systems Department. “Our research found room for improvements."

“Adding encryption to the network membership key would be an important first step in securing the V2G charging process," said FJ Olugbodi, an SwRI engineer who contributed to the project. “With network access granted by unsecure direct access keys, the non-volatile memory regions on PLC-enabled devices could be easily retrieved and reprogrammed. This opens the door to destructive attacks such as firmware corruption."

However, encrypting embedded systems on vehicles poses several challenges so SwRI has developed a zero-trust architecture that can address these. It connects several embedded systems using a single cybersecurity protocol. SwRI's future EV cybersecurity research will test zero-trust systems for PLC and other network layers.

"Automotive cybersecurity poses many layers of complexity, but we are excited about these new techniques to identify and address vulnerabilities," said Cameron Mott, an SwRI manager leading SwRI's automotive cybersecurity research.■
