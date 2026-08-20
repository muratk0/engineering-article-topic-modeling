# MRP explained

[TARİH: 01.11.2020 ISMR]

MRP is a planning tool geared specifically to assembly operations. The aim is to allow each manufacturing unit to tell its supplier what parts it requires and when it requires them. The supplier may be the upstream process within the plant or an outside supplier. Together with MRP II, it is probably the most widely used planning and scheduling tool in the world. MRP was created to tackle the problem of ‘dependent demand’; determining how many of a particular component is required knowing the number of finished products. Advances in computer hardware made the calculation possible.

The process starts at the top level with a Master Production Schedule (MPS). This is an amalgam of known demand, forecasts and product to be made for finished stock. The phasing of the demand may reflect the availability of the plant to respond. The remainder of the schedule is derived from the MPS. Two key considerations in setting up the MPS are the size of ‘time buckets’ and the ‘planning horizons’. A ‘time bucket’ is the unit of time on which the schedule is constructed and is typically daily or weekly. The ‘planning horizon’ is how far to plan forward and is determined by how far ahead demand is known and by the lead times through the operation. There are three distinct steps in preparing an MRP schedule: exploding, netting and offsetting.

Explosion uses the Bill of Materials (BOM). This lists how many, of what components, are needed for each item (part, subassembly, final assembly, finished product) of manufacture. BOMs are characterised by the number of levels involved, following the structure of assemblies and sub-assemblies. The first level is represented by the MPS and is ‘exploded’ down to final assembly. Thus, a given number of finished products is exploded to see how many items are required at the final assembly stage.

The next step is ‘netting’, in which any stock on hand is subtracted from the gross requirement determined through explosion, giving the quantity of each item needed to manufacture the required finished products.

The final step is ‘offsetting’. This determines when manufacturing should start so that the finished items are available when required. To do so, a ‘lead time’ has to be assumed for the operation. This is the anticipated time for manufacturing.

The whole process is repeated for the next level in the BOM and so on until the bottom is reached. These will give the requirements and timings to outside suppliers.
